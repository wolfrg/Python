#coding:utf8
'''
Created on 2016年12月9日
这个脚本用来对比配置文件的改动
官方文档：http://python.usyiyi.cn/python_278/library/difflib.html
@author: wolfrg
'''
import difflib
import sys


try:
    sysfile1  = sys.argv[1]  #第一个配置文件路径参数
    sysfile2 = sys.argv[2]   #第二个配置文件路径参数
    
except Exception,e:
    print "Error:"+ str(e)
    print "Usage:Compare1 filename1 filename2"
    sys.exit()
  

#文件读取分隔函数
def readfile(filename):
    try:
        fileHandle = open(filename,'rb')
        #print  fileHandle 
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:  
        print ("Read file Error:" +str(error))
        sys.exit()
        
if sysfile1 == "" or sysfile2 == "":
    print "Usage:Compare1.py filename1 filename2"
    sys.exit()
    
    
#调用readfile函数，获取分隔后的字符串
text1_lines = readfile(sysfile1)
text2_lines = readfile(sysfile2)

d  = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)




