'''
yuanlin unit09 homework 1
建立可以爬取多篇表特版⽂章的網路圖片下載器
抓取 .txt 裡面ptt網址中的圖片，並將其放入獨立資料夾中
'''
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

def getUrlList(txtfile):
    # 取得網址列表
    f = open(txtfile, 'r')
    result = f.read().splitlines()
    return result

def getHTMLContent(link):
    # 取得網頁內容
    res = requests.get(link, headers = headers)
    return res.content

def getSoup(html):
    # 取得 Soup
    return BeautifulSoup(html, 'html.parser')

def getTitle(soup):
    # 取得文章 title
    tmp = soup.select('span[class^=article-meta-value]')
    title = re.split('<|>', str(tmp[2]))
    return title[2]

def savePhoto(soup, title):
    # 將圖片存檔
    images = soup.select('a[href^=http://i.imgur]')
    if not os.path.exists('./images/{}/'.format(title)):
        # 如果資料夾不在，建立他
        os.makedirs('./images/{}/'.format(title))

    for image in images:
        filename = image['href'].split('/')[3]
        img = urlopen(image['href'])
        with open('./images/{}/{}'.format(title, str(filename)), 'wb') as f:
            f.write(img.read())

tList = getUrlList('url.txt')
for tl in tList:
    hc = getHTMLContent(tl)
    soup = getSoup(hc)
    title = getTitle(soup)
    savePhoto(soup, title)