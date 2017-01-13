#coding:utf8

'''
Created on 2017年1月9日

@author: wolfrg
'''

import pysvn

import os,re
'''def  get_login(realm,username,may_save):
    retcode = True
    username='fengruigang'
    password = 'fengruigang'
    save = False
    return retcode,username,password,save'''

svnurl = 'svn://192.168.0.232/remote/zhangmen-frg/Alpha/trunk'
copath = 'E:\\GitSVN\\example5'

client = pysvn.Client()
client.checkout(svnurl,copath)

os.chdir('E:\\GitSVN\\example3')  #切换到svn目录
#client.add('addfile.html')        #添加一个文件到版本库
#client.checkin('.','commit my code') #提交文件到版本库
#changes = client.status('.')
# print changes
#检测状态，获取各种新增、删除、修改、冲突、未版本化的状态
changes = client.status('.')

for f in changes:
    if f.text_status == pysvn.wc_status_kind.added:
        print f.path,'A'
    elif f.text_status == pysvn.wc_status_kind.deleted:
        print f.path,'D'
    elif f.text_status == pysvn.wc_status_kind.modified:
        print f.path,'M'
    elif f.text_status == pysvn.wc_status_kind.conflicted:
        print f.path,'C'
    elif f.text_status == pysvn.wc_status_kind.unversioned:
        print f.path,'U'

