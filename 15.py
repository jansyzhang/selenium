# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:06:11 2019

"""

from calculator import Count
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")

class TestAdd(Mytest):
    
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)
    
    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

class TestSub(Mytest):
    
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)
    
    def test_add2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)
        
        
if __name__ == "__main__":
    unittest.main()

