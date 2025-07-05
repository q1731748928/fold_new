



import json
import time

import execjs
import requests
import base64

requests = requests.session()


class JyClick():
    def __init__(self):
        self.one_url = 'https://www.geetest.com/demo/gt/register-click-official?t={}'
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
        response = requests.get(self.one_url.format(str(int(time.time() * 1000))), headers=self.headers)
        challenge = response.json()['challenge']
        gt = response.json()['gt']
        self.gt = gt
        self.challenge = challenge

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
        print(requests.get('https://api.geevisit.com/ajax.php', params=params, headers=self.headers).text)

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
            "token": "8Ex4T4HOPaoA2Sl91uhDRjGZc8zS0XzhpCOvwBtkbR4",
            "type": verify_type
        }
        if extra:
            payload['extra'] = extra
        resp = requests.post(self._custom_url, headers=self._headers, data=json.dumps(payload))
        # print(resp.text)
        return resp.json()['data']['data']

    def parse_data(self, pic, s, c):
        img_res = requests.get('https://static.geetest.com' + pic, headers=self.headers)
        open('dd.png', 'wb').write(img_res.content)
        xy = self.click_verify(img_res.content)
        click_true_str = self.geetest_click(xy)
        # print(click_true_str)
        print(click_true_str, pic, s, c, self.gt, self.challenge)
        js = execjs.compile(open('01-极验点选.js', encoding='utf-8').read())
        data_w = js.call('get_w', click_true_str, pic, c, self.gt, self.challenge, s)
        # print(data_w)
        return data_w

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
        # return json.loads(res.text[1:-1])['data']['validate']

    def main(self):
        self.one_request()
        pic, s, c = self.two_request()
        data_w = self.parse_data(pic, s, c)
        validate = self.three_request(data_w)


if __name__ == '__main__':
    jy = JyClick()
    jy.main()