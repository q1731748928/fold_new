import requests


headers = {
    "Host": "www.python-spider.com",
    "accept-language": "zh-CN,zh;q=0.8",
    "user-agent": "Mozilla/5.0 (Linux; U; Android 10; zh-cn; Pixel 4 Build/QQ3A.200805.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1",
    "content-type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache"
}
url = "https://www.python-spider.com/api/app1"
data = {
    "page": "1",
    "sign": "e3ae1fe48fda99b0196c53242f25157b",
    "t": "1737953766773"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)