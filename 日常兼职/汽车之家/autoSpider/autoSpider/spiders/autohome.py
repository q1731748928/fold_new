import scrapy
import pymysql
import json

from scrapy import cmdline


class AutohomeSpider(scrapy.Spider):
    name = 'AutohomeSpider'
    allowed_domains = ['autohome.com.cn']
    start_urls = [
        'https://car-web-api.autohome.com.cn/car/search/searchcar?searchtype=5&pageindex=0&pagesize=30&orderid=0&state=2'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 3,  # 防止被封
    }

    def __init__(self, *args, **kwargs):
        super(AutohomeSpider, self).__init__(*args, **kwargs)
        self.db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="car_info")
        self.cursor = self.db.cursor()

    def parse(self, response):
        result = json.loads(response.text)['result']
        seriescount = result.get('seriescount')
        total_pages = int(seriescount / 30) + 2

        for index in range(1, total_pages):
            url = f'https://car-web-api.autohome.com.cn/car/search/searchcar?searchtype=5&pageindex={index}&pagesize=30&orderid=0&state=2'
            yield scrapy.Request(url, callback=self.parse_seriesgroup)

    def parse_seriesgroup(self, response):
        seriesgrouplist = json.loads(response.text)['result']['seriesgrouplist']

        for seriesgroup in seriesgrouplist:
            seriesid = seriesgroup['seriesid']
            seriesname = seriesgroup['seriesname']
            url = f'https://car-web-api.autohome.com.cn/car/param/getParamConf?mode=1&site=1&seriesid={seriesid}'
            yield scrapy.Request(url, callback=self.save_to_db, meta={'seriesid': seriesid, 'seriesname': seriesname})

    def save_to_db(self, response):
        seriesid = response.meta['seriesid']
        seriesname = response.meta['seriesname']
        result = json.loads(response.text)['result']
        json_string = json.dumps(result, ensure_ascii=False)

        try:
            sql = "insert INTO car_model VALUES (%s, %s, %s)"
            val = (seriesid, seriesname, json_string)
            self.cursor.execute(sql, val)
            self.db.commit()
        except Exception as e:
            self.logger.error(f"Error: {e}")

    def close(self, reason):
        self.db.close()


if __name__ == '__main__':
    cmdline.execute('scrapy crawl AutohomeSpider'.split())