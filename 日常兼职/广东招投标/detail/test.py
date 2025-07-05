import requests
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://zbtb.gd.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
    "__jsluid_s": "d0af8236def3eba872f19902a8f35c15",
    "openstack_cookie_insert": "97258147",
    "_horizon_sid": "542af0bd-bdd9-44b6-adc2-27615f30e6fe"
}
url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/his1/view-pdf"
params = {
    "attachId": "02745f46fd91460ba0d8c2c2abdc89c8"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)

with open(f"./test.pdf", "wb") as f:
    f.write(response.content)