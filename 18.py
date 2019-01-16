# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:10:07 2019

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        #定义空的verificationErrors数组，脚本运行时的错误信息将被记录到这个数组中
        self.verificationErrors = [] 
        self.accept_next_alert = True #表示是否继续接受下一个警告，初始状态为True
    
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys("si")
        driver.find_element_by_id("su").click()
    
    #用于查找页面元素是否存在
    def is_element_persent(self, how, what):
        try:
            #通过find_element来接受元素的定位方法（how）和定位值（what）
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    #用于判断当前页面是否存在警告窗
    def is_alert_persent(self, how, what):
        try:
            self.driver.switch_to_alert()
        except NoSuchElementException:
            return False
        return True
    
    #用于关闭警告并获得警告信息
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        
        
        