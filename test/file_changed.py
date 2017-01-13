#coding:utf8 必须放第一行
'''
本代码旨在练习操作目录下文件和文件夹的变化
'''
import os
import filecmp
'''
#第一步：Check if a path exists:

if os.path.exists("C:\\file_mo"):
    print "Yes - found it"
    
#把目录下的文件和子目录列出来，只能列出一层的子目录
if os.listdir("C:\\file_mo"):
    src_dir = os.listdir("C:\\file_mo")
    print src_dir
    
#第二步：Check if a path is a file
if os.path.isfile("C:\\file_mo\\123.txt"):
    print "That is a file alright"   
    
'''   
#第三步：更进一步，定义一个函数遍历目录下的文件包括子目录下的文件

def listfiles(src):
    src_files = os.listdir(src)
    filesNum = 0
     
    for file in src_files:
       src_path = os.path.join(src,file)
       if os.path.isdir(src_path):
            filesNum += listfiles(src_path)
            print ('目录：%s' % src_path) #也可以是其他操作
            
          
        
       elif os.path.isfile(src_path):
           filesNum += 1
           print ('目录下的文件:%s ' % src_path)
        
        
    return  filesNum

listfiles("C:\\file_mo")   

#filecmp.cmp("C:\\file_mo", "D:\\file_mo")          

