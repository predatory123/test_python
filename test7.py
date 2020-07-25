'''BeautifulSoup的使用'''
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
try:
    r = requests.get(url)
    rsp = r.text
    soup = BeautifulSoup(rsp,'html.parser')
    print(soup.prettify())
except:
    print('爬取失败')