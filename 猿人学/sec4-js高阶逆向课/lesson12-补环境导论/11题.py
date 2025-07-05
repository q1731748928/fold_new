import re

import execjs
import requests

cookies = {
    'sessionid': 'v5vxp57gehv2vgmckgmh19io2dgpuzk9'
}
session = requests.session()
url = 'https://www.python-spider.com/challenge/11'
response = session.get(url, cookies=cookies)
jscode = re.match('<script>(.*?)</script>', response.text).group(1)


with open('11题.js', 'r', encoding='utf-8') as f:
    result = execjs.compile(f.read().replace("__jscode",jscode)).call('decode')
cookies['__jsl_clearance'] = str(result).split("=")[1].split(";")[0]
response = session.get(url, cookies=cookies)
print(response.text)




