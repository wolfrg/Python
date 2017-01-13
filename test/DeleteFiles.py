#coding:utf8
'''
Created on 2016年12月1日
这个脚本是用来解决目前工作中Jenkins+maven+私服不能自动删除文件而创建的
@author: wolfrg
'''
import os

#创建函数
def deleteFiles(dirpath):
    
    files = os.listdir(dirpath)
    #print files
    for f in files:
        
 
 
 
 
#调用函数
deleteFiles("E:\\Python\\Test\\a")   