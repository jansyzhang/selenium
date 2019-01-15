# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:26:24 2019

"""
import unittest

#在整个模块开始与结束时被执行
def setUpMoudle(): 
    print("test module start >>>>>>>>>")

def tearDownMoudle():
    print("test module end >>>>>>>>>>")

class Test(unittest.TestCase):
    
    #在整个测试类的开始与结束时被执行
    @classmethod
    def setUpClass(cls):
        print("test class start ===========>")
    
    @classmethod
    def tearDownClass(cls):
        print("test class end ============>")
    
    #在测试用例开始与结束时被执行
    def setUp(self):
        print('test case start -->')
    
    def tearDown(self):
        print('test case end -->')
    
    def test_case(self):
        print("test case 1")
    
    def test_case2(self):
        print("test case 2")

if __name__ == "__main__":
    unittest.main()
