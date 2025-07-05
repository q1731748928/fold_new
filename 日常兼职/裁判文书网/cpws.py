import json
import random
import time

import execjs
import requests
import pymysql
# 打开数据库连接
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="part_time_job")
cursor = db.cursor()
# 使用 cursor() 方法创建一个游标对象 cursor


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
    "Referer": "https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=3da744f65ad50f45840a9165583596a5&s21=%E7%9B%97%E7%AA%83&s8=02&s9=0201&s6=01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}
cookies = {
    "wzws_sessionid": "gjZmNjkwMYE1YjJiYTSgaEVx2oAxMTUuMjA0Ljc2LjIzMQ==",
    "SESSION": "f4a4fa38-f71b-4f9f-a3cc-9929a0faa680",
    "wzws_cid": "9d369f27fd05f341ddab43cdee5d2b0917edb320e2961230c0c94626da51f337f4133e5682f884622aba56da58bb7b51e6aec3f0edc32bb13706733d0e9ce385bec676cc28ffa3252e1d1a5d7b3344a7"
}

def find_exist(comment):
    # 假设我们要检查的用户名

    # SQL 查询语句，检查 username 是否存在
    query = "SELECT COUNT(*) FROM cpws WHERE title = %s;"

    # 执行查询
    cursor.execute(query, (comment,))

    # 获取查询结果
    result = cursor.fetchone()

    # 如果查询结果大于0，说明该用户名已经存在
    return result[0]

def get_detail(docId):
    data = {
        "docId": str(docId),
        "ciphertext": "1100010 111000 110101 1111001 1011010 1101001 1101101 1110010 1110110 1000111 1001101 1001011 1101000 1001011 1000011 1010000 110011 110011 1010001 1110001 1000111 1100001 1000011 110110 110010 110000 110010 110101 110000 110110 110000 111000 1100101 1000011 1101011 1001111 1000011 1011000 1001110 1000101 1001100 1010111 1010011 110010 1010100 110110 110100 110001 1010101 1001110 1000101 1011001 1011000 1000001 111101 111101",
        "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch",
        "__RequestVerificationToken": "w4Fun1lHVGrC1p25f1VtRtAM",
        "wh": "944",
        "ww": "1728",
        "cs": "0"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    # print(response.text)
    secretKey = response.json()['secretKey']
    result = response.json()['result']
    ctll = execjs.compile(open('cpws.js', encoding='utf-8').read())
    decrypt_result = ctll.call('decrypt', result, secretKey)
    # print(decrypt_result)
    js = json.loads(decrypt_result)
    return js


url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
ctll = execjs.compile(open('cpws.js', encoding='utf-8').read())
cipher = ctll.call('get_cipher')
for i in range(21, 22):
    url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
    data = {
        "pageId": "e6fe1417aab7a9187433a493985997cc",
        "s21": "盗窃",
        "s16": "刑事案由",
        "s11": "1",
        "s8": "02",
        "s9": "0201",
        "s6": "01",
        "sortFields": "s50:desc",
        "ciphertext": "1001000 1011001 110001 1100110 1100100 1111001 1111010 1100111 1001000 1100101 1001110 1010001 111000 1001011 1101111 1100111 1010010 1000110 1011000 1101011 1101011 110010 111001 1001100 110010 110000 110010 110101 110000 110110 110000 111000 1110101 1101100 1111010 110101 110110 1010101 110111 1100100 1011000 1010010 1101000 1110001 1010110 1000001 1000111 1011000 110001 1110111 1100111 1110100 1101110 1110111 111101 111101",
        "pageNum": str(i),
        "queryCondition": "[{\"key\":\"s21\",\"value\":\"盗窃\"},{\"key\":\"s11\",\"value\":\"1\"},{\"key\":\"s8\",\"value\":\"02\"},{\"key\":\"s9\",\"value\":\"0201\"},{\"key\":\"s6\",\"value\":\"01\"},{\"key\":\"s39\",\"value\":\"R10\"},{\"key\":\"s42\",\"value\":\"2024\"}]",
        "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc",
        "__RequestVerificationToken": "pBkWhWxbaFO5OSlrHl98XK3P",
        "wh": "944",
        "ww": "1728",
        "cs": "0"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    time.sleep(3)
    # print(response.text)
    # wait_time = random.uniform(30, 60)
    # time.sleep(wait_time)
    secretKey = response.json()['secretKey']
    result = response.json()['result']
    ctll = execjs.compile(open('cpws.js', encoding='utf-8').read())
    decrypt_result = ctll.call('decrypt', result, secretKey)
    js = json.loads(decrypt_result)
    print(js)
    resultLists = js['queryResult']['resultList']
    for resultList in resultLists:
        # print(resultList)
        title = resultList.get("1")
        result = find_exist(title)
        if result < 0:
            print(f"当前信息已存在：{title}")
            continue
        else:
            case_num = resultList.get("7")
            date = resultList.get("31")
            row_key = resultList.get("rowkey")
            # print(f"row_key:{row_key}")
            detail = get_detail(row_key)
            # print(f"detail:{detail}")
            time.sleep(3)
            # print(str(i), str(title), str(case_num), str(date))
            try:
                sql = "INSERT INTO cpws (pg, detail, doc_id, title, case_num, date) VALUES (%s, %s, %s, %s, %s,%s)"
                val = (i, str(detail), row_key, title, case_num, date)
                cursor.execute(sql, val)
                db.commit()
            except Exception as e:
                print(e)