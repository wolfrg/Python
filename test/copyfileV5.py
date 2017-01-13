#coding:utf8
'''
Created on 2016年12月15日

@author: wolfrg
'''
import os, sys
import  filecmp
import re
import shutil


holderlist = []

def compareme(dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only
    diff_in_one = dircomp.diff_files  # 不匹配文件，源目录文件已经发生变化
    # dirpath=os.path.abspath(dir1)   #定义源目录绝对路径
    
    # 将更新文件或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]
    #print x
    # 判断是否存在相同子目录，以便递归
    if  len(dircomp.common) > 0:
        for item in dircomp.common_dirs:  # 递归子目录
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
            
    return holderlist



 
source_files =compareme("E:\\Python\\Test\\Alpha\\cn\\","E:\\Python\\Test\\RC\\cn\\")
print source_files