import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Range": "bytes=0-1161700",
    "Referer": "https://zbtb.gd.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDkwOTk4NjIsIm5iZiI6MTc0OTA5MjY2MiwianRpIjoiMjFhZWVjODg2ZTc4NGNkZGE1MDc2YzMyMWQ2MjE1OTAiLCJzdWIiOiIiLCJhZ2VudElkIjoiIn0.reErISxH_K8DweoTUJjC5IIYyeDeI8Hfbwtt25yBSJE"
}
cookies = {
    "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
    "__jsluid_s": "d0af8236def3eba872f19902a8f35c15",
    "openstack_cookie_insert": "44166039",
    "_horizon_sid": "3a2bf85d-38c0-4a78-971f-5806fcc1a14e"
}
url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/file/v2/download/556189902639846400"
response = requests.get(url, headers=headers, cookies=cookies)

with open(f"./test.pdf", "wb") as f:
    f.write(response.content)