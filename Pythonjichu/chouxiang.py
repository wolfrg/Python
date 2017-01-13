#coding:utf8
'''
Created on 2016年4月22日
《Python基础教程》 第六章 抽象  关于参数的练习
@author: wolfrg
'''


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)  
#print storage
  
def lookup(data,label,name):
    return data[label].get(name)


def store(data,full_name):
    names = full_name.split()
    print 'names list: ',names
    if len(names) == 2:
        names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data, label, name) 
        if people:
            people.append(full_name)
            
        else:
            data[label][name] = [full_name]
            

         
MyNames={}
init(MyNames)
store(MyNames, 'Lie  Hetland')
print lookup(MyNames,'middle','Lie') 

     
