from urllib.request import urlopen
html = urlopen('https://www.sdut.edu.cn/')
###   html = urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/download/')
print(html.read())
