import requests
import urllib3

ip = "127.0.0.1"
port = 7890

proxies = {
    "http": "http://%s:%d" % (ip, port),
    "https": "http://%s:%d" % (ip, port)
}

urllib3.disable_warnings()
cookies = {
    '__jsl_clearance': '1724295043.597|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_f28b5e55506ab1123951a7789b28ce563D',
    'yrx-13': 'Azvl298q2-83jIPv2M8C9Rc2zBSgkE-SSaQTRi34FzpRjFXKtWDf4ll0o5c-',
    'sessionid': 'x05vti2vu64kzrzimol7g74utm5h5ktz',
    'no-alert': 'true',
    'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1724381259,1724500182,1724501051,1724896456',
    'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1724896456',
    'HMACCOUNT': '788AC10A3780E5E2',
}

headers = {
    'Host': 'www.python-spider.com',
    # 'Cookie': '__jsl_clearance=1724295043.597|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_f28b5e55506ab1123951a7789b28ce563D; yrx-13=Azvl298q2-83jIPv2M8C9Rc2zBSgkE-SSaQTRi34FzpRjFXKtWDf4ll0o5c-; sessionid=x05vti2vu64kzrzimol7g74utm5h5ktz; no-alert=true; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1724381259,1724500182,1724501051,1724896456; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1724896456; HMACCOUNT=788AC10A3780E5E2',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-platform': '"macOS"',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.python-spider.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.python-spider.com/challenge/7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'priority': 'u=1, i',
}
sum = 0
for page in range(1, 101):
    data = {
        'page': page,
    }
    requests.post('https://www.python-spider.com/cityjson', cookies=cookies, headers=headers, proxies=proxies)
    response = requests.post('https://www.python-spider.com/api/challenge7', cookies=cookies, headers=headers, data=data, verify=False,proxies=proxies).json()
    datas = response['data']
    for data in datas:
        value = int(data['value'])
        print(value)
        sum += value
print(sum)
