import os.path
import time

import requests
import json

headers = {
    "Host": "www.lawsdata.com",
    "sec-ch-ua-platform": "\"macOS\"",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "authentication": "您自己的登录凭证",
    "sec-ch-ua-mobile": "?0",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.lawsdata.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.lawsdata.com/",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=1, i"
}
for i in range(1, 33):
    url = "https://www.lawsdata.com/sweet/compass-instrument/search/instrument"
    data = {
        "textSearchList": [
            {
                "fieldNameList": [
                    "_text_"
                ],
                "valueList": [
                    "虚假投资理财"
                ],
                "fuzzy": 0,
                "key": "@text"
            }
        ],
        "sortField": "courtLevel",
        "sortOrder": "desc",
        "pageNo": i
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    documents = response.json()['returnData']["documents"]
    for document in documents:
        documentLists = document["documentList"]
        for documentList in documentLists:
            id = documentList.get('id')
            caseTitle = documentList.get('caseTitle')
            # print(id, caseTitle)
            url = f"https://www.lawsdata.com/sweet/compass-instrument/export/wordForInstrument/{id}"
            params = {
                "": ""
            }
            response = requests.get(url, headers=headers, params=params)
            time.sleep(5)
            if os.path.exists(f'./word/{caseTitle}.docx'):
                print('文件已存在，跳过')
                continue
            else:
                with open(f'./word/{caseTitle}.docx', 'wb') as f:
                    f.write(response.content)
                print('下载成功!')

