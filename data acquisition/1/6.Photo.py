import requests
from lxml import etree

urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(1,3)]
path = 'C://Users/user/Desktop/a/'
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

def get_photo(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    photo_urls = selector.xpath('//p/a[@class="view_img_link"]/@href')
    for photo_url in photo_urls:
        data = requests.get('http:'+photo_url, headers = header)
        fp = open(path+photo_url[-10:],'wb')
        fp.write(data.content)
        fp.close()

for url in urls:
    get_photo(url)
