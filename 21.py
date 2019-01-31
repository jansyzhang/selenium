# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:45:50 2019

"""

#多线程
from time import sleep, ctime
import threading

def music(func, loop):
    for i in range(loop):
        print("music %s begins at %s" % (func, ctime()))
        sleep(2)
        
def movie(func, loop):
    for i in range(loop):
        print("movie %s begins at %s" % (func, ctime()))
        sleep(5)

#创建线程数组
threads = []

#创建线程t1，并将t1添加到数组中
t1 = threading.Thread(target=music, args=('A', 2))
threads.append(t1)

#创建线程t2，并将t2添加到数组中
t2 = threading.Thread(target=movie, args=('B', 2))
threads.append(t2)      

if __name__ == '__main__':
    #启动线程
    for t in threads:
        t.start()
    
    #守护线程,等待线程终止
    for t in threads:
        t.join()
    
    print('all ends %s' % ctime())
