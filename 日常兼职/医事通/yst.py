import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.jkwin.com.cn/yst_web/hospital/findHospital",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "JSESSIONID": "2B0E08ADB0F9537DC839FCF7D29D49A8",
    "Hm_lvt_ecf73a45c81aa9493ec73d1d2de618f6": "1745388929",
    "HMACCOUNT": "11F3EEC15F332D20",
    "Hm_lpvt_ecf73a45c81aa9493ec73d1d2de618f6": "1745388932"
}
url = "https://www.jkwin.com.cn/yst_web/hospital/getOrg"
for i in range(1, 5):
    params = {
        "areaId": "42",
        "orgTypeId": "",
        "orgGradeName": "",
        "pageNo": str(i),
        "pageSize": "10"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    results = response.json()['data']['results']
    for org in results:
        #  医院名称
        ORG_NAME = org.get('ORG_NAME')
        # 医院地址
        ORG_ADDR = org.get('ORG_ADDR')
        # 电话
        CONTACT_PHONE = org.get('contact')
        print(ORG_NAME, ORG_ADDR, CONTACT_PHONE)
