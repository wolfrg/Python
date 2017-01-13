#coding:utf8
'''
Created on 2016年5月20日
递归的练习
@author: wolfrg
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    

print fact(5)    

