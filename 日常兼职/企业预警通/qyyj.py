import json
import random
import re
import time

import pymysql
import requests
import xlrd

session = requests.session()
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="qyyjt")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
def read_excel():
    # 打开Excel文件
    file_path = '/Users/hejie/PycharmProjects/turing_exec/日常兼职/企业预警通/2024.06在建工程.xls'
    workbook = xlrd.open_workbook(file_path)

    # 获取第一个工作表
    sheet = workbook.sheet_by_index(0)
    # 读取从第18行到第1153行的数据
    data = []
    for row_idx in range(953, 1153):  # 注意这里是从第18行，索引是从0开始的
        row = sheet.row_values(row_idx)
        data.append(row)

    excluded_keywords = ['政府', '大学', '中心', '局', '——']
    # 使用字典来实现去重且有序
    company_dict = {}
    # 循环遍历 rows，并将每行的 company_name 添加到字典中
    for row in data:
        company_name = row[1]
        if not any(keyword in company_name for keyword in excluded_keywords):
            company_dict[company_name] = None

    return company_dict

def find_exist(comment):
    # 假设我们要检查的用户名

    # SQL 查询语句，检查 username 是否存在
    query = "SELECT COUNT(*) FROM qyyjt WHERE company_name = %s;"

    # 执行查询
    cursor.execute(query, (comment,))

    # 获取查询结果
    result = cursor.fetchone()

    # 如果查询结果大于0，说明该用户名已经存在
    return result[0]
def get_refresh_token():
    headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "client": "pc-web;pro",
            "dataid": "9999900005",
        "pcuss": 'eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiand0IiwiYWxnIjoiSFMyNTYifQ.eyJjcmVhdGVUaW1lIjoiMjAyNS0wNC0yOSAxMTo1NTo1My4yNzgiLCJleHAiOjE3NDU4OTk4NTMsInVzZXJJZCI6IjIwMjUwNDI3MTA1MjUzXzE4OTM5NjYyMTg5IiwiZXhwaXJlZFRpbWUiOiIyMDI1LTA0LTI5IDEyOjEwOjUzLjI3OCJ9.iDr1rDO9ZoKQaMps4kzQ9HFnOWFFjuYJyJYbtlbk8oI',
        "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.qyyjt.cn/s?tab=securities&k=%E5%AE%9D%E9%92%A2%E6%B9%9B%E6%B1%9F%E9%92%A2%E9%93%81%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "system": "new",
            "system1": "Macintosh; Intel Mac OS X 10_15_7;Chrome;135.0.0.0",
            "terminal": "pc-web;pro",
            "user": "BFF37120F39EF5801824287C4E4D754F30399020310E152F8C10EE812CB1BCCB",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "ver": "20250424",
        }
    url = "https://www.qyyjt.cn/getData.action"
    params = {
            "_t": "9999900005"
    }
    response = session.get(url, headers=headers, params=params)
    info = response.json()['info']
    if info == 'success':
        print("刷新token成功")
        params = {
            "_t": "9999900082"
        }
        response = requests.get(url, headers=headers, params=params)
        info = response.json()['info']
        if info == 'success':
            print("操作成功")
            url = "https://www.qyyjt.cn/finchinaAPP/getServerDate.action"
            response = requests.get(url, headers=headers)
            returncode = response.json()['returncode']
            if returncode == 0:
                print('请求服务器成功')
            else:
                print('请求服务器失败')
                return "fail"
        else:
            return "fail"
    else:
        return "fail"


