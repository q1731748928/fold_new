import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "client": "pc-web;pro",
    "dataid": "434",
    "pcuss": "eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiand0IiwiYWxnIjoiSFMyNTYifQ.eyJjcmVhdGVUaW1lIjoiMjAyNS0wNC0yOCAyMTowNzo0My4xNDUiLCJleHAiOjE3NDU4NDY1NjMsInVzZXJJZCI6IjIwMjUwNDI3MTA1MjUzXzE4OTM5NjYyMTg5IiwiZXhwaXJlZFRpbWUiOiIyMDI1LTA0LTI4IDIxOjIyOjQzLjE0NSJ9.5WbudxhHeR4qnjSBtjzLm2eb_Oft4NmRUHRnRF-zPOk",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.qyyjt.cn/detail/enterprise/overview?code=9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27&type=company",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "system": "new",
    "system1": "Macintosh; Intel Mac OS X 10_15_7;Chrome;135.0.0.0",
    "terminal": "pc-web;pro",
    "user": "BFF37120F39EF5801824287C4E4D754F30399020310E152F8C10EE812CB1BCCB",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "ver": "20250424",
    "x-request-id": "sHn0kDuWTtih39ZR8Wz8K",
    "x-request-url": "%2Fdetail%2Fenterprise%2Foverview%3Fcode%3D9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27%26type%3Dcompany"
}
url = "https://www.qyyjt.cn/getData.action"
params = {
    "type": "company",
    "code": "9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27",
    "isContinuous": "1",
    "_t": "434"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)