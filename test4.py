'''百度搜素'''
import requests
url = "https://www.baidu.com/s"
try:
    kw = {
        'wd':'比亚迪'
    }
    r = requests.get(url,params=kw)
    ss = r.raise_for_status()
    print(r.request.url)
    print(r.text)
except:
    print('爬取失败')


print('分割线'+'*'*50)
url2 = "https://www.so.com/s"
try:
    kw = {
        'q':'比亚迪'
    }
    r = requests.get(url2,params=kw)
    ss = r.raise_for_status()
    print(r.request.url)
    print(r.text)
except:
    print('爬取失败')
