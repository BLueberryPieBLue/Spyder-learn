import urllib.request
from bs4 import BeautifulSoup

url0 = "http://www.sdut.edu.cn"
req0 = urllib.request.Request(url0)
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
html0 = urllib.request.urlopen(req0).read()
soup0 = BeautifulSoup(html0, 'html.parser')
news = soup0.select('#wp_news_w8 > ul > li > a')
for i in news:
    print(i.get_text())


