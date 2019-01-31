# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:34:11 2019

"""

# 自定义线程类
import threading
from time import sleep, ctime

# 创建线程类
class MyThread(threading.Thread):
    
    def __init__(self, func, args, name=''):
        #threading.Thread.__init__(self)
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
    
    def run(self):
        self.func(*self.args)

def super_player(file_, time):
    for i in range(2):
        print('start playing %s, %s' % (file_, ctime()))
        sleep(time)
        
lists = {'A.mp3': 3, 'B.mp4': 5, 'C.mp4': 4}
threads = []
files = range(len(lists))

for file_, time in lists.items():
    t = MyThread(super_player, (file_, time), super_player.__name__)
    threads.append(t)
    
if __name__ == '__main__':
    # 启动线程
    for t in files:
        threads[t].start()
    
    for t in files:
        threads[t].join()
    
    print('all ends %s' % ctime())