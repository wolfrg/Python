#coding:utf8
'''
Created on 2016年6月29日

@author: wolfrg
'''
import os
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


d = modification_date('c:/file_mo/123.txt')
size = os.path.getsize('c:/file_mo/123.txt')

print d 
print size
print repr(d)
print str(d)