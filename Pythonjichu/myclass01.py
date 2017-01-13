#coding:utf8
'''
Created on 2016年5月23日

@author: wolfrg
创建一个类,设置和获取名字，并打招呼。
'''
   
class Person:
    
    #定义类方法
    
    def setName(self,name):
        self.name = name 
        
        
    def  getName(self,name):
        self.name = name
    
    def setAge(self,age):
        self.age=age
    
    def getAge(self,age):
        self.age=age    
            
        
    def greet(self):
            print "Hello,world! I'm %s,I am %d years old!" % (self.name,self.age)


t = Person()


t.setName('王二妮')
t.setAge(20)

t.getName("王二妮")
t.getAge(19)


t.greet()

