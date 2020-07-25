'''京东商品比价'''
import requests
import re

login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.754894437.3.5af911d9FgWFWk%26ad_id%3D%26am_id%3D%26cm_id%3D%26pm_id%3D1501036000a02c5c3739'
kv = {

}

rsp = requests.post(login_url, params=kv)
print(rsp.text)