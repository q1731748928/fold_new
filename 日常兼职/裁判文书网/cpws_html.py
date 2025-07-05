import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=bdb5971ecfc54d3bbab294db0f29f594&s21=%E7%9B%97%E7%AA%83&s16=%E5%88%91%E4%BA%8B%E6%A1%88%E7%94%B1&s11=1&s8=02&s9=0201&s6=01",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "wzws_sessionid": "gTViMmJhNIAxMTUuMjA0Ljc2LjIzMaBoRMpQgjZmNjkwMQ==",
    "SESSION": "1bebc4c9-fe29-432f-90bf-d4f5a660b259",
    "wzws_cid": "21216c36b974ae13fae74a59649c1d08ee439dbf1312c606ba23072ac43b8d825cd493987f4bc8aae9a07768b9ee1d900d8b2c0b1d5dbcc9b9c2ce259d79f87f724e58661012d220925b27eafd149c3b"
}
url = "https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html"
params = {
    "pageId": "bdb5971ecfc54d3bbab294db0f29f594",
    "s21": "盗窃",
    "s16": "刑事案由",
    "s11": "1",
    "s8": "02",
    "s9": "0201",
    "s6": "01"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)