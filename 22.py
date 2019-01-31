# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:23:04 2019

"""
from time import sleep, ctime
import threading

# 创建超级播放器
def super_player(file_, time):
    for i in range(2):
        print('start playing %s, %s' % (file_, ctime()))
        sleep(time)

# 播放的文件与播放的时长
lists = {'A.mp3': 3, 'B.mp4': 5, 'C.mp4': 4}

threads = []
files = range(len(lists))

# 创建线程
for file_, time in lists.items():
    t = threading.Thread(target=super_player, args=(file_, time))
    threads.append(t)
    
if __name__ == '__main__':
    # 启动线程
    for t in files:
        threads[t].start()
    
    for t in files:
        threads[t].join()
    
    print('all ends %s' % ctime())