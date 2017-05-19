# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup


def getHtml(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/57.0.2987.98 Chrome/57.0.2987.98 Safari/537.36'}
    url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    res_html = response.read().decode('utf8')
    return res_html


def getItems(page):
    html = getHtml(page)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', {'class': 'article block untagged mb15'})

    for item in items:
        author = item.h2.get_text()
        like = item.i.get_text()
        content = item.span.get_text()
        print '作者:', author + '\n'  + content + '\n', '点赞:', like
        input_enter = str(raw_input())
        if input_enter == '':
            continue
        elif input_enter == 'q':
            break

if __name__ == '__main__':
    num = raw_input('请输入终止页(大于１):')
    page = range(1, int(num))
    for i in page:
        f = getItems(i)
        print f

