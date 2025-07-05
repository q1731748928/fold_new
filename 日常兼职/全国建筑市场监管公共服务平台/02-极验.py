



import json
import time

import execjs
import requests
import base64

requests = requests.session()


class JyClick():
    def __init__(self):
        self.one_url = 'https://jzsc.mohurd.gov.cn/APi/webApi/geetest/startCaptcha'
        self.two_url = 'https://api.geevisit.com/get.php'
        self._custom_url = "http://api.jfbym.com/api/YmServer/customApi"
        self.gt = None
        self.challenge = None
        self._headers = {
            'Content-Type': 'application/json'
        }
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.geetest.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }

    def one_request(self):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://jzsc.mohurd.gov.cn/data/project/detail?id=3148",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLVXxoJ2MA2ROVufX7q+xA1PhpUUKvcMtoMqfGfwdLCb8g==",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "timeout": "30000",
            "v": "231012"
        }
        response = requests.get(self.one_url, headers=headers)
        res = execjs.compile(open('03-aes案例.js', encoding='utf-8').read())
        result = res.call('b', response.text)
        js = json.loads(result)
        challenge = js['data']['challenge']
        gt = js['data']['gt']
        randomId = js['data']['randomId']
        self.gt = gt
        self.challenge = challenge
        self.randomId = randomId

    def two_request(self):
        params = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": "",
            "callback": "geetest_" + str(int(time.time() * 1000))
        }
        requests.get('https://api.geevisit.com/ajax.php', params=params, headers=self.headers)

        params = {
            "is_next": "true",
            "type": "click",
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "https": "true",
            "protocol": "https://",
            "offline": "false",
            "product": "float",
            "api_server": "api.geevisit.com",
            "isPC": "true",
            "autoReset": "true",
            "width": "100%",
        }
        response = requests.get(self.two_url, headers=self.headers, params=params)
        pic = json.loads(response.text[1:-1])['data']['pic']
        s = json.loads(response.text[1:-1])['data']['s']
        c = json.loads(response.text[1:-1])['data']['c']
        return pic, s, c


    def geetest_click(self, click_xy):
        # 坐标还原
        click_point_array = click_xy.split('|')
        click_point_true = []
        for item in click_point_array:
            x, y = item.split(',')
            point = str(int(int(x) / 344 * 10000)) + '_' + str(int(int(y) / 344 * 10000))
            click_point_true.append(point)
        click_true_str = ','.join(click_point_true)
        return click_true_str

    def click_verify(self, image, extra=None, verify_type="30103"):
        payload = {
            "image": base64.b64encode(image).decode(),
            "extra": 'click',
            "token": "I61cGqzqQ1SkKeLEw2IG_q1pBzMz6qWM5K4ypvv8CKI",
            "type": verify_type
        }
        if extra:
            payload['extra'] = extra
        resp = requests.post(self._custom_url, headers=self._headers, data=json.dumps(payload))
        return resp.json()['data']['data']

    def parse_data(self, pic, s, c):
        img_res = requests.get('https://static.geetest.com' + pic, headers=self.headers)
        open('dd.png', 'wb').write(img_res.content)
        xy = self.click_verify(img_res.content)
        click_true_str = self.geetest_click(xy)
        js = execjs.compile(open('01-极验点选.js', encoding='utf-8').read())
        data_w = js.call('get_w', click_true_str, pic, c, self.gt, self.challenge, s)
        return data_w

    def four_request(self, validate):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://jzsc.mohurd.gov.cn/data/project/detail?id=137919",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
            "accessToken": 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLVXxoJ2MA2ROVufX7q+xA1PhpUUKvcMtoMqfGfwdLCb8g==',
            "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "timeout": "30000",
            "v": "231012"
        }
        cookies = {
            "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1749224334,1749255683",
            "HMACCOUNT": "5D6551E60719B08D",
            "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1749258726"
        }
        url = "https://jzsc.mohurd.gov.cn/APi/webApi/geetest/verifyLoginCode"
        params = {
            "geetest_challenge": self.challenge,
            "geetest_validate": validate,
            "geetest_seccode": f"{validate}|jordan",
            "randomId": self.randomId
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res = execjs.compile(open('03-aes案例.js', encoding='utf-8').read())
        result = res.call('b', response.text)
        js = json.loads(result)
        accessToken = js['data']['accessToken']
        print(accessToken)


    def three_request(self, data_w):
        params = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": data_w,
        }
        url = "https://api.geevisit.com/ajax.php"
        time.sleep(2)
        res = requests.get(url, params=params, headers=self.headers)
        print(res.text)
        return json.loads(res.text[1:-1])['data']['validate']
    def main(self):
        self.one_request()
        pic, s, c = self.two_request()
        data_w = self.parse_data(pic, s, c)
        validate = self.three_request(data_w)
        self.four_request(validate)



if __name__ == '__main__':
    jy = JyClick()
    jy.main()

