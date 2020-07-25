'''通用爬虫模型'''
import requests

def getHTMLtext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()   #如果状态码不是200，则会引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    url = 'https://www.jd.com'
    print(getHTMLtext(url))
