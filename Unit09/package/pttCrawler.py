from bs4 import BeautifulSoup

def getPrePageURL(soup):
    # 取得上一頁的連結
    pages = soup.find('div', {'class': 'btn-group btn-group-paging'})
    return 'https://www.ptt.cc{}'.format(pages.find_all('a')[1].get('href'))