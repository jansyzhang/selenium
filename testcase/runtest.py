# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:25:20 2019

"""

import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#定义测试用例的目录为当前目录
test_dir = 'F:\\coding\\selenium\\testcase\\'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":

    #定义报告存放路径
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './' + now +'result.html'
    
    fp = open(filename, 'wb') 
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例情况')
    runner.run(discover)
    fp.close()   