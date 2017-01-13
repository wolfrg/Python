#coding:utf8
'''
Created on 2016年12月12日

@author: wolfrg
'''
import os
import shutil

lines = open("E:\\Python\\Test\\Alpha\\system_config.properties").readlines()
f = open("E:\\Python\\Test\\RC\\Alpha_system_config.properties",'w')
f.writelines(lines)
f.close()
                        
#打开文件，读入每一行
lines = open('Alpha_system_config.properties').readlines() 
#打开你要写得文件
fp = open('RC_system_config.properties','w')  
for s in lines:
#replace是替换，write是写入
    fp.write( s.replace('zm.gaiay.net.cn','t.zm.gaiay.cn'))
    print('替换成功')    #测试时开启
fp.close()  # 关闭文件