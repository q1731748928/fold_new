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
url = "https://home.kyexam.com/udo/getwrongques"
# for i in range(1, 11):
limit = 28
start = 112
data = {
    "state": "{\"limit\":28,\"start\":112}"
    # f'{{"limit":{limit},"start":"{start}"}}'
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
# print(response.text)
datas = response.json()['data']
for data in datas:
    qid = data.get('qid')
    qtrid = data.get('qtrid')
    data = {
        "state": f'{{"qid":{qid},"qtrid":"{qtrid}"}}'
    }
    url = "https://home.kyexam.com/udo/getwrongquedetail"
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    # print(response.text)
    datas = response.json()['data']
    title = datas['title']
    qtype = datas['qtype']
    if qtype == 1:
        print('[单选题]' + datas['title'])
    if qtype == 2:
        print('[多选题]' + datas['title'])
    if qtype == 3:
        print('[判断题]' + datas['title'])
    options = datas.get('options')
    for option in options:
        print(option)
    rightoids = datas.get('rightoids')
    # 先遍历所有选项并输出
    # for option in options:
    #     title = option.get('title')
    #     print("选项是: " + str(title))
    for index, option in enumerate(options):
        # 用字母 A, B, C... 来表示选项
        option_label = chr(65 + index)  # 65 是字母 'A' 的 ASCII 码
        print(f'{option_label}. {option.get("title")}')
    # 查找并输出正确答案
    correct_answers = []

    for index, option in enumerate(options):
        oid = option['oid']
        title = option['title']
        if oid in rightoids:  # 如果当前 oid 是正确答案之一
            option_label = chr(65 + index)  # 获取对应的字母
            correct_answers.append(f"{option_label}")  # 将正确答案添加到列表中
            # 将所有正确答案合并成一行输出
    print("答案是：" + "".join(correct_answers))
