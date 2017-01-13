#coding:utf8
'''
Created on 2016年8月23日

@author: wolfrg
'''
import sys
import logging
import time
import watchdog
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self,event):
          if event.is_directory:
              print (event.event_type,event.src_path)
              
          else:
              print (event.event_type,event.src_path)
              
    def on_modified(self,event):
        if not event.is_directory:
            print( event.event_type,event.src_path)

    def on_moved(self,event):
        print ("move",event.src_path,event.dest_path)


if __name__ == "__main__":
  event_handler = MyHandler()
  observer = Observer()
  observer.schedule(event_handler, path='.', recursive=True)
  observer.start()

  try:
    print ("started myWatch")
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()         
              
                
              
         
         
    
