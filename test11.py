'''正则表达式 基本使用方法'''
import re

# 1. re.search()方法，匹配第一个位置, 返回match对象
match = re.search(r'[0-9]\d{5}','PLT 100086,acs123456')
if match:
    print(match.group(0))

# 2. re.match()方法，从开始匹配，返回match对象
match = re.search(r'[0-9]\d{5}','100100 Plt')
if match:
    print(match.group(0))

# 3. re.findall()方法，匹配所有，返回一个列表
match = re.findall(r'[0-9]\d{5}','100100 Plt,adada123456,ac5874585dfd')
print(match)

# 4. re.split()方法，将匹配出的字符串分割， 返回一个列表
match = re.split(r'[0-9]\d{5}','123487aa,Plt000012,adada123456,123456adc',maxsplit=3)
print(match)

#5. re.finditer()方法，返回匹配的迭代类型， 每个迭代类型是match对象
for m in re.finditer(r'[0-9]\d{5}','123487aa ,Plt000012, adada123456 ,123456adc'):
    if m:
        print(m.group(0))

# 6. re.sub()   替换匹配的结果， 返回字符串
match = re.sub(r'[0-9]\d{5}','xxoo','123487aa,Plt000012,adada123456,123456adc',count=2)
print(match)
print(type(match))
