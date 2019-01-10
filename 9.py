# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:55:10 2019

"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

#鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

#接收警告框
#driver.switch_to_alert().accept()
#driver.switch_to.alert.accept()

