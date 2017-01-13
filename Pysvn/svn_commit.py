#coding:utf8
'''
Created on 2017年1月10日

@author: wolfrg
'''
from optparse import OptionParser 
import sys 
import os.path, shutil, stat 
import tempfile 
import pysvn
import re 
 
class TagClient: 
    def __init__(self, url, svndir, tagdir): 
        self.url = url 
        self.svndir = svndir 
        self.tagdir = tagdir 
        self.message = "Tag %s as %s" % (svndir, tagdir) 
 
        self.svnclient = NotifiedClient() 
        self.svnclient.callback_get_log_message = self.get_tag_message 
 
    def get_tag_message(self): 
        return True, self.message 
 
    def doIt(self): 
        self.svnclient.copy(os.path.join(self.url, self.svndir), 
                            os.path.join(self.url, self.tagdir)) 
 
def notify(event_dict): 
    if event_dict['action'] == pysvn.wc_notify_action.delete: 
        sys.stdout.write("Removing %s\n" % (event_dict['path'])) 
    elif event_dict['action'] == pysvn.wc_notify_action.add: 
        sys.stdout.write("Adding %s\n" % (event_dict['path'])) 
    elif event_dict['action'] == pysvn.wc_notify_action.copy: 
        sys.stdout.write("Copying %s\n" % (event_dict['path'])) 
 
def NotifiedClient(): 
    client = pysvn.Client() 
    client.callback_notify = notify 
    return client 
 
## 
## Check to see if a node (path) exists. If so, returns an entry oject for it. 
## 
def svn_path_exists(svn_url, svn_dir): 
    client = NotifiedClient() 
    head = pysvn.Revision(pysvn.opt_revision_kind.head) 
 
    try: 
        entry = client.info2(os.path.join(svn_url, svn_dir), 
                             revision = head, 
                             recurse = False)[0] 
        return entry 
    except pysvn._pysvn.ClientError: 
        return None 
 
## 
## Create a directory in svn (and any parents, if necesary) 
## 
def make_svn_dirs(svn_url, svn_import_dir): 
    client = NotifiedClient() 
 
    entry = svn_path_exists(svn_url, svn_import_dir) 
    if entry: 
        if entry[1]['kind'] == pysvn.node_kind.dir: 
            return True 
        else: 
            sys.stderr.write("\nError: %s exists but is not a directory.\n\n" % (svn_import_dir)) 
            raise pysvn.ClientError 
    else: 
        make_svn_dirs(svn_url, os.path.dirname(svn_import_dir)) 
        client.mkdir(os.path.join(svn_url, svn_import_dir), 
                     "Creating directory for import") 
 
def contains_svn_metadata(dir): 
    for root, dirs, files in os.walk(dir): 
        if '.svn' in dirs or '.svn' in files: 
            return True 
    return False 
 
## 
## Checkout an svn dir to a temporary directory, and return that directory 
## 
def checkout_to_temp(svn_url, svn_dir): 
    workingdir = tempfile.mkdtemp(prefix="svn-load") 
 
    client = NotifiedClient() 
    client.checkout(os.path.join(svn_url, svn_dir), 
                    os.path.join(workingdir, 'working')) 
 
    return workingdir 
 
## 
## return a list of files that exist only in dir1 
## 
def unique_nodes(dir1, dir2): 
    unique = [] 
    for root, dirs, files in os.walk(dir1): 
        if '.svn' in dirs: 
            dirs.remove('.svn') 
        for path in files + dirs: 
            relpath = os.path.join(root, path)[len(dir1)+1:] 
            counterpath = os.path.join(dir2, relpath) 
            if not os.path.exists(counterpath): 
                unique.append(relpath) 
 
    return unique 
 

## Generate the header line for the move menu 
## 
def move_menu_generate_header(delcolhead, addcolhead, delcollen): 
    delcollen = max(delcollen, len(delcolhead)) 
    header = " " * 5 
    header = header + delcolhead 
    header = header + (delcollen - len(delcolhead) + 1) * " " 
    header = header + addcolhead + "\n" 
    return header 
 
 
