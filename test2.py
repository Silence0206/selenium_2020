# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import random
import json

Cookie='_lxsdk_cuid=15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6; ' \
         '_lxsdk=15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6; ' \
         'cy=1; ' \
       'cye=shanghai;' \
         ' _hc.v=5d406e75-d105-f1b3-1737-31a16f94427d.1579866901; ' \
         ' _hc.v=5d406e75-d105-f1b3-1737-31a16f94427d.1579866901; ' \
         '_dp.ac.v=92022daa-6ab6-442c-ba1a-eba0c1ebd56d; ua=17269328027; ' \
         's_ViewType=10; ' \
         'ctu=4329c5876d2e95d48e474b155baf3eea3f2d10b1dbc334759956c31419481f0c;' \
         ' dper=2c36fa871899cb787641c6d014a5891b6bea491af8a718084b0274bd84f4fdfffc6946156a90863670fa08b7f6248c46aabfaa2647141f63d11e20f4eba7c700fbe75ea743b1cacd4db0b1ff3ad56adb9466f376074031445743b43015b2cd0e; ' \
         'll=7fd06e815b796be3df069dec7836c3df; ' \
         'dplet=9acca81eff65d09f1e3a1dd8d45dcbc9; ' \
         'aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1580099960;' \
         ' _lxsdk_s=16fe54a188d-887-b24-884%7C%7C30; ' \
            'name=dpdecookie; ' \
         'Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1580099974'
Cookie = '_lxsdk_cuid=15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6; _lxsdk=15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6; cy=1; cye=shanghai; _hc.v=5d406e75-d105-f1b3-1737-31a16f94427d.1579866901; _dp.ac.v=92022daa-6ab6-442c-ba1a-eba0c1ebd56d; ua=17269328027; s_ViewType=10; ctu=4329c5876d2e95d48e474b155baf3eea3f2d10b1dbc334759956c31419481f0c; dper=2c36fa871899cb787641c6d014a5891b6bea491af8a718084b0274bd84f4fdfffc6946156a90863670fa08b7f6248c46aabfaa2647141f63d11e20f4eba7c700fbe75ea743b1cacd4db0b1ff3ad56adb9466f376074031445743b43015b2cd0e; ll=7fd06e815b796be3df069dec7836c3df; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1580099960; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1580099974; dplet=e3deb526ca63c90e1408e002fee156b2; _lxsdk_s=16fe5d31927-914-ba4-9c9%7C%7C25'

def addcookie(Cookie,driver):
    a = Cookie.split(';')
    for key in a:
        try:
            m = key.split('=')

            driver.add_cookie({'name':m[0], 'value' : m[1]})
        except BaseException as e:
            print({'name': m[0], 'value': m[1]})
            print(m[0], "打开出错休息5秒 错误原因：", e)
    return
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')
# options.add_argument('--headless')
options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示

wd = webdriver.Chrome(r'G:\chromedriver.exe',chrome_options=options)
wd.get('http://www.dianping.com/shanghai/ch70/g193r3')
wd.delete_all_cookies()
wd.add_cookie({
    'value':'15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6',
    'name' : '_lxsdk_cuid'
})
#这样不行
# wd.add_cookie({'value': '15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6', 'name': ' _lxsdk'})
#这样行
wd.add_cookie({
    'value':'15d81de7047c8-0d940d74f92cb3-b373f68-100200-15d81de7047c6',
    'name' : '_lxsdk'
})

a = Cookie.split(';')
for key in a:
    try:
        m = key.split('=')
        # 这样不行
        wd.add_cookie({
            'value': m[1],
            'name': m[0]
        })
    except BaseException as e:
        print({'name': m[0], 'value': m[1]})
        print(m[0], "打开出错休息5秒 错误原因：", e)
# time.sleep(3)
# wd.refresh()
# time.sleep(random.uniform(20, 30))
# cookie = wd.get_cookies()
# result = {}
# for each in cookie:
#     result[each['name']] = each['value']
# print(result)
# with open('cookies22.txt','w') as cookief:
#     #将cookies保存为json格式
#     cookief.write(json.dumps(cookie))
