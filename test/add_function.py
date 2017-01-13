#coding:utf8
'''
Created on 2016年8月30日

@author: wolfrg
'''
def add_function(x,y):
    """
    This is a function that adds x and y
    """
    
    result = x + y
    
    return result

if  __name__=="__main__":
    a= 4
    b = 9
    c = add_function(a, b)
    print "a + b = {0} + {1} = {2}".format(a,b,c) #字符串的format方法
 

  
