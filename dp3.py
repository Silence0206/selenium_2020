# -*- coding: utf-8 -*-
from selenium import webdriver
import json
import time

cok = ' ua=17269328027; s_ViewType=10; ctu=4329c5876d2e95d48e474b155baf3eea3f2d10b1dbc334759956c31419481f0c; dper=2c36fa871899cb787641c6d014a5891b6bea491af8a718084b0274bd84f4fdfffc6946156a90863670fa08b7f6248c46aabfaa2647141f63d11e20f4eba7c700fbe75ea743b1cacd4db0b1ff3ad56adb9466f376074031445743b43015b2cd0e; ll=7fd06e815b796be3df069dec7836c3df; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1580099960; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1580099974; dplet=e3deb526ca63c90e1408e002fee156b2; _lxsdk_s=16fe5d31927-914-ba4-9c9%7C%7C25'
def addcookie(Cookie,driver):
    a = Cookie.split(';')
    for key in a:
        m = key.split('=')
        driver.add_cookie({'name':m[0], 'value' : m[1]
            #                   ,  "domain": ".dianping.com", "expires": "", 'path': '/',
            # 'httpOnly': False,
            # 'HostOnly': False
            })
    return

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
options.add_argument('disable-infobars')#隐藏"Chrome正在受到自动软件的控制"
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')

driver = webdriver.Chrome(executable_path=r'G:\chromedriver.exe', chrome_options=options)
driver.get('http://www.dianping.com/')
time.sleep(20)
driver.delete_all_cookies()
driver.add_cookie({
    'value':'15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6',
    'name' : '_lxsdk_cuid'
})
driver.add_cookie({
    'value':'15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6',
    'name' : '_lxsdk'
})
driver.add_cookie({
    'value':'1',
    'name' : 'cy'
})
driver.add_cookie({
    'value':'shanghai',
    'name' : 'cye'
})
driver.add_cookie({
    'value':'5d406e75-d105-f1b3-1737-31a16f94427d.1579866901',
    'name' : '_hc.v'
})
driver.add_cookie({
    'value':'92022daa-6ab6-442c-ba1a-eba0c1ebd56d',
    'name' : '_dp.ac.v'
})
time.sleep(1)
driver.refresh()
