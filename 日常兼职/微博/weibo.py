import requests

"""
爬虫2024年6月，2024年11月这两段时间内，带“姜萍”这个关键词，点赞量超过100的原创微博，直接按时间倒序抓取，不用逐日抓取。
"""
headers = {
    "Host": "s.weibo.com",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://weibo.com/",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=0, i"
}
cookies = {
    "SCF": "Apw15g4T9uVfNmb50Y5895gwM6AKkrgoBSXYWd5sHLkdWCxftxRU2OZdEp2UPxQt6peBxYhLapkxHf7QbkjPc-s.",
    "PC_TOKEN": "bed4013cc9",
    "SUB": "_2A25K_Av0DeRhGeNJ6lAY8CnEwj6IHXVmcAE8rDV8PUNbmtAbLVXnkW9NS-OJLVKKQmz8LhvHJWFT9A7taAp8r_4r",
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh08cDwohrgHn_R4p.nIJZU5JpX5KzhUgL.Fo-NeKz4ehMR1Kz2dJLoI7LyUPxDMcfy9Pet",
    "ALF": "02_1746929829",
    "SINAGLOBAL": "8112002628457.431.1744337854928",
    "ULV": "1744337854936:1:1:1:8112002628457.431.1744337854928:"
}
url = "https://s.weibo.com/weibo"
params = {
    "q": "姜萍",
    "page": 2
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

print(response.text)
print(response)