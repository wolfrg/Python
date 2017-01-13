#coding:utf8
'''
Created on 2016年8月31日

@author: wolfrg
'''

import os,sys,md5
f1 = open('E:\\Python\\Test\\Alpha\\a.txt','r')
f2 = open('E:\\Python\\Test\\RC\\a.txt','r')
print md5.new(f1.read()).digest() == md5.new(f2.read()).digest()



