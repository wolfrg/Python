#coding:utf8
'''
Created on 2016年5月30日

@author: wolfrg
第九章 构造方法继承的练习
'''
__metaclass__ =type
class Bird:
    #这个类定义鸟都具有的一些最基本的功能：吃。
    def __init__(self):
        self.hungry = True
        
    def eat(self):
        if self.hungry:
            print 'Aaaaah....' 
            self.hungry =False
        else:
            print 'No,thanks!'  
            
            

b = Bird()
b.eat()  
b.eat()         

#添加子类SongBird     

class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)  #调用父类的构造函数
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'  #构造方法被重写。
        
    def sing(self):
        print self.sound
        

sb = SongBird()
sb.sing()
sb.eat()
            