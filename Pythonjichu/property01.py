#coding:utf8
'''
Created on 2016年6月2日

@author: wolfrg
property函数的练习
'''
__metaclass__ =type
class  Rectangle:
    def __init__(self):
          self.width = 0
          self.height = 0
          
    def setSize(self,size):
        self.width,self.height=size
        
    def getSize(self):
        return self.width,self.height  
    size = property(getSize,setSize)
    
    
r = Rectangle()
r.width = 20
r.height = 30
print r.size
r.size=150,100 #赋值
print r.width