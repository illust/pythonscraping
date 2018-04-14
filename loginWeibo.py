# -*- coding: utf-8 -*-
from selenium import webdriver
import requests

loginUrl = 'http://www.weibo.com/login.php'
    
# 构建浏览器
chromePath = 'D:\Software\Continuum\Anaconda3\chromedriver.exe'
wd = webdriver.Chrome(executable_path=chromePath)
wd.get(loginUrl)
wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('illust0130@foxmail.com')
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('wwhh131134')
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(input("输入验证码： "))
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

req = requests.Session()
cookies = wd.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) # 转换cookies
test = req.get("https://weibo.com/topgirls8?topnav=1&wvr=6&topsug=1")
print(test.content)