#coding:utf8
'''
Created on 2016年12月19日
  练习发送邮件的脚本
@author: wolfrg
'''
import smtplib
import string

HOST = "smtp.ym.163.com"
SUBJECT = "Test email from Python" #定义邮件主题
TO = ['fengruigang2011@163.com','1019127992@qq.com'] #给多人发邮件，收件人地址是List型
FROM = "fengruigang@gaiay.cn"
text = "这是我的第一个Python脚本的邮件 Python rules them all!" #邮件内容
BODY = string.join((
       "From: %s" % FROM,
       "TO: %s" % TO,
       "Subject: %s" % SUBJECT,
       "",
       text             
       ),"\r\n" )


server = smtplib.SMTP()
server.connect(HOST,25)
server.starttls()
server.login("fengruigang@gaiay.cn", "frg198791")
server.sendmail(FROM,TO,BODY)
server.quit()