#coding:utf8
'''
Created on 2016年6月23日

@author: wolfrg
'''

f = open(r"c:\aa.txt")
while True:
    line = f.readline()
    if not line:break
    print line
f.close()