# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:05:58 2019

@author: zhangxin
"""

'''from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id('kw').send_keys("ssss")
driver.find_element_by_id('su').click()

#截取当前窗口，并制定截图保存的位置
driver.get_screenshot_as_file("D:\\baidu_img.jpg")'''

from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("ssssss")
driver.find_element_by_id("su").click()
print(logging.basicConfig(level=logging.DEBUG))