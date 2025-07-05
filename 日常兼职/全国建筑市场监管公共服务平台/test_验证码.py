import json
import time

import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/data/project/detail?id=3148",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLVMl/7XMw9Fwvvq70ITkDFghpUUKvcMtoMqfGfwdLCb8g==",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "timeout": "30000",
    "v": "231012"
}
url = "https://jzsc.mohurd.gov.cn/APi/webApi/geetest/startCaptcha"
response = requests.get(url, headers=headers)
# print(response.text)
res = execjs.compile(open('03-aes案例.js', encoding='utf-8').read())
result = res.call('b', response.text)
js = json.loads(result)
# print(js)
challenge = js['data']['challenge']
gt = js['data']['gt']
params = {
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "pt": "0",
    "client_type": "web",
    "w": "",
    "callback": "geetest_" + str(int(time.time() * 1000))
}
print(requests.get('https://api.geevisit.com/ajax.php', params=params, headers=headers).text)
params = {
    "is_next": "true",
    "type": "click",
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "https": "true",
    "protocol": "https://",
    "offline": "false",
    "product": "float",
    "api_server": "api.geevisit.com",
    "isPC": "true",
    "autoReset": "true",
    "width": "100%",
}
two_url = 'https://api.geevisit.com/get.php'
response = requests.get(two_url, headers=headers, params=params)
pic = json.loads(response.text[1:-1])['data']['pic']
s = json.loads(response.text[1:-1])['data']['s']
c = json.loads(response.text[1:-1])['data']['c']
