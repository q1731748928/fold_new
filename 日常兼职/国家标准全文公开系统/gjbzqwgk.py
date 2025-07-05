import random
import time

import ddddocr


import requests
from lxml import etree
import re
wait_time = random.uniform(10, 30)
ocr = ddddocr.DdddOcr()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://openstd.samr.gov.cn/bzgk/gb/std_list_type?p.p1=1&p.p90=circulation_date&p.p91=desc",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "JSESSIONID": "B33FC7255A64BD9B88B210A055E6C630"
}
url = "https://openstd.samr.gov.cn/bzgk/gb/std_list_type"
params = {
    "r": "0.1016201731373394",
    "page": "1",
    "pageSize": "10",
    "p.p1": "1",
    "p.p90": "circulation_date",
    "p.p91": "desc"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
tree = etree.HTML(response.text)
clicks = tree.xpath('//tr/td[@class="mytxt"]/a/@onclick')
for click in clicks:
    result = re.search(r"'([^']*)'", click)
    if result:
        link = result.group(1)
        # print(link)
        base_url = 'https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=' + str(link)
        resp = requests.get(base_url, headers=headers, cookies=cookies)
        time.sleep(wait_time)
        # print(resp.text)
        tree = etree.HTML(resp.text)
        data_values = tree.xpath('//table[@class="tdlist"]//tr//button[@class="btn xz_btn btn-sm btn-warning app-hide"]/@data-value')
        for data_value in data_values:
            time1 = round(time.time() * 1000)
            url = "http://c.gb688.cn/bzgk/gb/gc"
            params = {
                f"_{time1}": ""
                # "1748080585216": ""
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
            # url = f"http://c.gb688.cn/bzgk/gb/showGb?type=download&hcno={data_value}"
            #
            # if str(response.text) == "success":
            #     down_url2 = f'http://c.gb688.cn/bzgk/gb/viewGb?hcno={data_value}'
            #     print(down_url2)
            #     res = requests.get(down_url2, headers=headers, cookies=cookies)
            #     with open(f"./{data_value}.pdf", "wb") as f:
            #         f.write(res.content)
            #     print('下载文件成功')
