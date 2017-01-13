#coding=utf-8
'''
Created on 2016年11月23日

@author: wolfrg
'''

from Tkinter import *
import tkMessageBox
import urllib2
import hashlib
import json


trans_id = '20161123000032562'    #提供百度翻译的APP ID
trans_password = 'yFllN1nG3iZY3ySfjbTw'    #提供密钥
phone_num = '177108256939'    #要求是salt，其实电话号码就行


'''
这段代码目前没发现什么作用
def count(word):
    c = 0
    for c in word:
        c += 1
    return c
'''


def md5hex(word):
    if isinstance(word, unicode):
        word = word.encode("utf-8")
    elif not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def trans(word, fr='en', to='zh'):
    #word_num = count(word)
    sign = md5hex(trans_id + word + phone_num + trans_password)
    api = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q=' + word + '&from=' + 'en' + '&to=' + 'zh' + '&appid=20161123000032562&salt=' + phone_num + '&sign=' + sign
    trans_data = urllib2.urlopen(api).read()
    trans_data = json.loads(trans_data)
    trans_data = trans_data['trans_result'][0]['dst']
    return trans_data


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bd=30)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='翻译', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get()
        result = trans(name)
        tkMessageBox.showinfo('翻译结果', 'Result: %s' % result)

app = Application()
# 设置窗口标题:
app.master.title('Translate')
# 主消息循环:
app.mainloop()