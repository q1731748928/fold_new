import execjs
import requests

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.python-spider.com/challenge/55",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "zarj9rsg6gc4p0njnoh9ea3w1pvv5h8z"
}
url = "https://www.python-spider.com/api/challenge55"

sum = 0
for page in range(1, 101):
    data = {
        "page": page
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    ctll = execjs.compile(open('题55.js', encoding='utf-8').read())
    datas = ctll.call('decode', response)
    for data in datas:
        value = int(data['value'])
        # print(value)
        sum += value
print(sum)
