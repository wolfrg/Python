#coding:utf8
'''
Created on 2017年1月11日
@author: wolfrg
脚本功能：批量提交svn文件
实现思路：强制add 新加的文件，首先调用windows下svn命令判断文件的svn状态
参考文档：http://www.bubuko.com/infodetail-1868966.html
'''

import pysvn
import os
import re


os.chdir('E:\\GitSVN\\example4') #切换到svn目录


#强制add没有受版本控制的文件
#把状态为delete的文件重定向到一个txt文件,每次提交完成后清空文件
os.system('svn add --force *')  
a = os.system('svn st -u . | findstr ! > E:\\GitSVN\\notdelete.txt')  

#接下来就是对notdelete.txt文件的操作

#首先读取文件的每一行
lines  = open("E:\\GitSVN\\notdelete.txt","r").readlines()

#使用for循环把替换后的内容写入一个新文件
fp = open("E:\\GitSVN\\delete.txt","w")
for s  in lines:
    fp.write(re.sub('!|\d| ','',s,20))  #把！符号、数字和空格替换掉    
fp.close()    #关闭文件

#第二步操作替换好的文件
deletefiles = open("E:\\GitSVN\\delete.txt","r").readlines()

for d in deletefiles:
    os.system('svn delete %s ' % d)

#提交全部文件        
os.system('svn commit  -m "frg test log"') 
print '文件提交成功'

