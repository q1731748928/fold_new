import requests
import base64

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.python-spider.com/challenge/54",
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
    "__jsl_clearance": "1724295043.597|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_f28b5e55506ab1123951a7789b28ce563D",
    "yrx-13": "Azvl298q2-83jIPv2M8C9Rc2zBSgkE-SSaQTRi34FzpRjFXKtWDf4ll0o5c-",
    "sessionid": "x05vti2vu64kzrzimol7g74utm5h5ktz",
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1724381259,1724500182,1724501051,1724896456",
    "no-alert": "true"
}
sum = 0
for page in range(1, 101):
    data = {
        'page': page,
        'token': base64.b64encode(str(page).encode())
    }
    response = requests.post('https://www.python-spider.com/api/challenge54', cookies=cookies, headers=headers, data=data).json()
    datas = response['data']
    for data in datas:
        value = int(data['value'])
        print(value)
        sum += value
print(sum)
