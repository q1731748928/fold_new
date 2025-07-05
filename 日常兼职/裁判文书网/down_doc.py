import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=b63812ea8f5a9f966a80dabd17d475ba&s21=%E7%9B%97%E7%AA%83&s16=%E5%88%91%E4%BA%8B%E6%A1%88%E7%94%B1&s11=1&s8=02&s9=0201",
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
    "wzws_cid": "d56da33039824ea83fcd047fdec7075ea71c60f0eed639ba7c06c170dd0520730dd8710f481ae879c4612c473bbfefcb76ae485f1843b8291d53aaa48d08e47cd4dc3e4f6582d2b4d85ea87109859b53",
    "wzws_reurl": "L3dlYnNpdGUvY29tbW9uL3BsdWdpbnMvbGF5dWkvbGF5L21vZHVsZXMvbGF5ZGF0ZS5qcw=="
}
url = "https://wenshu.court.gov.cn/down/one"
params = {
    "docId": "8nyfOeIL6L49rG+DyRxnbjAwIhOPYdl/50WtQoWCTC8XFxROocc9jpO3qNaLMqsJbiYbrBEk/we+kAmZ5LrvExw6B8FP7R7bZqbEpWu4A8SbxT7l8BSTsDPbuJ4pL41z"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)