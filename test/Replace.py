#coding:utf8
'''
Created on 2016年8月24日

@author: wolfrg
'''
import sys,os,os.path  
def file_replace():  
    path = sys.argv[1]  
    old_data = sys.argv[2]  
    new_data = sys.argv[3]  
    if not os.path.exists(path):  
        print ('file of dir does not exists!\n')
        return  
    elif os.path.isdir(path):     
        for root,dirs,files in os.walk(path):  
            for fn in files:  
                filepath = os.path.join(root,fn)  
                f = open(filepath,'r+')  
                line = f.readlines()  
                f.seek(0)  
                for s in line:  
                    f.write(s.replace(old_data,new_data))  
                f.close()  
    elif os.path.isfile(path):  
        f = open(path,'r+')  
        line = f.readlines()  
        f.seek(0)  
        for s in line:  
            f.write(s.replace(old_data,new_data))  
        f.close()  
    else:  
        print ('argv[1] illegal,not a file or dir\n')
        return  
if __name__=='__main__':  
    file_replace()  