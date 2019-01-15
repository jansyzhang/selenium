# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:59:46 2019

"""

import unittest

class MyTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @unittest.skipIf(3>2, "if condition true, skip")
    def test_skip_if(self):
        print('test bbb')
    
    @unittest.skipUnless(3>2, "if condition true, perform")
    def test_skip_unless(self):
        print('test ccc')
        
    @unittest.expectedFailure
    def test_expected_failure(self):
        unittest.assertEqual(2, 3)

if __name__ == "__main__":
    unittest.main()