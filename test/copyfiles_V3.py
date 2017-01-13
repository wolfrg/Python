#coding:utf8
'''
Created on 2016年12月12日
脚本功能：在cmd 命令行下 ，把要更新的项目的Alpha下的sysconfig_properties配置文件以交互的方复制到RC目录下
@author: wolfrg
'''

import sys,os
import difflib

#第一步：把Alpha下的sysconfig配置文件复制到RC下并重命名
lines = open("E:\\Python\\Test\\Alpha\\system_config.properties").readlines()
f = open("E:\\Python\\Test\\RC\\Alpha_system_config.properties",'w')
f.writelines(lines)
f.close()


#第二步：替换域名                       
#打开文件，读入每一行
lines = open('Alpha_system_config.properties').readlines() 
#打开你要写得文件
fp = open('RC_system_config.properties','w')  
for s in lines:
#replace是替换，write是写入
    fp.write( s.replace('zm.gaiay.net.cn','t.zm.gaiay.cn'))
    print('替换成功')    #测试时开启
fp.close()  # 关闭文件

#第三步：把替换后的文件和原来的文件进行对比

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