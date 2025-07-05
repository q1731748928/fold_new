import re

import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "SECKEY_ABVK": "el0wKxO6yTShMRDYAUu/BFMDcEoOXJxx3+Kll//5eNT6WvxLUl2eNTaVPShbmJ2drksMLy3bBozFqhdMZW4kig%3D%3D",
    "BMAP_SECKEY": "el0wKxO6yTShMRDYAUu_BFMDcEoOXJxx3-Kll__5eNTOqQTWW6nkQGMQ5VlTrLOomCf-sK0td0h49EwK7b0I9dL-Nv3ckSeM4ZLtHmF-eRXTQqz7z2G5XQItRqz1TqeIUi7LKpnQlTdQqaEXqDPTNBrhlYoyBY2Vndl_LIXXr9HQlcnzoVQO59fqKZwF3dDDLy3ZhDDyfZtYY53CPivC2w",
    "lianjia_uuid": "872b476d-954f-4044-bbac-29733d771eef",
    "sajssdk_2015_cross_new_user": "1",
    "crosSdkDT2019DeviceId": "-y5bzco--3rckih-gzoapvaxl9s1s18-3ctdk4gtq",
    "login_ucid": "2000000180369959",
    "lianjia_token": "2.001447c4e5731c932e05eaedd492e1fb8e",
    "lianjia_token_secure": "2.001447c4e5731c932e05eaedd492e1fb8e",
    "security_ticket": "pBpuazyCxZVRZA4/DSo9S1wRGuv6x+m7/6sWg6eH1C1sZeZ+r4N6jYbvUFwWcOJ9rJPC/PYMS9+eA1Jitdnef0dMIWhePLP+TpOoW0Bo/qf7l/6axSb9P4HYtCpA4NShBROzI+vSXXiFUZK7uJqZsTfSDAUluluTURzlwgKxJAw=",
    "ftkrc_": "2a652128-2ed5-4051-a6e7-9e52d3074c35",
    "lfrc_": "abfe67a2-505c-4e86-b364-baeda290b61e",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22196e73da398237d-0502804e8995958-19525636-1930176-196e73da3992856%22%2C%22%24device_id%22%3A%22196e73da398237d-0502804e8995958-19525636-1930176-196e73da3992856%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
    "lianjia_ssid": "86de8565-1a08-4dc0-a3cb-a8ce6e37b59f",
    "Hm_lvt_b160d5571570fd63c347b9d4ab5ca610": "1747636299,1747639025,1747641651,1747659232",
    "HMACCOUNT": "11F3EEC15F332D20",
    "digv_extends": "%7B%22utmTrackId%22%3A%22%22%7D",
    "Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610": "1747659844",
    "srcid": "eyJ0Ijoie1wiZGF0YVwiOlwiOGUwMmYyMjg0ZWQ3YjY0ZWJiMTliMDg3YmE2NzQ5MmVkNzdiNGQ0OWZhYjVjYTBmYzE4MmE4ODc2NmI5Njg1MTJiOTNlNDViNTk0NmE5YWIyMTUwMDU1ZTJkZTI1ZDJlNWU1NDg4YTUwMWRkMWMwMTc3OWE4ZjE4NTE2YTM2MjVlYWIwNTlkNzNlZjA5MjczYThiM2Y4N2U1OWI3ODg1OTY3YmUzNThkZWYxMmNmN2M3ZWFjMzM0NTIyZjFkY2E3Njc2ZmE5MDcxNjMxOTViOGQxNWVmZGFmZGRjZWI2MzljMDNiOWZlNmY5YjI2OTY2YmE4ZTExODFkZGEwZTg2M2NmMGI0Mzg2ZjY1NTc4ZTUyODg1OWI2NTNlNGQwYzg4NzZlNDRkYjYyYjE0Y2QyYjg2YTdhMDVkZmFhZWZmOGRcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiODFkYzJiNTlcIn0iLCJyIjoiaHR0cHM6Ly94ei5rZS5jb20vZXJzaG91ZmFuZy8xMDMxNDA2NjQ1MzMuaHRtbCIsIm9zIjoid2ViIiwidiI6IjAuMSJ9",
    "select_city": "110000"
}
url = "https://xz.ke.com/ershoufang/103140664533.html"
response = requests.get(url, headers=headers, cookies=cookies)

from lxml import etree

tree = etree.HTML(response.text)
contents = tree.xpath('//div[@class="content"]')
for content in contents:
    price_containers = content.xpath('./div[@class="price-container"]')
    house_infos = content.xpath('./div[@class="houseInfo"]')
    aroundInfo = content.xpath('./div[@class="aroundInfo"]')
    # 平均价格（元/m2）
    avg_price = ''
    # 面积 m2
    area = ''
    # 小区
    community_name = ''
    # 建成年份
    build_year = ''
    for price_container in price_containers:
        avg_price = \
        price_container.xpath('./div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()')[0]
    for house_info in house_infos:
        area = house_info.xpath('./div[@class="area"]/div[@class="mainInfo"]/text()')[0]
        build_year = \
        str(house_info.xpath('./div[@class="area"]/div[@class="subInfo noHidden"]/text()')[0]).split("年建")[0].strip()
    for aroundInfo in aroundInfo:
        community_name = str(aroundInfo.xpath('./div[@class="communityName"]/a[1]/text()')[0])
    print(community_name, area, avg_price, build_year)
introContents = tree.xpath('//div[@class="introContent"]')
for introContent in introContents:
    bases = introContent.xpath('./div[@class="base"]')
    for base in bases:
        base_span_lists = base.xpath('./div[@class="content"]/ul//li/span[@class="label"]/text()')
        base_lists = base.xpath('./div[@class="content"]/ul//li/text()')
        li_base_list = []
        for base_list in base_lists:
            base_list = re.sub(r'[\n\s]+', '', base_list)
            if base_list == '':
                continue
            li_base_list.append(base_list)
        for base_span_list, li_base in zip(base_span_lists, li_base_list):
            base_span_list = base_span_list.strip()
            # print(span, li)
            print(base_span_list + ":" + li_base)
            # result.append(str(base_span_list) + ":" + str(li))
            # result.append("\n")
    transactions = introContent.xpath('./div[@class="transaction"]')
    for transaction in transactions:
        transaction_span_lists = transaction.xpath('./div[@class="content"]/ul//li[@class=" has-data"]/span/text()')
        transaction_lists = transaction.xpath('./div[@class="content"]//ul//li/text()')
        for transaction_list, transaction_span in zip(transaction_lists, transaction_span_lists):
            transaction_span = transaction_span.strip()
            if transaction_span == '':
                transaction_span = '暂无数据'
            transaction_list = transaction_list.strip()
            if transaction_list == '':
                transaction_list = '暂无数据'
            print(transaction_span, transaction_list)
