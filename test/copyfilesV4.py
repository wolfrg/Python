# coding:utf8
'''
Created on 2016年12月13日
#脚本目标：实现差异复制检验源与备份目录差异,经过实践脚本中的替换方法在windows下用replace()方法，linux下用sub()方法
@author: wolfrg
'''
import os
import  filecmp
import re
import shutil


holderlist = []

def compareme(dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only
    diff_in_one = dircomp.diff_files  # 不匹配文件，源目录文件已经发生变化
    #dirpath=os.path.abspath(dir1)   #定义源目录绝对路径
    
    # 将更新文件或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]

    # 判断是否存在相同子目录，以便递归
    if  len(dircomp.common) > 0:
        for item in dircomp.common_dirs:  # 递归子目录
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
    
    
    return holderlist      
def main():
    dir1 = 'E:\\Python\\Test\\Alpha\\cn\\' #33、34这两行是在非交互环境下调试用
    dir2 = 'E:\\Python\\Test\\RC\\cn\\'
#     if len(sys.argv) > 2:
#         dir1 = sys.argv[1]
#         dir2 = sys.argv[2]
#     else:
#         print ("Usage:", sys.argv[0], "datadir backupdir")
#         sys.exit()    
    source_files = compareme(dir1,dir2)
    #取绝对路径后，后面不会自动加上'/'
    dir1 = os.path.abspath(dir1)
     
    if not dir2.endswith('\\'):
        dir2 = dir2 + '\\'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False
     
    
    # 遍历返回的差异文件或目录
    for item in source_files:
        # re.sub用于替换字符串中的匹配项
        destination_dir = item.replace(dir1,dir2) 
        
        destination_files.append(destination_dir)
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True  # 再次调用compareme函数标记
                
                
                
    # 重新调用compareme函数，重新遍历新创建目录的内容        
    if createdir_bool:
        destination_files = []
        source_files = []
        source_files = compareme(dir1, dir2)  # 调用compareme函数
        
        for item in source_files:  # 获取源目录差异路径清单，对应替换成备份目录
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir) 
                      
    print ("update item:")
    print (source_files)  # 输出更新项清单        
    copy_pair = zip(source_files, destination_files)  # 将源目录与备份目录文件清单拆分成元组
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])  #在这里留一个问题，就是复制这步能不能用CopyFiles_v2这个模块
  
                
if __name__ == '__main__':
    main()
                 
               
