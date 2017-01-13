#coding:utf8
'''
Created on 2016年5月20日

@author: wolfrg
'''
total = 0

def sum(arg1,arg2):
    #返回两个参数的和
    total=arg1+ arg2
    print "函数内局部变量total的值：" ,total
    return total

#调用sum函数
sum(10,20)
print "函数外全局变量total的值仍是：",total