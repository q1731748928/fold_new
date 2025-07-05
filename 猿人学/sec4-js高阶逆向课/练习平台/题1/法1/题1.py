import time

import execjs
import requests

with open("题1.js", encoding="utf-8") as f:
    js_code = f.read()
ctll = execjs.compile(js_code)
params = ctll.call("get_params")

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.python-spider.com/challenge/1",
    "safe": params.get('tokens'),
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "timestamp": params.get('timestamp'),
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1723770763,1724119816",
    "HMACCOUNT": "333AB986E02C62E9",
    "sessionid": "bjvq76ro309ddeptqnek2o7w64mhpvls",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1724122014"
}
url = "https://www.python-spider.com/api/challenge1"
sum = 0
for page in range(1, 101):
    data = {
        "page": str(page)
    }
    js = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    datas = js['data']
    for data in datas:
        value = int(data['value'])
        sum += value
print(sum)