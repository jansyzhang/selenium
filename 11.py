# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:05:35 2019

@author: zhangxin
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#获取cookie信息
'''cookie = driver.get_cookies()
print(cookie)'''

#向cookie的name和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaa', 'value': 'bbbbbb'})

#遍历cookie中的name和value信息并打印
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))