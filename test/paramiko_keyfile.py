#coding:gbk
'''
Created on 2017年3月6日

@author: Ops

证书登录
'''
import paramiko
hostname = '192.168.0.221'
username = 'tomcat'
mySSHKEY = 'E:\内网\内网服务\内网服务器key文件\\fengruigang_tomcat_20150427'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,username=username,key_filename=mySSHKEY,password='tomcat@fengruigang')

stdin,stdout,stderr=ssh.exec_command('uptime')

for std in stdout.readlines():
    print std,
    
ssh.close() 