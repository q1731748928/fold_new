from Crypto.Cipher import AES
import base64
import json
import requests

headers = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36;SuiRui/mh/ver=1.6.1",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "deviceId": "cccc9eeadaf3084c868dcd1e8606a32b",
    "t": "1737471479132",
    "s": "8cf25afa241abaa1fc5ed587de26ebf1",
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDM0NTUyMCIsImlzcyI6IiIsImlhdCI6MTczNzQyMDM2NywibmJmIjoxNzM3NDIwMzY3LCJleHAiOjE4OTUxMDAzNjd9.B5GBpim6xTuGdaFGHAoI9RWtUJk1baV0q4TgU_3xlNc",
    "Host": "api.axlywszrnr.work",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

def decrypt(str):

    key = 'JhbGciOiJIUzI1Ni'.encode('utf8')
    # print(key)
    text = base64.b64decode(str)
    iv = b"JhbGciOiJIUzI1Ni"
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)

    plain_text = cryptos.decrypt(text)
    #print(plain_text)
    print(plain_text.decode('unicode_escape'))

headers = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36;SuiRui/mh/ver=1.6.1",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "deviceId": "cccc9eeadaf3084c868dcd1e8606a32b",
    "t": "1737471927741",
    "s": "2356d90decdd5710ab17fe928bcd8d50",
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDM0NTUyMCIsImlzcyI6IiIsImlhdCI6MTczNzQyMDM2NywibmJmIjoxNzM3NDIwMzY3LCJleHAiOjE4OTUxMDAzNjd9.B5GBpim6xTuGdaFGHAoI9RWtUJk1baV0q4TgU_3xlNc",
    "Host": "api.axlywszrnr.work",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
url = "https://api.axlywszrnr.work/api/comics/base/chapterInfo"
params = {
    "chapterId": "150490"
}
response = requests.get(url, headers=headers, params=params)

js = json.loads(response.text)
encData = js['encData']
print(decrypt(encData))