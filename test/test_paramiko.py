#coding:gbk
'''
Created on 

@author: Ops
SSH 账号密码登录的方式
'''
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='118.186.17.174',port=10001,username='root',password='frgadmin')
stdin,stdout,stderr=ssh.exec_command('ls  -l')

for std in stdout.readlines():
    print std,
    
ssh.close() 
