''''显卡排名爬取'''
import requests
from bs4 import BeautifulSoup
import bs4

def gethtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ''

def getlist(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def plist(ulist,num):
    plt = "{0:<5}\t{1:{3}<20}\t{2:<3}"
    print(plt.format('排名','显卡名称','跑分',chr(12288)))  #槽的用法
    for i in range(num):
        u = ulist[i]
        print(plt.format(u[0],u[1],u[2],chr(12288)))

if __name__ == '__main__':
    ulist = []
    url = 'http://itianti.sinaapp.com/index.php/gpu'
    html = gethtml(url)
    getlist(ulist,html)
    plist(ulist,20)