#!/usr/bin/env python3
# -*- coding: gbk -*-
'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
'''
import requests
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from http.cookiejar import LWPCookieJar
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'http://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


# 获取验证码
def get_captcha():
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url,allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False



def login(secret, account):
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'http://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        print("邮箱登录 \n")
        post_url = 'http://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.text
        print(login_page.status)
        print(login_code)
    except:
        # 需要输入验证码后才能登录成功
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = eval(login_page.text)
        print(login_code['msg'])
    session.cookies.save()


"""
try:
    input = raw_input
except:
    pass
"""
def getInfo(url):
    soup = htm2bs(url)
    zhihu_people = url[29:]
    
    '''
    errStatus = soup.find_all("div",{"class":"zh-profile-account-status"})
    if errStatus is not None:
        return None
    print(errStatus)
    '''
    try:
        name = soup.find("div",{"class":"title-section ellipsis"}).find("span")
        print("知友姓名: "+name.string) #打印姓名

        followers = soup.find("a",{"href":"/people/%s/followers"%zhihu_people}).find("strong")
        print("关注者: "+followers.string+" 人")   #打印关注人数

        gender = soup.find("span",{"class":"gender"}).find("i")
        if len(gender.attrs['class'][1]) > 17:  #判断性别
            gender = "她"
        else:
            gender = "他"

        img = soup.find("div",{"class":"zm-profile-header-main"}).find("img")
        if 'srcset' in img.attrs:
            urlretrieve(img.attrs['srcset'][:-3],"zhihuDownload\%s.jpg"%name.string)#下载头像
            print("%s的头像: "%gender+img.attrs['srcset'][:-3]) #打印头像地址
    
        print("=======================================================================")
    except urllib.error.HTTPError as e:
        print(e.code)

def htm2bs(url):
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    return soup

if __name__ == '__main__':
    if isLogin():
        print('知乎登陆中...')
        print('您已经登录!')
        print("=======================================================================")
        url = "https://www.zhihu.com/topic/19684455/top-answers"
        people = set()
        questions = set()
        soup = htm2bs(url)
        links = soup.find_all("a",{"class":"question_link"})
        for link in links:
            questions.add(link.attrs['href'][10:])
    
        for question in questions:
            soup = htm2bs("https://www.zhihu.com/question/" + question)
            authors = soup.find_all("a",{"class":"author-link"})
            for author in authors:
                people.add(author.attrs['href'][8:])
        people.remove('Ace1987')
        people.remove('yang-xiao-91-41')
        print(people)
    
        for item in people:
            url = "https://www.zhihu.com/people/" + item
            getInfo(url)
    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)
