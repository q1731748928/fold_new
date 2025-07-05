import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://gleami.apps.fao.org",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://gleami.apps.fao.org/scenarios",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "csrftoken": "ccoCJveqBKM6jADPOelm9k69VfXRF8Hzo6NTWZsUl1tDLxkxBc21l1Up7obG9lVv",
    "sessionid": "9gyopkur38k1hecaix79jxom3dhpp9k6",
    "_ga": "GA1.1.1163173444.1747796148",
    "_ga_D1DDJEPMCW": "GS2.1.s1747796148$o1$g1$t1747800406$j0$l0$h0"
}
url = "https://gleami.apps.fao.org/scenarios"
data = {
    "csrfmiddlewaretoken": "bu4f1nEihmvTJEw6BgGPgtWXFBGodsxEnotweRSM1DcqbBdOoenusaKdRKUdHFLA",
    "scenario": ""
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)