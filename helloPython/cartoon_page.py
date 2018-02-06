# -*- coding:utf-8 -*-
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import requests
import re
import MySQLdb
from bs4 import BeautifulSoup

class DMZJ_PAGE:
    def __init__(self):
        self.url = 'http://manhua.dmzj.com/tags/category_search/0-0-0-all-4-0-0-'
        self.afterurl = '.shtml#category_nav_anchor'
        self.db = MySQLdb.connect('localhost','root','','cartoon',charset='utf8')
    
    def getPage(self, sub_url):
        #获取页面
        request = urllib2.Request(sub_url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
    
    def getImageUrls(self):
        sub_url = 'http://manhua.dmzj.com/tags/category_search/0-0-0-all-4-0-0-1.shtml#category_nav_anchor'
#         pattern = re.compile('<div class="leftmiddle_mr">(.*?)</*?</div>', re.S)
#         items = re.findall(pattern, self.getPage(sub_url))
#         print self.getPage(sub_url)
        #print items[0]
        soup = BeautifulSoup(self.getPage(sub_url), 'html.parser')
        #print soup
        #无法直接获取总页数，通过拼接链接，直到出现无效链接为止
        href_before = 'http://manhua.dmzj.com/tags/category_search/0-0-0-all-4-0-0-'
        href_after = '.shtml#category_nav_anchor'
        
        href = 'http://manhua.dmzj.com/tags/category_search/0-0-0-all-4-0-0-321.shtml#category_nav_anchor'
        
        
        index = 1
        r = href_before+str(index)+href_after
        pages = []
        while(requests.get(r).status_code==200):
            print r
            r = href_before+str(index)+href_after
            pages.append(index)
            index = index + 1
        print pages
        
dmzj_page = DMZJ_PAGE()
dmzj_page.getImageUrls()
    
