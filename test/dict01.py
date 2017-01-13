#coding:utf8
'''
Created on 2016年4月21日

@author: wolfrg
'''
'''people = {
          'Alice':{
                   'phone':'1234',
                   'addr':'和平里7号'
                   },
          'Beth':{
                  'phone':'5678',
                  'addr':'翠屏北里26号'
                  },
          'Cixi':{
                  'phone':'98765',
                  'addr':'Foo drive 23'
                  }
          }

labels = {
          'phone':'phone number',
          'addr':'address'
          }

name = raw_input('Name: ')
request = raw_input('Phone number (p) or address (a)?')

if request == 'p':
    key = 'phone'
else:
    print '没有找到您要的电话号码'
    
if request == 'a':
    key = 'addr'
else:
    print '没有找到您要的地址！'
        


if name in people:
    print "%s's %s is %s." % (name,labels[key],people[name][key])
    
else:
    print '没有你要找的这个人'
    
    
'''
    
    
    
d = {'a':1,'b':2,'c':3}
for k in d:
    print k,'to',d[k]   
    
    
    