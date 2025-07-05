import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.szse.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.szse.cn/lawrules/rule/allrules/bussiness/index.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "X-Request-Type": "ajax",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://www.szse.cn/api/search/content"
params = {
    "random": "0.8689274271936437"
}
data = {
    "keyword": "",
    "time": "0",
    "range": "title",
    "channelCode%5B%5D": "szserulesAllRulesBuss",
    "currentPage": "1",
    "pageSize": "20",
    "scope": "0"
}
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)