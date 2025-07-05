import json

import execjs
import requests


headers = {
    "Host": "wenshu.court.gov.cn",
    "sec-ch-ua-platform": "\"macOS\"",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua-mobile": "?0",
    "Origin": "https://wenshu.court.gov.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=e6fe1417aab7a9187433a493985997cc&s21=%E7%9B%97%E7%AA%83&s16=%E5%88%91%E4%BA%8B%E6%A1%88%E7%94%B1&s11=1&s8=02&s9=0201&s6=01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}
cookies = {
    "wzws_sessionid": "oGhFUdOAMTE1LjIwNC43Ni4yMzGCNmY2OTAxgTViMmJhNA==",
    "SESSION": "55df6a06-3664-4a40-b7dd-8832112428f6",
    "wzws_cid": "747726db551223175c8f8fc2806501061f5d709f24b45764120f019b327f8f230dff8d3aa6e667293f5b4f86eabd4f279140537a1994edea1a663b8347d04e795821882c8bc799e9f55ef9e1218e7706"
}
url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
data = {
    "pageId": "e6fe1417aab7a9187433a493985997cc",
    "s21": "盗窃",
    "s16": "刑事案由",
    "s11": "1",
    "s8": "02",
    "s9": "0201",
    "s6": "01",
    "sortFields": "s50:desc",
    "ciphertext": "1001000 1011001 110001 1100110 1100100 1111001 1111010 1100111 1001000 1100101 1001110 1010001 111000 1001011 1101111 1100111 1010010 1000110 1011000 1101011 1101011 110010 111001 1001100 110010 110000 110010 110101 110000 110110 110000 111000 1110101 1101100 1111010 110101 110110 1010101 110111 1100100 1011000 1010010 1101000 1110001 1010110 1000001 1000111 1011000 110001 1110111 1100111 1110100 1101110 1110111 111101 111101",
    "pageNum": "1",
    "pageSize": "15",
    "queryCondition": "[{\"key\":\"s21\",\"value\":\"盗窃\"},{\"key\":\"s11\",\"value\":\"1\"},{\"key\":\"s8\",\"value\":\"02\"},{\"key\":\"s9\",\"value\":\"0201\"},{\"key\":\"s6\",\"value\":\"01\"},{\"key\":\"s39\",\"value\":\"R10\"},{\"key\":\"s42\",\"value\":\"2024\"}]",
    "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc",
    "__RequestVerificationToken": "pBkWhWxbaFO5OSlrHl98XK3P",
    "wh": "944",
    "ww": "1728",
    "cs": "0"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
# print(response.text)
secretKey = response.json()['secretKey']
result = response.json()['result']
ctll = execjs.compile(open('cpws.js', encoding='utf-8').read())
decrypt_result = ctll.call('decrypt', result, secretKey)
# print(decrypt_result)
js = json.loads(decrypt_result)
print(js)