## 
## Generate a row in the move menu 
## 
def move_menu_generate_row(num, delfile, addfile, delcollen): 
    deleted = delfile + '_' * (delcollen - len(delfile) - 1) 
    return("%4d %s %s\n" % (num, deleted, addfile)) 
 
def move_menu_prompt(): 
    return("Enter two indexes for each column to rename, (R)elist, or (F)inish: ") 
 
def move_node(workingdir, src, dest): 
    client = NotifiedClient() 
    make_svn_dirs("", os.path.dirname(os.path.join(workingdir, dest))) 
    client.move(os.path.join(workingdir, src), 
                os.path.join(workingdir, dest)) 
# ## Clear out the removed files 
# shutil.rmtree(os.path.join(workingdir, src)) 
 
def remove_nodes(workingdir, newdir): 
    dellist = unique_nodes(workingdir, newdir) 
    fqdellist = [ os.path.join(workingdir, p) for p in dellist ] 
    client = NotifiedClient() 
    client.remove(fqdellist) 
 
## 
## Overlay the new tree on top of our working directory, adding any 
## new nodes along the way 
## 
def overlay_files(workingdir, newdir): 
    client = NotifiedClient() 
 
    for root, dirs, files in os.walk(newdir): 
        for f in files: 
            fullpath = os.path.join(root, f) 
            relpath = fullpath[len(newdir)+1:] 
            counterpath = os.path.join(workingdir, relpath) 
            if os.path.isdir(counterpath): 
                sys.stderr.write("Can't replace directory %s with file %s.\n" 
                                 % (counterpath, fullpath)) 
                return False 
            needs_add = False 
            if not os.path.exists(counterpath): 
                needs_add = True 
            shutil.copy(fullpath, counterpath) 
            if needs_add: 
                client.add(counterpath) 
        for d in dirs: 
            fullpath = os.path.join(root, d) 
            relpath = fullpath[len(newdir)+1:] 
            counterpath = os.path.join(workingdir, relpath) 
 
            if not os.path.exists(counterpath): 
                shutil.copytree(fullpath, counterpath) 
                client.add(counterpath) 
                # Added entire subtree, no need to recurse down it 
                ## FIXME: this isn't working - seems to make loop 
                ## end prematurely 
                #dirs.remove(d) 
            elif not os.path.isdir(counterpath): 
                sys.stderr.write("Can't replace file %s with dir %s.\n" 
                                 % (counterpath, fullpath)) 
                return False 
            # else, its a directory that already exists, but we still 
            # need to recurse down it. 
 
## 
## An instance of the move menu 
## 
def move_menu(workingdir, newdir): 
    # make these variables in case of future localization 
    delcolhead = 'Deleted' 
    addcolhead = 'Added' 
 
    deleted = unique_nodes(workingdir, newdir) 
    added = unique_nodes(newdir, workingdir) 
 
    if not deleted and not added: 
        # Nothing to do 
        return 
 
    menu_pair = re.compile("^(?P<src>\d+)\s+(?P<dest>\d+)$") 
 
    while deleted and added: 
        # The deleted column should be as wide as the longest path 
        # in that column or the length of the 'Deleted' string, whichever 
        # is greater 
        delcollen = max([len(i) for i in deleted] + [len(delcolhead)]) + 1 
        header = move_menu_generate_header(delcolhead, addcolhead, delcollen) 
        sys.stdout.write(header) 
 
        # 
        # Display the menu, row-by-row 
        # 
        for i in range(max([len(deleted), len(added)])): 
            delcell = "" 
            if len(deleted) > i: 
                delcell = deleted[i] 
            addcell = "" 
            if len(added) > i: 
                addcell = added[i] 
            row = move_menu_generate_row(i, delcell, addcell, delcollen) 
            sys.stdout.write(row) 
 
        prompt = move_menu_prompt() 
        sys.stdout.write(prompt) 
        input = sys.stdin.readline()[:-1] 
        if input in ['r', 'R']: 
            continue 
        if input in ['f', 'F']: 
            return 
        m = menu_pair.match(input) 
        if m: 
            srcindex = int(m.group('src')) 
            destindex = int(m.group('dest')) 
 
            if srcindex > len(deleted) or destindex > len(added): 
                sys.stderr.write("Error: Invalid index.\n") 
                continue 
 
            src = deleted[srcindex] 
            dest = added[destindex] 
            move_node(workingdir, src, dest) 
 
            del deleted[srcindex] 
 
            # If we moved a node into a subtree that didn't yet exist, 
            # then move_node politely created it for us. That was nice of her. 
            # Let's remove those directories from our 'added' list - we can't 
            # move a directory to a name that already exists. 
            head = dest 
            while head: 
                if head in added: 
                    added.remove(head) 
                (head, tail) = os.path.split(head) 
 
            # If we just moved a directory, its subtree went with it and 
            # can't move again. Remove subtree nodes from the deleted list so 
            # the user can't try it. If this proves to be a desired feature, 
            # we'll need to do multiple commits. Otherwise, users should 
            # move subtree components first, and then move the whole directory 
            if os.path.isdir(os.path.join(workingdir, dest)): 
                for node in deleted: 
                    if node[:len(src)+1] == src + '/': 
                        deleted.remove(node) 
        else: 
            sys.stderr.write("Error: Invalid input.\n") 
            continue 
 
