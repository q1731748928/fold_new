import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://gleami.apps.fao.org",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://gleami.apps.fao.org/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-fetch-storage-access": "active",
    "x-client-data": "CI+2yQEIprbJAQipncoBCI3cygEIlaHLAQiUo8sBCIagzQEI3e7OARjh4s4B",
    "content-length": "0"
}
cookies = {
    "csrftoken": "ccoCJveqBKM6jADPOelm9k69VfXRF8Hzo6NTWZsUl1tDLxkxBc21l1Up7obG9lVv",
    "sessionid": "9gyopkur38k1hecaix79jxom3dhpp9k6",
    "_ga": "GA1.1.1163173444.1747796148",
    "_ga_D1DDJEPMCW": "GS2.1.s1747796148$o1$g1$t1747796421$j0$l0$h0ar_debug=1ar_debug=1"
}
url = "https://gleami.apps.fao.org/animals_selection"
data = {
    'productionsys': ['1_1', '1_2', '2_3', '2_4', '3_5', '3_6', '4_7', '4_8', '5_9', '5_10', '5_11', '6_12', '6_13', '6_14'],
    'animalproductionsysproduct': [
        '1_1_1', '1_1_2', '1_2_1', '1_2_2', '2_3_1', '2_3_2', '2_4_1', '2_4_2',
        '3_5_1', '3_5_2', '3_6_1', '3_6_2', '4_7_1', '4_7_2', '4_8_1', '4_8_2',
        '5_9_3', '5_10_1', '5_11_3', '6_12_1', '6_13_1', '6_14_1'
    ],
    'csrfmiddlewaretoken': 'AIe9wKjQXWPoiJfwG9Jrc3noEtqRljNTMCDqJexkHdwVKGWet7q6oKbEQCEGPw1P'
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
print(response.headers)