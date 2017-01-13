#coding:utf8
'''
Created on 2016年5月25日

@author: wolfrg
'''
class People:
    __name='jack'
    __age=20
    
    
    def getName(self):
        return self.__name        
        
    def getAge(self):  
        return self.__age
    
    
p = People()
print p.getName(),p.getAge()      
        