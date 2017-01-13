#coding:utf8
import pysvn


svnurl = 'svn://192.168.0.232/remote/zhangmen-frg/Alpha/trunk' #svn地址
copath = 'E:\\GitSVN\\example4'

client = pysvn.Client()
client.checkout(svnurl,copath)