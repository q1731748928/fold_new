import re
import time

import pymysql
from lxml import etree

import requests
import random
wait_time = random.uniform(10, 30)

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="part_time_job")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://hip.ke.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "select_city": "320300",
    "lianjia_ssid": "3cc4e6a8-2205-4cc0-9aa2-3fe933dfb5b9",
    "lianjia_uuid": "ce021157-c505-4b25-bf94-5a21b0787276",
    "Hm_lvt_b160d5571570fd63c347b9d4ab5ca610": "1747737270",
    "HMACCOUNT": "11F3EEC15F332D20",
    "sajssdk_2015_cross_new_user": "1",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22196ed4256c399f-0cae81b883fc008-19525636-1930176-196ed4256c42e4d%22%2C%22%24device_id%22%3A%22196ed4256c399f-0cae81b883fc008-19525636-1930176-196ed4256c42e4d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
    "crosSdkDT2019DeviceId": "kslknv--3rckih-iyqqlu9j3p9dp2v-e9el37i68",
    "login_ucid": "2000000483989782",
    "lianjia_token": "2.001501372d407143d704ac1e1c08525b3e",
    "lianjia_token_secure": "2.001501372d407143d704ac1e1c08525b3e",
    "security_ticket": "QXhh3ylzYI2iD7B2NIsOX25z/OgW7NF6Nn8BHUGdHXGRE79lEAAS3FUSGQC9qCo65o5zJEnBsWbzP0vkOwYKr9rMgCfc6pM/7LQ6yDGNeH46EHHDQCqxQ+fOla4GJYbJvW6ywukMFKFGNld+/AQwJh78USSLnbyxtiXOZZ+Dcd0=",
    "ftkrc_": "5ad16c34-4edd-4acc-a483-862e69a42873",
    "lfrc_": "a6756296-b998-45e3-a576-3c3f3ebf1db8",
    "Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610": "1747752105",
    "srcid": "eyJ0Ijoie1wiZGF0YVwiOlwiZWQzMTVmODNiYmNlYTJlMTk2NmY4YzA2MGQ0NGQ0ZWRkM2RkOGMxMjIyNTk0ZjdlZDQ4MzlmODJmNmNjYmJhNzM5NDI2M2M5YzE2YTBiNjFjNTdhODc2NGJlZWZjYzg5M2YzOTQwNmYyYjE2MmYyNDcxOTNkMDllOGE5MGQ4ZGE3NDBhNzQyMTZhNDIwYTUxYzRhZGE0MjdkYWE4NjViYjE4M2M4MzQxMDYxODYyNTlhNmM2ZTUxYmE4ODczYzRkMWJlZjBiNGViOGQ2OGNhZmRhNGYyYTU0OWFkNzUyMzU5ZjYxY2U2OWEzMzNkMzBjYzE3YWM2MTc2NzBlM2ExMTEyODBkMDkxNTY5ZGZkZTE4MWNkYzdkN2FlMDliZDk5NjdiN2ViNDAzYTJiNjZkMDA3MzI2YjU3MzY2NDA1NGJcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiZThlYmYxMmZcIn0iLCJyIjoiaHR0cHM6Ly94ei5rZS5jb20vZXJzaG91ZmFuZy9wZzMwcnMlRTYlOTYlQjAlRTUlOUYlOEUlRTUlOEMlQkEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=",
    "hip": "J3hy4uIjd89oaqqkTDFYYcngCEzPvgq9JO2HJcav7AahbzsCCrmX5L93ncdZn4uF3PdOPU5ghLQ7tWSKvFKWEBnZJAGO5eM5ic_wO5zksAvj7SLJn3Ti1zHdHpDNe8POhQL5e0fbymUQy1x-L0hJlD2OpgZtjTkboy16qbmri7ltAHDMuMA%3D"
}
for i in range(53, 61):
    print(f'当前爬取第{i}页')
    url = f"https://xz.ke.com/chengjiao/pg{i}rs%E6%96%B0%E5%9F%8E%E5%8C%BA/"
    response = requests.get(url, headers=headers, cookies=cookies)
    # print(response.text)
    tree = etree.HTML(response.text)
    title = tree.xpath('.//div[@class="title"]/text()')[0]
    if str(title).__eq__("人机验证"):
        print('触发验证码了!')
        break
    listContents = tree.xpath('//ul[@class="listContent"]')
    count = 0
    for listContent in listContents:
        hrefs = listContent.xpath('./li/a/@href')
        for href in hrefs:
            # count += 1
            # if count <= 25:
            #     continue
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
            location = '新城区'
            response = requests.get(href, headers=headers, cookies=cookies)
            time.sleep(wait_time)
            tree = etree.HTML(response.text)
            title = tree.xpath('.//div[@class="title"]/text()')[0]
            if str(title).__eq__("人机验证"):
                print('触发验证码了!')
                break
            mains = tree.xpath('.//div[@class="content"]/div[@class="title"]/h1[@class="main"]/text()')
            deal_dates = tree.xpath('.//div[@class="content"]/div[@class="title"]/h1[@class="main"]/strong/text()')
            info_frs = tree.xpath('.//div[@class="info fr"]')
            bases = tree.xpath('.//div[@class="base"]')
            transactions = tree.xpath('.//div[@class="transaction"]')
            for main in mains:
                title = re.sub(r'\n\s{2,}', '', main)
                if title == '':
                    continue
                community_name = str(title).split(" ")[0]
            for deal_date in deal_dates:
                deal_date = str(deal_date.strip()).split(" ")[0]
            for info_fr in info_frs:
                deal_cycle = info_fr.xpath('./div[@class="msg"]/span[2]/label/text()')[0]
                deal_cycle = re.sub(r'[\n\s]+', '', deal_cycle)
                avg_price = info_fr.xpath('./div[@class="price"]/b/text()')[0]
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
                    if '建筑面积' in base_span_list:
                        area = li_base
                    elif '建成年代' in base_span_list:
                        build_year = li_base
                    elif '房屋户型' in base_span_list:
                        house_type = li_base
                    elif '房屋朝向' in base_span_list:
                        house_direction = li_base
                    elif '装修情况' in base_span_list:
                        house_decoration_status = li_base
                    elif '建筑类型' in base_span_list:
                        building_type = li_base
                    elif '建筑结构' in base_span_list:
                        building_structure = li_base
                    elif '配备电梯' in base_span_list:
                        has_elevator = li_base
                    elif '所在楼层' in base_span_list:
                        floor = li_base
            for transaction in transactions:
                house_usage = transaction.xpath('./div[@class="content"]/ul/li[4]/text()')[0]
            try:
                sql = """INSERT INTO bk (
                    location, page, community_name, area, avg_price, deal_date, deal_cycle, 
                    build_year, house_type, house_direction, house_decoration_status, 
                    building_type, building_structure, has_elevator, floor, house_usage
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (
                    str(location), str(i), str(community_name), area, avg_price, deal_date,
                    deal_cycle, build_year, house_type, house_direction, house_decoration_status,
                    building_type, building_structure, has_elevator, floor, house_usage
                )
                cursor.execute(sql, val)
                db.commit()
            except Exception as e:
                print(e)

