#coding:utf8
import os
import shutil
def copyFiles():
    
    src_path = "c:\\file_mo\\"
    dst_path = "d:\\file_mo\\"
    for  files in os.walk(src_path):
        shutil.copyfile(src_path, dst_path)
        print ("复制成功")
    
    


copyFiles()