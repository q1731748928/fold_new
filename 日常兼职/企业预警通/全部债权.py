import re

import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "client": "pc-web;pro",
    "dataid": "441",
    "pcuss": "eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiand0IiwiYWxnIjoiSFMyNTYifQ.eyJjcmVhdGVUaW1lIjoiMjAyNS0wNC0yOCAyMzo1NTozMS44MTMiLCJleHAiOjE3NDU4NTY2MzEsInVzZXJJZCI6IjIwMjUwNDI3MTA1MjUzXzE4OTM5NjYyMTg5IiwiZXhwaXJlZFRpbWUiOiIyMDI1LTA0LTI5IDAwOjEwOjMxLjgxMyJ9.WgZfGqaNWveQ0zAy4EwpB7Ko7sW3WvYVuwIwC6S5u1k",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.qyyjt.cn/detail/enterprise/corporateFinancing?code=9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27&type=company",
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
    "x-request-id": "vmb0aviENEdK1g3-6TNCK",
    "x-request-url": "%2Fdetail%2Fenterprise%2FcorporateFinancing%3Fcode%3D9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27%26type%3Dcompany%23%25E5%2585%25A8%25E9%2583%25A8%25E5%2580%25BA%25E5%2588%25B8"
}
url = "https://www.qyyjt.cn/getData.action"
params = {
    "code": "9ECA4FB3C4E1AA3A10FC5CFEC7AF0F27",
    "type": "company",
    "skip": "0",
    "isContinuous": "1,2",
    "company_type": "current",
    "module_type": "web_f9_bond_financing",
    "dynamicIndex": "BD0201_046,isPerpetualBond,isGreenLabel,isNotGreenLabel,BD0002_084,BD0002_020,BD0002_016,BD0002_017,BD0002_018,BD0002_012,BD0201_045,BD0051_009,BD0051_004,BD0201_064,BD0201_006,BD0201_042,debtor,guarantor,BD0285_009,BD0285_004,fxlc",
    "branchCompany": "self",
    "_t": "441"
}
response = requests.get(url, headers=headers, params=params)
message = response.json()['data']['message']
print(message)
# (截止最新，债券存量规模0.00亿元，债券17只。)
message = response.json()['data']['message']
pattern = r'\d+\.?\d*[亿|万|元]+'
matches = re.findall(pattern, message)
continuous_creditors_right = matches[0]
