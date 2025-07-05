import requests


headers = {
    "Host": "home.kyexam.com",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260212 MMWEBSDK/20230805 MMWEBID/3482 MicroMessenger/8.0.42.2460(0x28002A34) WeChat/arm32 Weixin8.0.42.2460(0x28002A34) WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://home.kyexam.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://home.kyexam.com/dashboard",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "priority": "u=1, i"
}
cookies = {
    "yksuhome": "1Iy3uS4Yz7yUP5XFqHIJbColcndbaVXlkqRSRpQCpY0o%3D",
    "uid": "oyG776R8y7",
    "_ga": "GA1.1.1148119202.1745542416",
    "_ga_GN0HM4X9MD": "GS1.1.1745542415.1.1.1745542631.56.0.0"
}
url = "https://home.kyexam.com/udo/getwrongquedetail"
qid = 64923028
qtrid = "1915344216926494722,1915347489024679970"
# 使用 f-string 将 qid 替换到 JSON 字符串中
data = {
    "state": f'{{"qid":{qid},"qtrid":"{qtrid}"}}'
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)