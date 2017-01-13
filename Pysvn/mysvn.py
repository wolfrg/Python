#coding:utf8
'''
参考文档http://chenxiaoyu.org/2009/11/20/pysvn-tutorial.html
Created on 2017年1月5日
pysvn是什么，干什么的，它的原理是什么
@author: wolfrg
'''




'''
这三行在交互方式下执行没有问题
client = pysvn.Client()
check out the current version of the pysvn project
client.checkout('svn://192.168.0.232/remote/zhangmen-frg/Alpha/trunk','E:\\GitSVN\\example')'''


#创建一个client，用于登陆svn

import pysvn
'''
def  get_login(realm,username,may_save):
    retcode = True
    username='fengruigang'
    password = '123456'
    save = False
    return retcode,username,password,save
'''
client = pysvn.Client()
#client.callback_get_login = get_login


#在这个client下进行各种操作

svnurl = 'svn://192.168.0.232/remote/zhangmen-frg/Alpha/trunk'     #部署svn路径
copath = 'E:\\GitSVN\\example'  #svn check out 路径

client.checkout(svnurl,copath)