import ast
import json
import random
import re
import time

import execjs
import pymysql
import requests

wait_time = random.uniform(1, 3)

def set_headers(data):
    with open('./gj.js', encoding='utf-8') as f:
        js_code = f.read()
    ctll = execjs.compile(js_code)
    result = ctll.call("get_data", data)
    headers['X-Dgi-Req-App'] = str(result.get('X-Dgi-Req-App'))
    headers['X-Dgi-Req-Nonce'] = str(result.get('X-Dgi-Req-Nonce'))
    headers['X-Dgi-Req-Signature'] = str(result.get('X-Dgi-Req-Signature'))
    headers['X-Dgi-Req-Timestamp'] = str(result.get('X-Dgi-Req-Timestamp'))
    headers['X-Dgi-Req-Signatures'] = str(result.get('X-Dgi-Req-Signatures'))
    return headers

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://zbtb.gd.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "X-Dgi-Req-App": "ztbjg-portal",
    "X-Dgi-Req-Nonce": "owJQpxZdY2ftR2E2",
    "X-Dgi-Req-Signature": "993a0537cdac6b7298856a39bf482a26fff3e5cc506d958b23e81eb925b51702",
    "X-Dgi-Req-Signatures": "9246f0e1113ccc79a55861e9a37bc4ba286f1fb35aa83bb0e822ad6507a191b3",
    "X-Dgi-Req-Timestamp": "1747301755368",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
    "openstack_cookie_insert": "16275321",
    "_horizon_sid": "a319e773-1b55-49fc-83fe-826d9b64ab59"
}

# 连接到MySQL数据库
db_connection = pymysql.connect(
    host="localhost",          # MySQL 主机
    user="root",          # 用户名
    password="Q2893962404t@",  # 密码
    database="part_time_job"   # 数据库名称
)

# 创建一个游标对象来执行查询
cursor = db_connection.cursor()

# 执行查询以获取所有的 id 和 result_list
query = "SELECT keyword, result_type, project_code, trading_process, site_code, notice_id, notice_title FROM gzztb where id > 95986"
cursor.execute(query)

batch_size = 500  # Number of rows to insert at once
batch_data = []  # List to collect data for batch insertion
# 获取所有查询结果
results = cursor.fetchall()

# 打印每一行的 id 和 result_list
for row in results:
    start = time.time()
    keyword = row[0]
    result_type = row[1]
    project_code = row[2]
    trading_process = row[3]
    site_code = row[4]
    notice_id = row[5]
    title = row[6]
    # url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/detail" 中标候选人公示
    url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/detail"  # 招标结果
    o = {
        "data": {
            "projectCode": project_code,
            "tradingType": "A",
            "tradingProcess": trading_process,
            "siteCode": site_code,
        }
    }

    set_headers(o)
    response = requests.get(url, headers=headers, cookies=cookies, params=o.get('data'))
    time.sleep(wait_time)
    data = response.text

    # Add the data to the batch list
    batch_data.append((keyword, project_code, result_type, trading_process, site_code, data, notice_id, title))

    # If the batch reaches the specified size, insert the batch into the database
    if len(batch_data) >= batch_size:
        try:
            sql = """
                INSERT INTO gzztb_detail (keyword, project_code, result_type, trading_process, site_code, data, notice_id, title)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.executemany(sql, batch_data)
            db_connection.commit()
            print(f"Inserted {len(batch_data)} rows.")
            end_time = time.time()
            print(f"Total time taken: {end_time - start}")
            # Clear the batch data after insertion
            batch_data.clear()
        except Exception as e:
            print(f"Error inserting batch: {e.args}")

# Insert any remaining data in the batch (less than batch_size)
if batch_data:
    try:
        sql = """
            INSERT INTO gzztb_detail (keyword, project_code, result_type, trading_process, site_code, data, notice_id, title)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(sql, batch_data)
        db_connection.commit()
        end_time = time.time()
        print(f"Inserted {len(batch_data)} remaining rows.")
    except Exception as e:
        print(f"Error inserting remaining batch: {e.args}")

print('程序结束退出!')
# 关闭游标和数据库连接
# Inserted 500 rows.
# Total time taken: 960.0427029132843