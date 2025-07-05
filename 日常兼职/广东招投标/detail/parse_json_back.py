import ast
import json
import random
import re
import time

import execjs
import pymysql
import requests


def set_headers(data):
    with open('./gj.js', encoding='utf-8') as f:
        js_code = f.read()
    ctll = execjs.compile(js_code)
    result = ctll.call("get_data", data)
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
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    headers['X-Dgi-Req-App'] = str(result.get('X-Dgi-Req-App'))
    headers['X-Dgi-Req-Nonce'] = str(result.get('X-Dgi-Req-Nonce'))
    headers['X-Dgi-Req-Signature'] = str(result.get('X-Dgi-Req-Signature'))
    headers['X-Dgi-Req-Timestamp'] = str(result.get('X-Dgi-Req-Timestamp'))
    headers['X-Dgi-Req-Signatures'] = str(result.get('X-Dgi-Req-Signatures'))
    return headers


def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="part_time_job"
    )


def get_count(db_connection, data_value):
    cursor = db_connection.cursor()
    query = "SELECT count(1) FROM gzztb_detail WHERE data = %s"
    try:
        cursor.execute(query, (data_value,))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print(f"获取计数时出错: {e.args}")
        return 0
    finally:
        cursor.close()


def get_batch_data(db_connection, data_value, batch_size):
    cursor = db_connection.cursor()
    query = "SELECT notice_id, project_code FROM gzztb_detail WHERE data = %s LIMIT %s"
    try:
        cursor.execute(query, (data_value, batch_size))
        return cursor.fetchall()
    except Exception as e:
        print(f"获取批次数据时出错: {e.args}")
        return []
    finally:
        cursor.close()


def update_batch_data(db_connection, batch_data):
    cursor = db_connection.cursor()
    sql = """
        UPDATE gzztb_detail
        SET data = %s
        WHERE project_code = %s
    """
    try:
        start_time = time.time()
        cursor.executemany(sql, batch_data)
        db_connection.commit()
        print(f"更新 {len(batch_data)} 行数据。")
        end_time = time.time()
        print(f"总耗时: {end_time - start_time}")
    except Exception as e:
        print(f"更新批次数据时出错: {e.args}")
        db_connection.rollback()
    finally:
        cursor.close()


def main():
    data_value = '{"errcode":0,"errmsg":"ok","data":null}'
    batch_size = 500
    cookies = {
        "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
        "openstack_cookie_insert": "16275321",
        "_horizon_sid": "a319e773-1b55-49fc-83fe-826d9b64ab59"
    }

    db_connection = get_db_connection()
    total_count = get_count(db_connection, data_value)

    for count in range(1, (total_count + batch_size - 1) // batch_size + 1):
        batch_data = []
        results = get_batch_data(db_connection, data_value, batch_size)

        for row in results:
            notice_id = row[0]
            project_code = row[1]
            url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/detail"
            o = {
                "data": {
                    "projectCode": project_code,
                    "tradingType": "A",
                    "tradingProcess": "A010",
                    "siteCode": "44"
                }
            }
            headers = set_headers(o)
            try:
                response = requests.get(url, headers=headers, cookies=cookies, params=o.get('data'))
                response.raise_for_status()
                data = response.text
                batch_data.append((data, project_code))
            except requests.RequestException as e:
                print(f"请求 {url} 时出错: {e}")

            wait_time = random.uniform(1, 3)
            time.sleep(wait_time)
        if batch_data:
            update_batch_data(db_connection, batch_data)
    print('程序结束退出!')
    db_connection.close()


if __name__ == "__main__":
    main()