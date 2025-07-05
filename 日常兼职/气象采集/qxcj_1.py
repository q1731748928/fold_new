import time

import pymysql
from openpyxl.reader.excel import load_workbook

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="qxcj")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

import execjs
import requests

# 要用自己的cookie
cookies = {
    'Hm_lvt_6088e7f72f5a363447d4bafe03026db8': '1704421259',
    'Hm_lpvt_6088e7f72f5a363447d4bafe03026db8': '1704422591',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://www.aqistudy.cn/historydata/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

city = '北京'
# 读取js代码，构造js执行环境
with open("qxcj.js", 'r', encoding='utf-8') as f:
    js_code = f.read()
env = execjs.compile(js_code)
query = env.call("gethistory", city)
data = {
    'hA4Nse2cT': query
}
response = requests.post('https://www.aqistudy.cn/historydata/api/historyapi.php', cookies=cookies, headers=headers,
                         data=data)
time.sleep(5)
encrypted_data = response.text
result = (env.call("get_data", encrypted_data))
items = result['result']['data']['items']
for item in items:
    time_point = item.get('time_point')
    aqi = item.get('aqi')
    max_aqi = item.get('max_aqi')
    min_aqi = item.get('min_aqi')
    pm2_5 = item.get('pm2_5')
    pm10 = item.get('pm10')
    co = item.get('co')
    no2 = item.get('no2')
    o3 = item.get('o3')
    so2 = item.get('so2')
    so2 = item.get('so2')
    rank = item.get('rank')
    quality = item.get('quality')
    range = f'{min_aqi}~{max_aqi}'
    print(
        f"{city} {time_point} {aqi} {max_aqi} {min_aqi} {range} {pm2_5} {pm10} {co} {no2} {o3} {so2} {rank} {quality}")
    # try:
    #     sql = "INSERT INTO qxcj (city, time_point, aqi, max_aqi, min_aqi, pm2_5, pm10, co, no2, o3, so2, quality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    #     val = (city, time_point, aqi, max_aqi, min_aqi, pm2_5, pm10, co, no2, o3, so2, quality)
    #     cursor.execute(sql, val)
    #     db.commit()
    # except Exception as e:
    #     print(e.args)
