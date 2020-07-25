'''BeautifulSoup基本元素'''
import requests
from bs4 import BeautifulSoup

url = 'https://item.jd.com/100005518110.html'
r = requests.get(url)
rsp = r.text
soup = BeautifulSoup(rsp,'lxml')
# print(soup.prettify())

for rs in soup.find_all('a'):
    print(rs.get('href'))


# tag = soup.<img>
# print(tag.string)
# ss = soup.find(class='itemInfo-wrap')
# # print(soup.prettify())
# tag = soup.img
# print(tag.string)
# # print(soup.div[class='sku-name'])
#
# print(soup.a)
#
# tag = soup.p
# print(tag)
# # print(tag.attrs['target'])
# print(tag.string)
#
