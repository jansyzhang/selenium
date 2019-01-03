# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:45:47 2019

"""

'''------------------显示等待-------------------'''
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
element.send_keys("111111111111")'''

'''------------------is_display的方法的使用----------------'''
'''from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Firefox()
driver.get("https://www.baidu.com") 

print(ctime()) 
#需要注意for...else...的使用
for i in range(10):
    try:
        el = driver.find_element_by_id('kw22')               
        if el.is_displayed():
            break
    except: pass
    sleep(1)
else:
    print("time out")
print(ctime())'''

'''------------------隐式等待+sleep---------------------------'''
'''from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime, sleep

driver = webdriver.Firefox()

#设置隐式等待时间10s
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('1111111')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    
sleep(10)
print(ctime())
driver.quit()'''

