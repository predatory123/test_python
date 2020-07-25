'''爬取图片'''
import requests
import os

url = 'https://bpic.wotucdn.com/17/53/31/08bOOOPIC08.mp4'
root = "D://photo//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
