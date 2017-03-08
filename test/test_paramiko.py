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
ssh.connect(hostname='192.168.0.233',port=2222,username='root',password='123456')
stdin,stdout,stderr=ssh.exec_command('ls  -l')

for std in stdout.readlines():
    print std,
    
ssh.close() 
