# -*- coding: utf-8 -*-
from selenium import webdriver
import json
import time
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
options.add_argument('disable-infobars')#隐藏"Chrome正在受到自动软件的控制"

driver = webdriver.Chrome(executable_path=r'G:\chromedriver.exe', chrome_options=options)
driver.get('http://www.dianping.com/')
time.sleep(20)
cookie = driver.get_cookies()
print("COOKIE")
result = {}
for each in cookie:
    result[each['name']] = each['value']
print("RESULT")
print(result)
with open('cookies1.txt','w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(cookie))