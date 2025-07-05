import re
import time

import requests
from lxml import etree
start = time.time()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://xz.ke.com/ershoufang/",
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
    "SECKEY_ABVK": "el0wKxO6yTShMRDYAUu/BFMDcEoOXJxx3+Kll//5eNS8V3iYvrJouLBnOdUOXr15594NOq0qnzyx8HW+7eg6ng%3D%3D",
    "BMAP_SECKEY": "el0wKxO6yTShMRDYAUu_BFMDcEoOXJxx3-Kll__5eNTOqQTWW6nkQGMQ5VlTrLOoEFKIC3zHVAoFJm4ds2tp0AkdO4hLktyX_JrSiwQnfB-4BbQen0tU_ldpab1G30TXz1YWqBHMeLhbRgOuXjaHAqa-KCkYB3SqP_NCwt1gbKczlRdItCgagiZ9edh4ot5brTq6rXsjtreDLs-hcU78Cg",
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
    "select_city": "320300",
    "lianjia_ssid": "d8bbe1b0-5774-4659-9afa-c69ae83a3dbf",
    "Hm_lvt_b160d5571570fd63c347b9d4ab5ca610": "1747636299,1747639025,1747641651",
    "HMACCOUNT": "11F3EEC15F332D20",
    "Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610": "1747641654",
    "srcid": "eyJ0Ijoie1wiZGF0YVwiOlwiYTQ0ZDM3NzUyZmEwNmQ4Yzg0NTU0MDZiNWNlZjY1NmM0NjE2MjkzMDAyY2IxZDhkMTg5ZTJhZTRlYjNiNDE3ZGZkZDY1YzU3Njk4Njg5OTQyYmE5ZDM2NGU5MDliNGI4NmU2NDFmMmVlMzY4OGZiYjc1MWU5YmI0YzQ5Njg3YmM3ZTI0NDdjMjdjOTZmYjZiY2Q1MTJjMTEwZDE2YzQ3MmJiYTIyMGI4M2U1NmM3YjRiZTY2NjIyNzYzMzE3NWMyYjY4YWZiZjNjMDAyZGRhNWQ0Y2U3NmM0NzA3MWYxMzJhNmIzOGFjN2ZiYjY0OTYxZjRhNGE0ODg0YzRmYTYzZGRmMTE0MDFmZjNiODZjNmE5ZWI3Y2Q4ZjhiOWFkNWY0YWYyYTRjNzgyYmZlMzYxMGQxNWZkNWE5NDJlMTVkMjFcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiMmY0MzcyNWJcIn0iLCJyIjoiaHR0cHM6Ly94ei5rZS5jb20vZXJzaG91ZmFuZy9ycyVFNCVCQSU5MSVFOSVCRSU5OSVFNSU4QyVCQS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=="
}
result = []
for i in range(1, 2):
    # 小区
    community_name = ''
    # 面积 m2
    area = ''
    # 平均价格（元/m2）
    avg_price = ''
    # 成交日期
    deal_date = ''
    # 成交周期
    deal_cycle = ''
    # 建成年份
    build_year = ''
    # 户型
    house_type = ""
    # 房屋朝向
    house_direction = ''
    # 装修情况
    house_decoration_status = ''
    # 户型结构
    house_construct = ''
    # 建筑类型
    building_type = ''
    # 建筑结构
    building_structure = ''
    # 电梯配备
    has_elevator = ''
    # 所在楼层
    floor = ''
    # 房屋用途
    house_usage = ''
    print(f"正在爬取第{i}页")
    url = f"https://xz.ke.com/ershoufang/pg{i}rs%E4%BA%91%E9%BE%99%E5%8C%BA/"
    response = requests.get(url, headers=headers, cookies=cookies)
    tree = etree.HTML(response.text)
    contents = tree.xpath('//div[@class="content"]')
    ul_list = tree.xpath('//ul[@class="sellListContent"]')
    for ul in ul_list:
        hrefs = ul.xpath('.//li[@class="clear"]/a/@href')
        for href in hrefs:
            response = requests.get(href, headers=headers, cookies=cookies).text
            tree = etree.HTML(response)
            contents = tree.xpath('//div[@class="content"]')
            time.sleep(3)
            for content in contents:
                price_containers = content.xpath('./div[@class="price-container"]')
                house_infos = content.xpath('./div[@class="houseInfo"]')
                aroundInfo = content.xpath('./div[@class="aroundInfo"]')
                for price_container in price_containers:
                    avg_price = price_container.xpath('./div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()')[0]
                for house_info in house_infos:
                    area = str(house_info.xpath('./div[@class="area"]/div[@class="mainInfo"]/text()')[0]).replace("平米", "")
                    build_year = str(house_info.xpath('./div[@class="area"]/div[@class="subInfo noHidden"]/text()')[0]).split("年建")[0].strip()
                for aroundInfo in aroundInfo:
                    community_name = str(aroundInfo.xpath('./div[@class="communityName"]/a[1]/text()')[0])
                # print(community_name.strip())
                # print(area.strip())
                # print(avg_price.strip())
                # print(build_year.strip())
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
                        if '房屋户型' in base_span_list:
                            house_type = li_base
                        # elif
                        # print(span, li)
                        # print(base_span_list + ":" + li_base)
                        # result.append(str(base_span_list) + ":" + str(li))
                        # result.append("\n")
                transactions = introContent.xpath('./div[@class="transaction"]')
                for transaction in transactions:
                    transaction_span_lists = transaction.xpath('./div[@class="content"]/ul//li[@class=" has-data"]/span/text()')
                    transaction_lists = transaction.xpath('./div[@class="content"]//ul//li/text()')
                    for transaction_list, transaction_span in zip(transaction_lists, transaction_span_lists):
                        transaction_span = transaction_span.strip()
                        # if transaction_span == '':
                        #     transaction_span = '暂无数据'
                        # transaction_list = transaction_list.strip()
                        # if transaction_list == '':
                        #     transaction_list = '暂无数据'
                        if '上次交易' in transaction_span:
                            deal_date = transaction_list
                        # elif '成交周期' in transaction_span:
                        #     deal_cycle = transaction_list
                        print(deal_date, deal_cycle)
            #             # result.append(str(transaction_span) + ":" + str(transaction_list))

            #             result.append("\n")
            # result.append("\n\n")

# for res in result:
#     with open('bk.txt', 'a+', encoding='utf-8') as f:
#         f.write(res)
# end = time.time()
# print(f"写入成功，耗时{end - start}秒")
# print('写入成功')