wait_time = random.uniform(1, 3)
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "client": "pc-web;pro",
    "pcuss": 'eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiand0IiwiYWxnIjoiSFMyNTYifQ.eyJjcmVhdGVUaW1lIjoiMjAyNS0wNC0yOSAxMTo1NTo1My4yNzgiLCJleHAiOjE3NDU4OTk4NTMsInVzZXJJZCI6IjIwMjUwNDI3MTA1MjUzXzE4OTM5NjYyMTg5IiwiZXhwaXJlZFRpbWUiOiIyMDI1LTA0LTI5IDEyOjEwOjUzLjI3OCJ9.iDr1rDO9ZoKQaMps4kzQ9HFnOWFFjuYJyJYbtlbk8oI',
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.qyyjt.cn/s?tab=securities&k=%E4%B8%AD%E5%9B%BD%E6%B5%B7%E5%A4%96%E5%B7%A5%E7%A8%8B%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8%E6%AF%9B%E5%A1%94%E5%88%86%E5%85%AC%E5%8F%B8",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "system": "new",
    "system1": "Macintosh; Intel Mac OS X 10_15_7;Chrome;135.0.0.0",
    "terminal": "pc-web;pro",
    "user": "BFF37120F39EF5801824287C4E4D754F30399020310E152F8C10EE812CB1BCCB",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "ver": "20250424",
    "x-request-id": "OpmzHXATyyyvnOZnoi2rs",
    "x-request-url": "%2Fs%3Ftab%3Dsecurities%26k%3D%25E4%25B8%25AD%25E5%259B%25BD%25E6%25B5%25B7%25E5%25A4%2596%25E5%25B7%25A5%25E7%25A8%258B%25E6%259C%2589%25E9%2599%2590%25E8%25B4%25A3%25E4%25BB%25BB%25E5%2585%25AC%25E5%258F%25B8%25E6%25AF%259B%25E5%25A1%2594%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8"
}
url = "https://www.qyyjt.cn/finchinaAPP/v1/finchina-search/v1/multipleSearch"
company_dict = read_excel()
for company_name in company_dict.keys():
    if company_name != '' and company_name != None:
        result = find_exist(company_name)
        if result > 0:
            if result > 0:
                print("当前信息已存在")
                continue
        else:
            info = get_refresh_token()
            print(f'info：{info}')
            if info == 'success' or info == None:
                print("刷新token成功")
            else:
                print("刷新token失败")
                break
            # 公司code
            code = '——'
            # 评级
            main_rating = '——'
            # 全部债权
            all_creditors_right = '——'
            # 存续债权
            continuous_creditors_right = '——'
            params = {
                "skip": "0",
                "text": str(company_name),
                "template": "list"
            }
            response = session.get(url, headers=headers, params=params)
            print('公司名称是:' + company_name)
            lists = response.json()['data']['list']
            # 公司信息不存在
            if len(lists) == 0:
                try:
                    print(company_name, code, main_rating, all_creditors_right, continuous_creditors_right)
                    sql = "INSERT INTO qyyjt (company_name, code, main_rating, all_creditors_right, continuous_creditors_right) VALUES (%s, %s, %s, %s, %s)"
                    val = (company_name, code, main_rating, all_creditors_right, continuous_creditors_right)
                    cursor.execute(sql, val)
                    db.commit()
                    break
                except Exception as e:
                    print(e.args)
                continue
            else:
                code = lists[0]['code']
                url = "https://www.qyyjt.cn/getData.action"
                headers['dataid'] = "434"
                params = {
                    "type": "company",
                    "code": str(code),
                    "isContinuous": "1",
                    "_t": str(headers['dataid'])
                }
                response = session.get(url, headers=headers, params=params)
                time.sleep(wait_time)
                data = response.json()['data']
                if 'mainRating' in data:
                    if data.get('') != None or data.get('mainRating') != '':
                        main_rating = data['mainRating']
                # 全部债权
                headers['dataid'] = "441"
                params = {
                            "code": str(code),
                            "type": "company",
                            "skip": "0",
                            "isContinuous": "1,2",
                            "company_type": "current",
                            "module_type": "web_f9_bond_financing",
                            "dynamicIndex": "BD0201_046,isPerpetualBond,isGreenLabel,isNotGreenLabel,BD0002_084,BD0002_020,BD0002_016,BD0002_017,BD0002_018,BD0002_012,BD0201_045,BD0051_009,BD0051_004,BD0201_064,BD0201_006,BD0201_042,debtor,guarantor,BD0285_009,BD0285_004,fxlc",
                            "branchCompany": "self",
                            "_t": "441"
                }
                response = session.get(url, headers=headers, params=params)
                time.sleep(wait_time)
                data = json.loads(response.text)
                if 'message' in data['data']:
                    message = response.json()['data']['message']
                    print(message)
                    # 匹配债券数量
                    count_pattern = r'债券(\d+)只'
                    count_match = re.search(count_pattern, message)
                    if count_match:
                        count = count_match.group(1)
                        if int(count) > 0:
                            all_creditors_right = count
                    else:
                        print("未找到债券数量信息。")

                # 匹配存量规模
                params['isContinuous'] = '1'
                response = session.get(url, headers=headers, params=params)
                data = json.loads(response.text)
                if 'message' in data['data']:
                    scale_pattern = r'债券存量规模(\d+\.?\d*)亿元'
                    scale_match = re.search(scale_pattern, message)
                    if scale_match:
                        scale = float(scale_match.group(1))
                        if scale > 0.00:
                            print(f"债券存量规模: {scale}亿元")
                            continuous_creditors_right = f'{scale}亿元'
                        else:
                            print("债券存量规模为 0.00 亿元，不输出。")
                else:
                    print("未找到债券存量规模信息。")
                try:
                    print(company_name, code, main_rating, all_creditors_right, continuous_creditors_right)
                    sql = "INSERT INTO qyyjt (company_name, code, main_rating, all_creditors_right, continuous_creditors_right) VALUES (%s, %s, %s, %s, %s)"
                    val = (company_name, code, main_rating, all_creditors_right, continuous_creditors_right)
                    cursor.execute(sql, val)
                    db.commit()
                    break
                except Exception as e:
                    print(e.args)



