import requests
import random
import math
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://htgs.ccgp.gov.cn/GS8/contractpublish/search",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "$HMF_CI": "9523cac8184798495287bcb2c640f467cd9809ea4845673beaf01829c633ad626ecbf47173e634a1958da3aff0ada061e344444e5eeaef260c3055c2e1c1b441e7",
    "JSESSIONIDGS8": "M9P8XeGYJUgLuTxC2gtdMIuEIjJfTlCtm4ZsDZqd-5bWAfQ8hmHA\\u0021-64666437",
    "cookieinsert": "20111186"
}
url = "http://htgs.ccgp.gov.cn/GS8/genCodeImg"
random_float = random.random()
# 输出生成的随机浮点数
print(random_float)
params = {
    "t": str(random_float)
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

print(response.text)
print(response)
# msg = response.json()['msg']
# # msg = "25e8fcda0ae9dafd81a0093483425212"
# contextPath = "http://htgs.ccgp.gov.cn/GS8/"
# img_url = contextPath + "/upload/verifyCodes/" + msg + ".jpg"
# print(img_url)