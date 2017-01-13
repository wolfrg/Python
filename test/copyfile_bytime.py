#coding:utf8
'''
Created on 2016年6月30日

@author: wolfrg
'''
import os,shutil

def copyfiles_bytime(src,dst):
    
    if os.stat(src).st_mtime - os.stat(dst).st_mtime >1:
        shutil.copy2(src, dst)
        print "文件复制成功!"
        
    else:   
        print "文件没有变化!"    
        
        

copyfiles_bytime("c:/1/1.txt", "c:/2/1.txt")