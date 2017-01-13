#coding:utf8

'''
Created on 2016年4月22日

@author: wolfrg
'''

def story(**kwds):
    return 'Once upon a time, there was a ' '%(job)s  called  %(name)s.' % kwds

def power(x,y,*others):
    if others:
        print 'Received redundant parameters:',others
        
    return pow(x,y)

print power(2, 3,'Hello World!')

print story(job='king',name='Gumby')
params = {'job':'language','name':'Python'}
print story(**params)