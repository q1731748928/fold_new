import json
import time

import execjs
import pymysql
import requests




db_connection = pymysql.connect(
    host="localhost",          # MySQL 主机
    user="root",          # 用户名
    password="123456",  # 密码
    database="part_time_job"   # 数据库名称
)

# 创建一个游标对象来执行查询
cursor = db_connection.cursor()

# 执行查询以获取所有的 id 和 result_list
query = "SELECT doc_id FROM cpws limit 1"
cursor.execute(query)
results = cursor.fetchall()

# def update_data():
#     sql = """
#             UPDATE gzztb_detail
#             SET detail = %s
#             WHERE project_code = %s
#         """
#     try:
#         start_time = time.time()
#         cursor.executemany(sql, batch_data)
#         db_connection.commit()
#         print(f"更新 {len(batch_data)} 行数据。")
#         end_time = time.time()
#         print(f"总耗时: {end_time - start_time}")
#     except Exception as e:
#         print(f"更新批次数据时出错: {e.args}")
#         db_connection.rollback()
#     finally:
#         cursor.close()

# 打印每一行的 id 和 result_list
for row in results:
    doc_id = row[0]
    headers = {
        "Host": "wenshu.court.gov.cn",
        "sec-ch-ua-platform": "\"macOS\"",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://wenshu.court.gov.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId={doc_id}",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }
    cookies = {
        "wzws_sessionid": "gTViMmJhNIAxMTUuMjA0Ljc2LjIzMaBoRMpQgjZmNjkwMQ==",
        "SESSION": "1bebc4c9-fe29-432f-90bf-d4f5a660b259",
        "wzws_cid": "271c3dfe173f905b2033dfd0df03a942c42396c3a5b9f5a8c6ffc5612093d5c9d9e5d64fbe07c234c73246a7b7af4e598da793bab4edf0b044cb6a02d39b4637f6406d5e2692f66198a8f5aa789b76b3"
    }
    url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
    data = {
        "docId": str(doc_id),
        "ciphertext": "1000101 1110000 1101100 1010000 1001001 1100110 1111000 110110 1100011 1011010 110110 1001001 110100 111001 1001100 110000 1110101 1110110 1000101 110110 1011000 110010 1001110 1100101 110010 110000 110010 110101 110000 110110 110000 111000 1101111 1110000 1000101 1000110 1000100 1010010 1000010 110000 101011 1001011 1100110 110010 1100010 1000111 1101101 1100010 1001100 101111 1010110 110001 110011 1010001 111101 111101",
        "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch",
        "__RequestVerificationToken": "6EPIKUE6SFtH2BLIq2x2Bxuo",
        "wh": "944",
        "ww": "1728",
        "cs": "0"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    time.sleep(3)
    print(response.text)
    secretKey = response.json()['secretKey']
    result = response.json()['result']
    ctll = execjs.compile(open('cpws.js', encoding='utf-8').read())
    decrypt_result = ctll.call('decrypt', result, secretKey)
    # print(decrypt_result)
    js = json.loads(decrypt_result)
    print(js)