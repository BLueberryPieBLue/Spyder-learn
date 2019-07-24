import urllib.request
from bs4 import BeautifulSoup
import time

def get_info(url):
    req0 = urllib.request.Request(url)
    req0.add_header("User-Agent",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
    html0 = urllib.request.urlopen(req0).read()
    soup0 = BeautifulSoup(html0, 'html.parser')
    titles = soup0.select('#root > main > section > div > div.clearfix > div.detail.layout-main > div.sound-list-wrapper._OO > div.sound-list._OO > ul > li > div.text._OO > a')
    for j in titles:
        print(j.get_text())

if __name__=='__main__':
    urls = ['https://www.ximalaya.com/xiangsheng/2667276/p{}/'.format(str(i)) for i in range(1, 5)]
    for url in urls:
        get_info(url)
        time.sleep(5)







