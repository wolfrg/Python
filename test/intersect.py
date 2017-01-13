#coding:utf8
'''
Created on 2016年8月31日

@author: wolfrg
'''
def intersect(jenkins,alpha):
    res = []
    for content in jenkins:
        if content not in alpha:
            res.append(content)
     
    #print  content
    return content



s1 = open("e:/aa.txt").readlines()  
s2 = open('e:/bb.txt' ).readlines()
#intersect(s1, s2)

f = open('e:/not_in_alpha.txt','w')
f.write(intersect(s1, s2))