## treats u+x as the canonical decider for svn:executable 
## should probably see if svn import does it differently.. 
def is_executable(f): 
    s = os.stat(f) 
    return s[stat.ST_MODE] & 0500 == 0500 
 
def svn_is_executable(file): 
    client = NotifiedClient() 
 
    for path, prop_list in client.proplist(file): 
        if prop_list.has_key('svn:executable'): 
            return True 
    return False 
 
def svn_set_exec(file): 
    client = NotifiedClient() 
    client.propset('svn:executable', '*', file) 
 
def svn_clear_exec(file): 
    client = NotifiedClient() 
    client.propdel('svn:executable', file) 
 
def sync_exec_flags(workingdir): 
    client = NotifiedClient() 
 
    for root, dirs, files in os.walk(workingdir): 
        if '.svn' in dirs: 
            dirs.remove('.svn') 
        for f in files: 
            path = os.path.join(root, f) 
            if is_executable(path) and not svn_is_executable(path): 
                svn_set_exec(path) 
            if not is_executable(path) and svn_is_executable(path): 
                svn_clear_exec(path) 
 
def remove_leading_slashes(path): 
    while os.path.isabs(path): 
        path = path[1:] 
    return path 
 
if __name__ == '__main__': 
    usage = "usage: %prog [options] svn_url svn_import_dir [dir_v1 [dir_v2 [..]]]" 
    parser = OptionParser(usage=usage) 
    parser.add_option("-t", dest="tagdir", 
                      help="create a tag copy in tag_dir, relative to svn_url", 
                      metavar="tag_dir") 
 
    (options, args) = parser.parse_args() 
 
    if len(args) < 3: 
        sys.stderr.write("Invalid syntax.\n") 
        parser.print_help() 
        sys.exit(1) 
 
    url = args[0] 
    client = NotifiedClient() 
    if not client.is_url(url): 
        sys.stderr.write("Error: %s is not a valid svn url.\n") 
        sys.exit(1) 
 
    import_dir = remove_leading_slashes(args[1]) 
 
    dirs = args[2:] 
 
    # Check to make sure the user isn't trying to import an svn working dir 
    for d in dirs: 
        if contains_svn_metadata(d): 
            sys.stderr.write("Error: %s contains .svn dirs or files\n" % (d)) 
            sys.exit(1) 
 
    for d in dirs: 
        d = os.path.abspath(d) 
        make_svn_dirs(url, import_dir) 
        if options.tagdir: 
            make_svn_dirs(url, os.path.dirname(options.tagdir)) 
 
        workingparent = checkout_to_temp(url, import_dir) 
        workingdir = os.path.join(workingparent, 'working') 
        move_menu(workingdir, d) 
        remove_nodes(workingdir, d) 
        overlay_files(workingdir, d) 
        sync_exec_flags(workingdir) 
        client.checkin(workingdir, "Committing") 
        shutil.rmtree(workingparent) 
    if options.tagdir: 
        t = TagClient(url, import_dir, options.tagdir) 
        t.doIt()