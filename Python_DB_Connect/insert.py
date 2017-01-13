#coding:utf8
'''
Created on 2016年9月19日

@author: wolfrg
'''
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("192.168.0.250","root","123456","test" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 插入语句
sqli = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES (%s, %s, %s, %s, %s)"""
try:
   #执行sql语句
   cursor.executemany(sqli,[
                       ('Tom','Monkey','29','M','30000'),
                       ('Sam','Stive','29','M','30000'),
                       
                       ])
   #提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
#关闭数据库连接
db.close()