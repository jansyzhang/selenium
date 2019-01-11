# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:05:10 2019

"""

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://videojs.com")

video = driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')
button = driver.find_element_by_xpath('/html/body/section[1]/div[1]/button').click()


#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()", video)

#播放15s
sleep(15)

#暂停视频
print("sleep")
driver.execute_script("arguments[0].pause()", video)
