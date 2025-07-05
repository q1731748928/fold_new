import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "client": "pc-web;pro",
    "pcuss": "eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiand0IiwiYWxnIjoiSFMyNTYifQ.eyJjcmVhdGVUaW1lIjoiMjAyNS0wNC0yOCAyMzowOTo0OS4yOTciLCJleHAiOjE3NDU4NTM4ODksInVzZXJJZCI6IjIwMjUwNDI3MTA1MjUzXzE4OTM5NjYyMTg5IiwiZXhwaXJlZFRpbWUiOiIyMDI1LTA0LTI4IDIzOjI0OjQ5LjI5NyJ9.72GuSWsjWnaqsFSQuobs2i19YXbV9w4wU8AN4kZobuY",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.qyyjt.cn/s?tab=securities&k=%E4%B8%AD%E5%9B%BD%E6%B5%B7%E5%A4%96%E5%B7%A5%E7%A8%8B%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8%E6%AF%9B%E5%A1%94%E5%88%86%E5%85%AC%E5%8F%B8",
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
    "x-request-id": "OpmzHXATyyyvnOZnoi2rs",
    "x-request-url": "%2Fs%3Ftab%3Dsecurities%26k%3D%25E4%25B8%25AD%25E5%259B%25BD%25E6%25B5%25B7%25E5%25A4%2596%25E5%25B7%25A5%25E7%25A8%258B%25E6%259C%2589%25E9%2599%2590%25E8%25B4%25A3%25E4%25BB%25BB%25E5%2585%25AC%25E5%258F%25B8%25E6%25AF%259B%25E5%25A1%2594%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8"
}
url = "https://www.qyyjt.cn/finchinaAPP/v1/finchina-search/v1/multipleSearch"
# 公司code
code = '——'
# 评级
main_rating = '——'
# 全部债权
all_creditors_right = '——'
# 存续债权
continuous_creditors_right = '——'
params = {
        "skip": "0",
        "text": '宝钢工程技术集团有限公司',
        "template": "list"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
