'''爬虫实例，爬取大学排名'''
import requests
import bs4
from bs4 import BeautifulSoup

#得到网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  #获得异常信息
        r.encoding = r.apparent_encoding  #修改编码
        return r.text
    except:
        return " "

#分析页面数据，返回一个列表
def findUnit(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:  #查找所有的tr标签信息
        if isinstance(tr,bs4.element.Tag):      #检测代码类型
            tds = tr('td')    #   tr('td') = find_oll(tr,'td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
            #tds[3].string  是因为多了一个省市

#打印排名数据
def printUnit(ulist,num):
    tplt = "{0:^5}\t{1:{3}^10}\t{2:^3}"
    print(tplt.format('排名', '学校名称', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

# 运行函数
if __name__ == '__main__':
    uinfo = []
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2018_0.html'

    html = getHTMLText(url)
    findUnit(uinfo, html)
    printUnit(uinfo, 100)

