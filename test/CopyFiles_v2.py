#coding:utf8
'''
Created on 2016年10月13日

@author: wolfrg

该脚本的主要功能是针对夸平台，文件操作，复制Jenkins构成生成的文件到一个特定目录。
复制过程忽略java配置文件，单独判断复制web.xml文件。

               
'''
import os
from shutil import ignore_patterns, copystat, copy2, Error

#复制的函数
def copytree(src, dst, ignore=ignore_patterns('*.properties')):
    
    
    names = os.listdir(src)
    
    #得到源目录的文件
    #print src
    #print names
    if ignore is not None:
        ignored_names = ignore(src,names)
        #print ignored_names
    else:
        ignored_names = set()
        #print ignore_names
    errors = []    
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src,name)
        dstname = os.path.join(dst,name)
        try:
            if os.path.isdir(srcname):
                if  not os.path.isdir(dstname):
                    os.makedirs(dstname)
                copytree(srcname, dstname, ignore)
                #print("复制目录成功")
            else:
                if os.path.isfile(srcname):
                    if not os.path.isfile(dstname): 
                            copy2(srcname, dstname)       
                            #print("复制文件成功")
                    elif os.stat(srcname).st_mtime - os.stat(dstname).st_mtime >1: 
                            copy2(srcname, dstname)    
                            #print("复制文件成功")
            if "web.xml" in ignored_names: #web.xml文件要复制
                        copy2("c:/1/web.xml", "d:/2/web.xml")                         
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

    
#调用函数
#copytree("E:/update-maven/workspace/zhangmen-mc/target/zm-mc-0.0.1","E:/update-work/zhangmen/zhangmen-mc/Alpha/trunk", ignore_patterns("*.xml", "*.properties"))
copytree("E:\\update-maven\\workspace\\zhangmen-scheduler\\zm-scheduler-20161208\\target\\libs\\", "E:\\update-work\\zhangmen\\zhangmen-scheduler\\Alpha\\trunk\\libs",ignore_patterns("classes","generated-sources","logs","maven-archiver","maven-status","test-classes","*.properties"))
#copytree("E:\\Python\\Test\\Alpha","E:\\Python\\Test\\RC",ignore_patterns("classes","a","*.properties"))