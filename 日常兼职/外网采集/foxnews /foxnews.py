import json

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.foxnews.com/category/world/conflicts/ukraine",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-arch": "\"arm\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-ch-ua-platform-version": "\"14.4.1\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
for i in range(1, 5):
    url = "https://www.foxnews.com/api/article-search"
    params = {
        "searchBy": "tags",
        "values": "fox-news/world/conflicts/ukraine",
        "excludeBy": "tags",
        "excludeValues": "",
        "size": "11",
        "from": str((i - 1) * 10),
        "mediaTags": "world|conflicts|ukraine"
    }
    js = requests.get(url, headers=headers, params=params).json()
    if js == []:
        break
    for j in js:
        title = j.get('title')
        category = j.get('category')
        url = j.get('url')
        if not any(x in url for x in ["/video/", "/media/"]):
            url = 'https://www.foxnews.com' + url
            print(url)
    # # print(title, category, url)
    #     with open('./foxnew.txt','a+') as f:
    #         f.write(str(title) + "：" + str(category) + "：" + str(url))
    #         f.write('\n')

