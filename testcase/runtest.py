# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:25:20 2019

"""

import unittest

#定义测试用例的目录为当前目录
test_dir = 'F:\\coding\\selenium\\'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)