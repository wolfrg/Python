#coding:utf8
'''
Created on 2016年4月14日

@author: wolfrg
'''
import os

import shutil


def deleteFile(dirPath):
    files = os.listdir(dirPath)
    for f in files:
        filePath = os.path.join(dirPath,f)
        print (filePath)
        if os.path.isfile(filePath):
            os.remove(filePath)
        elif os.path.isdir(filePath):
            deleteFile(filePath)
            os.rmdir(filePath)
        print("删除成功")
        
#调用删除函数
#deleteFile("E:\\Temp\\2")

#判断文件类型的函数


#复制的函数
def copyFiles(src, dst):
    
    srcFiles = os.listdir(src)
    filesCopiedNum = 0


                        
    for file in srcFiles:
    
        src_path = os.path.join(src, file) #把路径和路径下的文件连在一起
        dst_path = os.path.join(dst, file)
        
        # 若源路径为文件夹，若存在于目标文件夹，则递归调用本函数；否则先创建再递归。
        if os.path.isdir(src_path):
            #如果目标文件夹不存在就创建文件夹
            if  not os.path.isdir(dst_path):
                os.makedirs(dst_path)              
            filesCopiedNum += copyFiles(src_path, dst_path)
            #print('复制文件夹成功') 在测试的时候开启这条语句

        #新增了源文件，目标文件不存在就去先复制，已经存在的文件就根据时间变化去复制。
        #如果源文件或目录删除了，目标文件和目录还存在，那就删除目标文件和目录。
        elif os.path.isfile(src_path):
            if not os.path.isfile(dst_path):
                shutil.copyfile(src_path, dst_path)
                #print "目标文件复制成功"
            elif os.stat(src_path).st_mtime - os.stat(dst_path).st_mtime >1:
                shutil.copyfile(src_path, dst_path)
                filesCopiedNum += 1
                #print('复制最新文件成功')
               
                

    return filesCopiedNum


#调用函数
#copyFiles("c:/1/","c:/2/")
copyFiles("E:\\Python\\Test\\Alpha\\","E:\\Python\\Test\\RC\\")
#copyFiles("E:\\update-maven\\workspace\\zhangmen-live\\zm-live-service\\target\\zm-live-service-0.0.1\\WEB-INF","E:\\update-work\\zhangmen\\zhangmen-live\\Alpha\\trunk\\WEB-INF")
    