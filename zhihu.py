#-*- coding:utf-8 -*-


import re
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import requests
import os
import time
import json

import urllib2
import urllib


#获取验证码
def get_captcha(header, session):
	proxies = {
	  "http": "http://140.143.90.197:1080",
	  "https": "http://103.244.252.242:3128",
	}
	# requests.get("http://example.org", proxies=proxies)
	# 验证码URL是按照时间戳的方式命名的
	captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
	response = session.get(captcha_url, headers=header)
	# 保存验证码到当前目录
	with open('captcha.gif', 'wb') as f:
		f.write(response.content)
		f.close()

	# 自动打开刚获取的验证码
	from PIL import Image
	try:
		img = Image.open('captcha.gif')
		img.show()
		img.close()
	except:
		pass

	captcha = {
		'img_size': [200, 44],
		'input_points': [],
	}
	points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20], [129.796875, 22],
			  [150.796875, 22]]
	seq = input('Please enter the position of the inverted word:\n>')
	for i in seq:
		captcha['input_points'].append(points[int(i) - 1])
	print json.dumps(captcha)
	return json.dumps(captcha)

def getContent(url):
	#代理IP
	
	#使用requests.get获取知乎首页的内容
	#r = requests.get(url)
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	#print response.read().decode('utf-8')
	return response.read().decode('utf-8')
	
#获取_xsrf标签的值
def getXSRF(url):
	content = getContent(url)
	#print content
	pattern = re.compile('<input type="hidden" name="_xsrf" value="(.*?)"/>',re.S)
	match = re.findall(pattern, content)
	print match[0]
	xsrf = match[0]
	return xsrf
	
#登录的主方法
def login(baseurl, phone_num, password):

	#设置头信息
	headers_base = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Connection':'keep-alive',
		'Host':'www.zhihu.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	}
	#使用session登录
	session = requests.session()
	login_data = {
		'_xsrf' : getXSRF(baseurl),
		'password' : password,
		'captcha_type' : 'cn',
		'captcha' : get_captcha(headers_base,session),#获取验证码信息
		'phone_num' : phone_num
	}
	
	#登录的url
	baseurl += '/login/phone_num'
	#post请求
	content = session.post(baseurl, headers = headers_base, data = login_data)
	print content
	#再次使用session以get去访问知乎页面，一定要设置verify=False，否则访问失败
	s = session.get("https://www.zhihu.com", headers = headers_base)
	print s.content
	#写到文本中
	
	f = open('zhihu.txt', 'w')
	f.write(s.content.encode('utf-8'))
	
url = 'https://www.zhihu.com'
login(url,'nickname','password')
#getContent(url)

	
	
