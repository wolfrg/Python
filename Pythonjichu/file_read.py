#coding:utf8
'''
Created on 2016年6月23日

@author: wolfrg
这是《Python基础教程》 11章文件内容的读取的练习，用read方法迭代每个字符。
'''
f = open(r"c:\aa.txt")
for char in f.read():
    print char,
f.close()    

    