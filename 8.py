# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:00:49 2019

多窗口进行切换
"""

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#获得百度搜索窗口的句柄
search_windows = driver.current_window_handle
print(search_windows)
print("------------------------------------------------")

driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.find_element_by_link_text('立即注册').click()
time.sleep(2)
#获得当前所有打开窗口的句柄
all_handles = driver.window_handles
print(all_handles)

time.sleep(5)
#进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now register window')
        #username
        driver.find_element_by_name('userName').send_keys('username')

        
time.sleep(10)
#回到搜索窗口
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window')
        #TANGRAM__PSP_4__closeBtn
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        driver.find_element_by_id('kw').send_keys('ddddd')
        driver.find_element_by_id('su').click()
