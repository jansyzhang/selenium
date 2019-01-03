# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:12:33 2019

"""

from selenium import webdriver
import os, time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

'''----------------定位页面中的一组元素 1------------------'''
#选择页面上所有tag name为input的元素
'''inputs = driver.find_element_by_tag_name('input')

#然后从中过滤出type为checkbox的元素，单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox': #判断过程
        i.click()
        time.sleep(1)

driver.quit()'''

'''-----------------定位页面中的一组元素 2------------------'''
#通过XPath找到type=checkbox的元素
#checkboxs = driver.find_element_by_xpath("//input[@type='checkbox']")

#通过CSS找到type=checkbox的元素
checkboxs = driver.find_element_by_css_selector('input[type=checkbox]')

for checkbox in checkboxs:
    checkbox.click()
    time.sleep(1)

#把页面上最后一个checkbox的钩给去掉
driver.find_element_by_css_selector('input[type=checkbox]').pop().click()
