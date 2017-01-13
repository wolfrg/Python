#coding:utf8

'''
脚本目的：监控配置文件的变化，提取变化的内容。
本脚实现方式:

'''
import difflib
 
a = open('E:\\Python\\Test\\Alpha\\a.txt', 'U').readlines()
b = open('E:\\Python\\Test\\Alpha\\b.txt', 'U').readlines()


#print a #打印出的是一个列表
text_a_lines = a.splitlines()
text_b_lines = b.splitlines()

diff = difflib.ndiff(text_a_lines, text_b_lines)

#sys.stdout.writelines(diff)
diff = filter(lambda x: x.startswith('+ ') or x.startswith('- '), diff) #过滤出以 '+ '、'- '开头的行
with open('e:/diff.html','w') as f:
    f.write('\n'.join(diff))



