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
    "_m_h5_tk": "67d4c5674d9fd8a9dcbb977224da25b3_1746879053461",
    "_m_h5_tk_enc": "5f4d8ae2092b66357043cbc89276ed79"
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.wx.search.shade/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": "1746873901902",
    "sign": "1",
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlemtopsearch.wx.search.shade",
    "sessionOption": "AutoLoginOnly",
    "c": "67d4c5674d9fd8a9dcbb977224da25b3_1746879053461;5f4d8ae2092b66357043cbc89276ed79"
}
data = {
    "data": "{\"searchReqFromPage\":\"xyMiniHome\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

RequestsCookieJar = response.cookies
_m_h5_tk = RequestsCookieJar.get('_m_h5_tk')
_m_h5_tk_enc = RequestsCookieJar.get('_m_h5_tk_enc')
print(_m_h5_tk, _m_h5_tk_enc)