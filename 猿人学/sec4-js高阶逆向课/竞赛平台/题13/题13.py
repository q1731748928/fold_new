import re

import requests
import urllib3
import subprocess

urllib3.disable_warnings()

ip = "127.0.0.1"
port = 8888

proxies = {
    "http": "http://%s:%d" % (ip, port),
    "https": "http://%s:%d" % (ip, port)
}

headers = {
    "Host": "match.yuanrenxue.cn",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=0, i"
}
cookies = {
    "sessionid": "fpntfydsmceedxyuiurpxibdttb10s9f",
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1724155159,1724899960",
    "HMACCOUNT": "788AC10A3780E5E2",
    "qpfccr": "true",
    "no-alert3": "true",
    "Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3": "1724154433,1724900074",
    "Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3": "1724900074",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1724900087",
    "tk": "-7395334595752961665",
    "yuanrenxue_cookie": "1724901262|rS4W8yIAQFUIzO4fOd0y0OAZs8xZUZMrzOY2YAPK9UiJ3LG6aGk5g3WP4GXvkdMkK1e5f5w1F7jS7wp2D5F8kUIPrd1HMNV2blw5Ot1EUx75BN"
}
url = "https://match.yuanrenxue.cn/match/13"
response = requests.get(url, headers=headers, cookies=cookies, verify=False).text
temps = re.search('<script>(.*)</script>', response).group(1)
js_code = 'document={};location={};' + temps + ';console.log(document.cookie)'
cookies = subprocess.check_output(['node', '-e', js_code])
result = subprocess.check_output(['node', '-e', js_code])
_cookie = re.match('yuanrenxue_cookie=(.*);path=', result.decode()).group(1)
cookies = {
        'yuanrenxue_cookie': _cookie,
    }
cookies['sessionid'] = "fpntfydsmceedxyuiurpxibdttb10s9f"
session =requests.session()
headers = {
    "Host": "match.yuanrenxue.cn",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=0, i"
}
sum = 0
for i in range(1, 6):
        params = {
            'page': i
        }
        response = session.post('https://match.yuanrenxue.com/api/match/13', headers=headers, cookies=cookies, verify=False, proxies=proxies, params=params)
        datas = response.json()['data']
        for data in datas:
            value = int(data['value'])
            print(value)
            sum += value
print(sum)