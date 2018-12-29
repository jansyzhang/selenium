# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:18:13 2018


163邮箱登录
"""

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.163.com/")

'''
163邮箱的源码内含有 iframe 元素，iframe 元素会创建包含另外一个文档的内联框架（即行内框架）。
而webdriver每次只能在一个页面识别，因此需要先定位到相应的frame，再对页面里的元素进行定位。

iframe嵌套需要层层切换
''' 
 
#driver.implicitly_wait(30) #隐式等待30s

#对iframe进行定位，以下都可行。
#frame = driver.find_element_by_xpath("//iframe[contains(@id, 'x-URS-iframe')]")
#frame = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
#frame = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")

driver.switch_to.frame(frame)
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_id('dologin').click()
          
#driver.quit()