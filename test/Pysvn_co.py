#coding:utf8
'''
Created on 2016年4月15日

@author: wolfrg

import pysvn
client = pysvn.Client()
status = pysvn.PysvnStatus()
#Check out a working copy

client.checkout('svn://192.168.0.232/remote/zhangmen-ma/Alpha/trunk','C:\\Users\\wolfrg\\Desktop\\trunk')

#判读文件状态
changes = client.status('C:\\Users\\wolfrg\\Desktop\\trunk')








#Add a file or dir to the repository

#f = file('C:\\Users\\wolfrg\\Desktop\\trunk\\','w')

'''
import pysvn
import datetime



client = pysvn.Client()

'''
pysvn.Client.info
    entry  = info( path )
    
    
'''

entry = client.info('C:\\Users\\wolfrg\\Desktop\\trunk')
out = client.status('C:\\Users\\wolfrg\\Desktop\\trunk\\')[1].text_status
file_status = 'unversioned'
status_list  = client.status ('C:\\Users\\wolfrg\\Desktop\\trunk')
print u'SVN路径:',entry.url
print u'最新版本:',entry.commit_revision.number
print u'提交人员:',entry.commit_author
print u'更新日期:', datetime.datetime.fromtimestamp(entry.commit_time)


'''
这里的思路是，用一个for循环遍历svn目录下的文件，然后获取文件状态，如果文件状态发生变化，就条件相应的文件
'''


    

print out

