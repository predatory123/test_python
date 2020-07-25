'''淘宝商品比价爬虫'''
import re
import requests
def geturl(url):
    login_url = 'https://ynuf.aliapp.org/service/um.json'
    kv = {
        'username':'17868806958',
        'password':'wyj810278777'
    }

    rsp = requests.post(login_url,params=kv)


    ck = {
        "cookie":"thw=cn; t=9d5947f271e20655000f64a8f7898b71; enc=T%2FF1xCd5rAIkophLEDRvhXgQ1RBHIfW0FRsKV7W6pRH5p%2FCv0g13bw26fdH8wziEqGs5j%2Bl%2F4726HsYfdIb%2BCQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cna=u3C3FUt0XmECAXruCOt9fnkl; tracknick=demon%5Cu7405%5Cu740A; tg=0; miid=578674071393872803; lgc=demon%5Cu7405%5Cu740A; mt=ci=83_1; cookie2=72f78fd56a95fa1a045236da6ec55715; _tb_token_=ee3e40639bf17; unb=2285810214; uc1=cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&lng=zh_CN&pas=0&tag=8&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie14=UoTaECEiFM6bHA%3D%3D&existShop=false; uc3=id2=UUpprax0mH9cug%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=B0euR33feNix&vt3=F8dByuKxpLggkG3tc30%3D; csg=dabfed25; cookie17=UUpprax0mH9cug%3D%3D; dnk=demon%5Cu7405%5Cu740A; skt=b133535927322a1c; existShop=MTU2ODcyMDAxNA%3D%3D; uc4=id4=0%40U2gjE%2B8nnLxwbsjoyTCx6KwBTpwU&nk4=0%40BQRDlHOSK6q5QC3jAzDqusTNiB0%3D; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%90%8A4f; _nk_=demon%5Cu7405%5Cu740A; cookie1=Bqr4lbbLSepknTuYhYoQ31Bi95npQ0039aNgyfffgSU%3D; _mw_us_time_=1568720015120; l=cBSP0RlHq_5Gu1ViBOCwourza77tsIRAmuPzaNbMi_5Iz6L6AS_OksF-hFp6cjWd9WYB4k6UXwp9-etk2Uw06Pt-g3fP.; isg=BP__g30FnraZ9JoZkA3uNVvPjtNJTCjifcsQ4ZHMnq71oB8imbZI1nyx5jD71Cv-",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    # headers = {
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    # }
    try:
        r = requests.get(url,headers=ck,timeout=30)
        # print(r.text)
        r.raise_for_status()   #获取错误信息
        r.encoding = r.apparent_encoding  #获取编码信息
        return r.text
    except:
        return ""



def getlist(lit,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(',')[1])
            lit.append(price,title)
    except:
        print('')

def getpage(lit):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for q in lit:
        count = count + 1
        print(tplt.format(count,q[0],q[1]))

if __name__ == '__main__':
    value = '羽绒服'
    depath = 2     #爬取的页数
    surl = 'https://s.taobao.com/search?q=' + value
    lit = []

    #获取翻页数据
    for  i in range(depath):
        try:
            url = surl + '&s' + str(44*i)
            html = geturl(url)
            getlist(lit,html)
        except:
            continue
    getpage(lit)

