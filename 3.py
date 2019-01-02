# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:37:39 2018

鼠标事件
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#perform()执行所有ActionChains中的存储行为，可以理解成是对整个操作的提交动作
right_click = driver.find_element_by_id('kw')

ActionChains(driver).move_to_element(right_click).perform()