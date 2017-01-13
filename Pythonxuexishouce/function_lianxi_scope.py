#coding:utf8
'''
Created on 2016年9月2日

@author: wolfrg

这个例子说明：在函数内部为参数赋新值不会改变外部任何变量的值
'''
X = 99

def f1():
    Y=88
    def f2():
        print(Y)
    f2()
    
f1()  
#print Y
print X      