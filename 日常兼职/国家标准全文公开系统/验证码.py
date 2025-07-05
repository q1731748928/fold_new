import time

import requests
import ddddocr
time1 = round(time.time() * 1000)
ocr = ddddocr.DdddOcr()

headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://c.gb688.cn/bzgk/gb/showGb?type=download&hcno=F60B16F6F204597DDAFD8CCCFC931E11",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID": "46963ABFB686B48639A29241A7047FD4"
}
url = "http://c.gb688.cn/bzgk/gb/gc"
params = {
    # f"_{time1}": ""
    "1748080585216": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

with open("验证码.jpeg", "wb") as f:
    f.write(response.content)
print('下载成功')

image = open("验证码.jpeg", "rb").read()
result = ocr.classification(image)
print(result)

url = "http://c.gb688.cn/bzgk/gb/verifyCode"
data = {
    "verifyCode": f'{result}'
}
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

print(response.text)
print(response)