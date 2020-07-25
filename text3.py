'''亚马逊商品详情'''
import requests
url = 'https://www.amazon.cn/dp/B07QN3683G/ref=sr_1_1?keywords=%E6%B8%B8%E6%88%8F%7Cgaming&pf_rd_i=42689071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_p=cdcd9a0d-d7cf-4dab-80db-2b7d63266973&pf_rd_r=85DYRTBY3TSFZNKX4PM2&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1567425787&s=pc&sr=1-1'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')