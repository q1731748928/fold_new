import base64
import json
import time
import scrapy
import execjs
import ddddocr
from scrapy import cmdline
from scrapy.http import JsonRequest


class ZbtbCaptchaSolverSpider(scrapy.Spider):
    name = "zbtb_captcha_solver"
    # start_urls = ['https://zbtb.gd.gov.cn/#/jygg?thirdType=10']

    def __init__(self, js_file="gj.js", check_js_file="get_postjson.js"):
        self.js_file = js_file
        self.check_js_file = check_js_file
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://zbtb.gd.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://zbtb.gd.gov.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "X-Dgi-Req-App": "ztbjg-portal",
            "X-Dgi-Req-Nonce": "501iFRjEQQHS5pyI",
            "X-Dgi-Req-Signature": "7213e168b97756018563bca8660a7d6755ffcf8d93a4fb21344999f7a2dc13e5",
            "X-Dgi-Req-Signatures": "58503fdbc59a6ccaafc833d549deb4299fb055f04494d8c71974a7406ce78989",
            "X-Dgi-Req-Timestamp": "1747125880919",
            "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.cookies = {
            "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
            "openstack_cookie_insert": "97258147",
            "_horizon_sid": "ca7b5dd5-2b22-4778-a341-354e4c046852"
        }

    def set_headers(self, data):
        with open(self.js_file, encoding='utf-8') as f:
            js_code = f.read()
        ctll = execjs.compile(js_code)
        result = ctll.call("get_data", data)

        self.headers['X-Dgi-Req-App'] = str(result.get('X-Dgi-Req-App'))
        self.headers['X-Dgi-Req-Nonce'] = str(result.get('X-Dgi-Req-Nonce'))
        self.headers['X-Dgi-Req-Signature'] = str(result.get('X-Dgi-Req-Signature'))
        self.headers['X-Dgi-Req-Timestamp'] = str(result.get('X-Dgi-Req-Timestamp'))
        self.headers['X-Dgi-Req-Signatures'] = str(result.get('X-Dgi-Req-Signatures'))
    def get_captcha_images(self):
        url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/get"
        data = {"captchaType": "blockPuzzle"}
        self.set_headers(data)
        data = json.dumps(data, separators=(',', ':'))
        yield JsonRequest(url=url, headers=self.headers, cookies=self.cookies, data=data, callback=self.save_captcha_images)

    def save_captcha_images(self, response):
        print(response)
        originalImageBase64 = response.json()['data']['repData']['originalImageBase64']
        jigsawImageBase64 = response.json()['data']['repData']['jigsawImageBase64']
        secretKey = response.json()['data']['repData']['secretKey']
        token = response.json()['data']['repData']['token']
        image_data1 = base64.b64decode(originalImageBase64)
        image_data2 = base64.b64decode(jigsawImageBase64)
        with open('dd1.jpg', 'wb') as file1:
            file1.write(image_data1)
        with open('dd2.jpg', 'wb') as file2:
            file2.write(image_data2)
        yield token, secretKey

    def solve_captcha(self, response):
        print(response)
        originalImageBase64 = response.json()['data']['repData']['originalImageBase64']
        jigsawImageBase64 = response.json()['data']['repData']['jigsawImageBase64']
        secretKey = response.json()['data']['repData']['secretKey']
        token = response.json()['data']['repData']['token']
        image_data1 = base64.b64decode(originalImageBase64)
        image_data2 = base64.b64decode(jigsawImageBase64)
        with open('dd1.jpg', 'wb') as file1:
            file1.write(image_data1)
        with open('dd2.jpg', 'wb') as file2:
            file2.write(image_data2)
        with open('dd1.jpg', 'rb') as f:
            target_bytes = f.read()
        with open('dd2.jpg', 'rb') as f:
            background_bytes = f.read()
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        Y = det.slide_match(background_bytes, target_bytes)['target'][0]
        with open(self.check_js_file, encoding='utf-8') as f:
            js_code = f.read()
        ctll = execjs.compile(js_code)
        pointJson = ctll.call("get_postjson", Y, secretKey)
        data = {
            "captchaType": "blockPuzzle",
            "pointJson": str(pointJson),
            "token": token
        }
        self.set_headers(data)
        check_url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/check"
        yield JsonRequest(check_url, headers=self.headers, cookies=self.cookies, data=data)
        # return response.json()['data']['repData']['token']
    def start_requests(self):
        response = self.get_captcha_images()
        print(response)
        token, secretKey = self.save_captcha_images(response)
        token = self.solve_captcha(token, secretKey)
        url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/notice/search"
        o = {
            "data": {
                "type": "trading-type",
                "publishStartTime": "",
                "publishEndTime": "",
                "keyword": "",
                "thirdType": 10,
                "siteCode": "44",
                "secondType": "A",
                "projectType": "",
                "dateType": "",
                "searchType": "pf",
                "pageNo": 7,
                "pageSize": 10,
                "openConvert": False
            }
        }
        self.set_headers(o)
        self.headers['Vtoken'] = token
        JsonRequest(url=url, headers=self.headers, cookies=self.cookies, data=o.get('data'))



if __name__ == '__main__':
    cmdline.execute('scrapy crawl zbtb_captcha_solver'.split())
