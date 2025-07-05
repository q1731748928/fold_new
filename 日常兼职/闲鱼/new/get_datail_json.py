import requests


headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://2.taobao.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://2.taobao.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-fetch-storage-access": "active",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "cad7ff1300bdb5eced6ccc26c3574804_1746969723792",
    "_m_h5_tk_enc": "28287c9463bac31250a9d7d20ef3cd95"
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idle.awesome.detail.unit/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": "1746961853037",
    "sign": "0e8714fe00a9c85a6ec8155990941b8d",
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idle.awesome.detail.unit",
    "sessionOption": "AutoLoginOnly",
    "c": "cad7ff1300bdb5eced6ccc26c3574804_1746969723792;28287c9463bac31250a9d7d20ef3cd95"
}
data = {
    "data": "{\"itemId\":\"903384025634\",\"flowVersion\":\"6.0\",\"needSimpleDetail\":false}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)