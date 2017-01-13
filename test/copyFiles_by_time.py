#coding:utf8
'''
Created on 2016年6月30日

@author: wolfrg
'''


'''file_list = []

file_list.append("c:/file_mo/")
print file_list'''

import os,time,shutil

def  copy_changed_file(src,dst):
    
    src_files = os.listdir(src)
    filecopyNum = 0
    for file  in src_files:
        
        src_path = os.path.join(src,file)
        dst_path = os.path.join(dst,file)
        source_file = os.path.normpath(src_path)
        destination_file = os.path.normpath(dst_path)
        
        if  os.path.isdir(src_path):
            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)
            filecopyNum +=  copy_changed_file(src_path, dst_path)
        
       
        elif  os.path.isfile(src_path):
              shutil.copy2(src_path, dst_path)
              filecopyNum += 1
              print "复制成功"
    
    #print source_file  
    print src_path      
    return filecopyNum
       




#调用函数
copy_changed_file("c:/file_mo", "d:/file_mo")    
           