# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:56:51 2019

"""

from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("22222")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "22222_百度搜索")
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()        