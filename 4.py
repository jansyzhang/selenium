# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:46:30 2019

键盘事件
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格+教程
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

#ctrl+a全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

#ctrl+x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

#ctrl+v粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

#通过回车来代替单击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)