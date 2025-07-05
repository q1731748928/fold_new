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
data = {
    "state": "{\"search\":\"\",\"limit\":28,\"start\":56,\"order\":\"asc\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
# print(response.text)
datas =  response.json()['data']
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
    print('题目是:', title)
    options = datas.get('options')
    rightoids = datas.get('rightoids')
    for option in options:
        oid = option.get('oid')
        title = option.get('title')
        print("oid是:" + str(oid) + "," + "title:是" + str(title))
        # for rightoid in rightoids:
        #     print(rightoid)
            # if oid == rightoid:
                # print("答案是:" + title)
        # for rightoid in rightoids:
    #     for option in options:
    #         print(option)
    #         # op = option.get("title")
    #         # print(op)
    #         if rightoid == option.get("oid"):
    #             pass
                # title = option.get('title')
                # print("答案是:" + title)
        # 根据oid获取title
        # if data['oid'] == 228475708:
        #     title = data['title']
        #     print(f"对应的title是: {title}")
        # else:
        #     print("没有找到匹配的oid")
        # print("答案是", rightoid)
        # # 给定一个oid的值
        # oid_to_find = rightoid
        # # 判断oid是否匹配，并获取对应的title
        # if data['oid'] == oid_to_find:
        #     title = data['title']
        #     print(f"对应的title是: {title}")
        # else:
        #     print("未找到对应的title")
    # for data in datas:
    #     options = data.get('options')
    #     for option in options:
    #         print(option)
#
#     print(response.text)
#     print(response)