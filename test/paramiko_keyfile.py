#coding:gbk
'''
Created on 2017��3��6��

@author: Ops

֤���¼
'''
import paramiko
hostname = '192.168.0.221'
username = 'tomcat'
mySSHKEY = 'E:\����\��������\����������key�ļ�\\fengruigang_tomcat_20150427'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,username=username,key_filename=mySSHKEY,password='tomcat@fengruigang')

stdin,stdout,stderr=ssh.exec_command('uptime')

for std in stdout.readlines():
    print std,
    
ssh.close() 