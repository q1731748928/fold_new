import json

import requests
import execjs
import pymongo

class JZGL():
    def __init__(self):

        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://jzsc.mohurd.gov.cn/data/company",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "accessToken": "jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLWIHXIL6R2vYs6t/kqWZLa9hpUUKvcMtoMqfGfwdLCb8g==",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "timeout": "30000",
            "v": "231012"
        }
        self.url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/project/list"
        self.js = execjs.compile(open('03-aes案例.js', encoding='utf-8').read())
        self.params = {
    "projectRegionId": "610102",
    "pg": "0",
    "pgsz": "15",
    "total": "0"
}

    def parse_data(self, res):
        da = json.loads(self.js.call('b', res))
        print(da)
        # item = {}
        # for i in da['data']['list']:
        #     item['QY_FR_NAME'] = i['QY_FR_NAME']
        #     item['QY_NAME'] = i['QY_NAME']
        #     print(item)

    def save_Data(self, item):
        pass



    def get_data(self):
        for i in range(1, 2):
            self.params['pg'] = i
            response = requests.get(self.url, headers=self.headers, params=self.params)
            self.parse_data(response.text)

    def main(self):
        self.get_data()

if __name__ == '__main__':
    jz = JZGL()
    jz.main()