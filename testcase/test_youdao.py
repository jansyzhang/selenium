# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:14:35 2019

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.youdao.com"
    
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("span")
        driver.find_element_by_id("translateContent").send_keys(Keys.ENTER)
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "span - 有道搜索")
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()