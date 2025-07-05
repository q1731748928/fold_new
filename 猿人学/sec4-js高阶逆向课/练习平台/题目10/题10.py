import requests
import urllib3
ip = "127.0.0.1"
port = 7890

proxies = {
    "http": "http://%s:%d" % (ip, port),
    "https": "http://%s:%d" % (ip, port)
}

urllib3.disable_warnings()

session = requests.Session()



headers = {
        'Content-Length': '6',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Origin': 'https://www.python-spider.com',
        'Referer': 'https://www.python-spider.com/challenge/10',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
sum = 0

for page in range(1, 101):
    data = {
        'page': page,
    }
    cookies = {
        'sessionid': 'x05vti2vu64kzrzimol7g74utm5h5ktz',
    }

    session.headers.clear()
    session.headers.update(headers)
    response = session.post('https://www.python-spider.com/api/challenge10', cookies=cookies, headers=headers, data=data, verify=False,proxies=proxies)
    datas = response.json()['data']
    for data in datas:
        value = int(data['value'])
        print(value)
        sum += value
print(sum)