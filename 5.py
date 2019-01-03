# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:11:10 2019

"""

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://mail.163.com/")

print('--------------------Before login---------------------')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面的URL
now_url = driver.current_url
print(now_url)

#执行邮箱登录
frame = driver.find_element_by_xpath("//iframe[contains(@id, 'x-URS-iframe')]")
#frame = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
#frame = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")

driver.switch_to.frame(frame)
driver.find_element_by_name('email').send_keys('jansyjm')
driver.find_element_by_name('password').send_keys('zx1995912')
driver.find_element_by_id('dologin').click()
time.sleep(5)

print('--------------------After login---------------------')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面的URL
now_url = driver.current_url
print(now_url)

#获取登录的用户名
user = driver.find_element_by_id('spnUid').text
print(user)
