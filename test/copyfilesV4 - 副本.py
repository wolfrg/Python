#coding:utf8
'''
Created on 2016年12月13日
#脚本目标：检验源与备份目录差异
@author: wolfrg
'''
import os,sys
import  filecmp
import re
import shutil


holderlist = []

def compareme(dir1,dir2):
    dircomp=filecmp.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only
    diff_in_one=dircomp.diff_files  #不匹配文件，源目录文件已经发生变化
    #dirpath=os.path.abspath(dir1)   #定义源目录绝对路径
    #print only_in_one
    #将更新文件或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    
    #判断是否存在相同子目录，以便递归
    if  len(dircomp.common) > 0:
        for item in dircomp.common_dirs: #递归子目录
            compareme(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
            
    return holderlist

def main():
    if len(sys.argv) >2:
        dir1=sys.argv[1]
        dir2=sys.argv[2]
    else:
        print "Usage:",sys.argv[0],"datadir backupdir"
        sys.exit()
        
        
    diff_files=compareme(dir1, dir2)
    dir1=os.path.abspath(dir1)
    
    if not dir2.endswith('/'):dir2=dir2+'/'
    dir2=os.path.abspath(dir2)
    destination_files = []
    createdir_bool=False
    
    
    #遍历返回的差异文件或目录
    for item in diff_files:
        destination_dir=re.sub(dir1,dir2,item)
        
        destination_files.append(destination_dir)
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True #再次调用compareme函数标记
                
                
                
        #重新调用compareme函数，重新遍历新创建目录的内容        
        if createdir_bool:
            destination_files = []
            source_files = []
            source_files=compareme(dir1, dir2)  #调用compareme函数
            for item in source_files: #获取源目录差异路径清单，对应替换成备份目录
                destination_dir=re.sub(dir1,dir2,item)
                destination_files.append(destination_dir)
                
                
                
        print "update item:"
        print diff_files #输出更新项清单        
        copy_pair=zip(source_files,destination_files) #将源目录与备份目录文件清单拆分成元组
        
        for item in copy_pair:
            if os.path.isfile(item[0]):
                shutil.copyfile(item[0], item[1])
  
                
if __name__=='__main__':
    main()        
               
