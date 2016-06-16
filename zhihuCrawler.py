#!/usr/bin/env python3
# -*- coding: gbk -*-
'''
Required
- requests (����)
- pillow (��ѡ)
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


# ���� Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}

# ʹ�õ�¼cookie��Ϣ
session = requests.session()
session.cookies = LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie δ�ܼ���")


def get_xsrf():
    '''_xsrf ��һ����̬�仯�Ĳ���'''
    index_url = 'http://www.zhihu.com'
    # ��ȡ��¼ʱ��Ҫ�õ���_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # �����_xsrf ���ص���һ��list
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


# ��ȡ��֤��
def get_captcha():
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # ��pillow �� Image ��ʾ��֤��
    # ���û�а�װ pillow ��Դ�������ڵ�Ŀ¼ȥ�ҵ���֤��Ȼ���ֶ�����
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'�뵽 %s Ŀ¼�ҵ�captcha.jpg �ֶ�����' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # ͨ���鿴�û�������Ϣ���ж��Ƿ��Ѿ���¼
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url,allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False



def login(secret, account):
    # ͨ��������û����ж��Ƿ����ֻ���
    if re.match(r"^1\d{10}$", account):
        print("�ֻ��ŵ�¼ \n")
        post_url = 'http://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        print("�����¼ \n")
        post_url = 'http://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # ����Ҫ��֤��ֱ�ӵ�¼�ɹ�
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.text
        print(login_page.status)
        print(login_code)
    except:
        # ��Ҫ������֤�����ܵ�¼�ɹ�
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
        print("֪������: "+name.string) #��ӡ����

        followers = soup.find("a",{"href":"/people/%s/followers"%zhihu_people}).find("strong")
        print("��ע��: "+followers.string+" ��")   #��ӡ��ע����

        gender = soup.find("span",{"class":"gender"}).find("i")
        if len(gender.attrs['class'][1]) > 17:  #�ж��Ա�
            gender = "��"
        else:
            gender = "��"

        img = soup.find("div",{"class":"zm-profile-header-main"}).find("img")
        if 'srcset' in img.attrs:
            urlretrieve(img.attrs['srcset'][:-3],"zhihuDownload\%s.jpg"%name.string)#����ͷ��
            print("%s��ͷ��: "%gender+img.attrs['srcset'][:-3]) #��ӡͷ���ַ
    
        print("=======================================================================")
    except urllib.error.HTTPError as e:
        print(e.code)

def htm2bs(url):
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    return soup

if __name__ == '__main__':
    if isLogin():
        print('֪����½��...')
        print('���Ѿ���¼!')
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
        account = input('����������û���\n>  ')
        secret = input("�������������\n>  ")
        login(secret, account)
