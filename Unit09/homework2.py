'''
進階：計算八卦版⽂章作者發⽂的數量和標題長度
'''
import requests
from bs4 import BeautifulSoup
from package import pttCrawler

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

postData = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

rs = requests.session()
rs.post('https://www.ptt.cc/ask/over18', headers = headers, data=postData) # 處理八卦板確認年齡的頁面

prePage = ''
for i in range(0, 5):
    print(str(i) + prePage + "------------------------------------------------")
    if i == 0:
        res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers = headers)
    else:
        res = rs.get(prePage, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    post = soup.select('.r-ent')
    for p in post:
        if '(本文已被刪除)' not in p.select('.title')[0].text:
            print(p.select('.title')[0].text + "-" + p.select('.author')[0].text)
    prePage = pttCrawler.getPrePageURL(soup)
        
