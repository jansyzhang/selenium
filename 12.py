# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:20:09 2019

"""

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#设置浏览器窗口的大小
driver.set_window_size(600, 600)

#搜索
driver.find_element_by_id('kw').send_keys("1111")
driver.find_element_by_id('su').click()
sleep(2)

#通过javascript设置浏览器窗口滚动条的位置
js = 'window.scrollTo(100, 450)'
driver.execute_script(js)
sleep(3)
