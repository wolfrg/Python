#coding:utf8
'''
Created on 2016年6月1日

@author: wolfrg
'''

class Rectangle:
    def  __init__(self): #定义一个构造方法
          self.width = 0
          self.height = 0
    
    def setSize(self,size): 
        self.width,self.height = size
        
    def getSize(self):      
        return self.width,self.height
     
r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()
r.setSize((20,40))
print r.width