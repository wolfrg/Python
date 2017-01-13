#coding:utf8
'''
Created on 2016年5月25日

@author: wolfrg
'''
class People:
    name = 'jack'  #定义类的属性，name和age是公有的，可以直接在类外通过对象名称访问。
    age =12
    
    
p = People()

print "%s's age is %d" % (People.name,p.age)   