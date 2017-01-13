#coding:utf8
'''
Created on 2016年8月24日

@author: wolfrg
'''
import os

#跳到E盘
os.chdir('e:\\')   
'''看一下这个文件是否存在'''
if not os.path.exists('Alpha_system_config.properties'):
    '''不存在就退出 '''
    exit(-1)                         
#打开文件，读入每一行
lines = open('Alpha_system_config.properties').readlines() 
#打开你要写得文件
fp = open('RC_system_config.properties','w')  
for s in lines:
#replace是替换，write是写入
    fp.write( s.replace('zm.gaiay.net.cn','t.zm.gaiay.cn'))
    print('替换成功')    #测试时开启
fp.close()  # 关闭文件