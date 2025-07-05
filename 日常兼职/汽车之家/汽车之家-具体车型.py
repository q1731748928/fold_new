import json
import time

import pymysql
import requests

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="car_info")
cursor = db.cursor()
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.autohome.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.autohome.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://car-web-api.autohome.com.cn/car/search/searchcar"
params = {
            "searchtype": "5",
            "pageindex": 0,
            "pagesize": "30",
            "orderid": "0",
            "state": "2"
        }
result = requests.get(url, headers=headers, params=params).json()['result']
# 1491
seriescount = result.get('seriescount')
print(seriescount)
for index in range(1, int(seriescount / 30) + 2):
    params = {
        "searchtype": "5",
        "pageindex": index,
        "pagesize": "30",
        "orderid": "0",
        "state": "2"
    }
    seriesgrouplist = requests.get(url, headers=headers, params=params).json()['result']['seriesgrouplist']
    time.sleep(3)
    for seriesgroup in seriesgrouplist:
        seriesid = seriesgroup['seriesid']
        seriesname = seriesgroup['seriesname']
        url = "https://car-web-api. /car/param/getParamConf"
        params = {
            "mode": "1",
            "site": "1",
            "seriesid": seriesid
        }
        result = requests.get(url, headers=headers, params=params).json()['result']
        time.sleep(3)
        json_string = json.dumps(result, ensure_ascii=False)
        try:
            sql = "insert INTO car_model VALUES (%s, %s, %s)"
            val = (seriesid, seriesname, json_string)
            cursor.execute(sql, val)
            db.commit()
        except Exception as e:
            print(e)

db.close()