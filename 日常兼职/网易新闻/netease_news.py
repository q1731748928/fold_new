import csv

import requests
from lxml import etree
import pymongo

client_mongo = pymongo.MongoClient(host='localhost', port=27017)
db = client_mongo['spider']['netease']

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://news.163.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "__root_domain_v": ".163.com",
    "_qddaz": "QD.378023852986324",
    "_ntes_nuid": "3d3eb1bed2d4bd713dfe3ebc47df749a",
    "ne_analysis_trace_id": "1746776847219",
    "_ntes_origin_from": "",
    "UserProvince": "%u5168%u56FD",
    "_antanalysis_s_id": "1746779287531",
    "s_n_f_l_n3": "98332b8ef3bf36b21746784522391",
    "pgr_n_f_l_n3": "f5578ec00ca93f7d17467768472194557",
    "vinfo_n_f_l_n3": "98332b8ef3bf36b2.1.1.1746776847220.1746781036354.1746785041567"
}
url = "https://sports.163.com/"
response = requests.get(url, headers=headers, cookies=cookies)
count = 0
tree = etree.HTML(response.text)
lists = tree.xpath('//div[@class="channel_news_list"]')
data = []
for list in lists:
    hrefs = list.xpath('./ul/li/a/@href')
    for href in hrefs:
        count += 1
        if count >= 501:
            break
        else:
            response = requests.get(href, headers=headers, cookies=cookies)
            tree = etree.HTML(response.text)
            # 正文中心
            mains = tree.xpath('//div[@class="post_main"]')
            for main in mains:
                # 新闻标题
                title = main.xpath('./h1[@class="post_title"]/text()')[0]
                # 发布时间
                date = str(main.xpath('./div[@class="post_info"]/text()')[0]).strip().replace("来源:", "")
                # 新闻来源
                source = main.xpath('./div[@class="post_info"]/a/text()')[0]
                # 发生地
                location = str(main.xpath('./div[@class="post_info"]/img/following-sibling::text()')[0]).strip()
            # 文章数
            span1 = tree.xpath('//div[@class="post_wemedia_info"]/span[1]/a/em/text()')[0]
            # 关注度
            span2 = tree.xpath('//div[@class="post_wemedia_info"]/span[2]/a/em/text()')[0]
            item = dict()
            item['title'] = title
            item['date'] = date
            item['source'] = source
            item['location'] = location
            item['article_count'] = span1
            item['focus_count'] = span2
            data.append([title, date, source, location, span1, span2])
            db.insert_one(item)
# 打开 CSV 文件进行写入
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入 CSV 文件的表头
    writer.writerow(['title', 'date', 'source', 'location', 'article_count', 'focus_count'])
    # 写入每一行数据
    writer.writerows(data)

# db.client_mongo.close()
