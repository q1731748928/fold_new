import random
import time

import execjs
import pymysql
import requests

# TODO 1. 更新有问题的data数据
# TODO 2. 更新有问题的notice_id后进行下载附件
wait_time = random.uniform(1, 3)
# 数据库查出noticeId，然后得到bidSectionCode 得到下载文件的id和文件类型，判断文件类型，如果是doc，则重命名docx，否则保留

# 连接到MySQL数据库
# 创建一个游标对象来执行查询
db_connection = pymysql.connect(
        host="localhost",  # MySQL 主机
        user="root",  # 用户名
        password="123456",  # 密码
        database="part_time_job"  # 数据库名称
    )
cursor = db_connection.cursor()
def get_file_id():
    # 执行查询以获取所有的 id 和 result_list
    query = "SELECT notice_id,bid_section_code FROM gzztb_detail where id > 80759 and data != '{\"errcode\":0,\"errmsg\":\"ok\",\"data\":[[]]}' and data != '{\"errcode\":0,\"errmsg\":\"ok\",\"data\":[]}'"
    cursor.execute(query)
    # 获取所有查询结果
    results = cursor.fetchall()
    # 打印每一行的 id 和 result_list
    for row in results:
        notice_id = row[0]
        bid_section_code = row[1]
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
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "X-Dgi-Req-App": "ztbjg-portal",
            "X-Dgi-Req-Nonce": "E1uJmuH7dJIbAs1e",
            "X-Dgi-Req-Signature": "f18e4be98bfe409a6875a86f92f34d10fbd493b4dd0b2936e59d67e5eeb571f0",
            "X-Dgi-Req-Signatures": "f905060f4e8a675faa59245f4562dbd83a29809b4e1b303b983e3a78a32e8dec",
            "X-Dgi-Req-Timestamp": "1748658735051",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        with open('./gj.js', encoding='utf-8') as f:
            js_code = f.read()
        ctll = execjs.compile(js_code)
        url = f"https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/his1/attachs"
        o = {
             "data": {
                "noticeId": str(notice_id),
                "parentType": "GGNR",
                "siteCode": "44"
}
                    }
        result = ctll.call("get_data", o)
        headers['X-Dgi-Req-App'] = str(result.get('X-Dgi-Req-App'))
        headers['X-Dgi-Req-Nonce'] = str(result.get('X-Dgi-Req-Nonce'))
        headers['X-Dgi-Req-Signature'] = str(result.get('X-Dgi-Req-Signature'))
        headers['X-Dgi-Req-Timestamp'] = str(result.get('X-Dgi-Req-Timestamp'))
        headers['X-Dgi-Req-Signatures'] = str(result.get('X-Dgi-Req-Signatures'))
        cookies = {
            "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
            "__jsluid_s": "d0af8236def3eba872f19902a8f35c15",
            "openstack_cookie_insert": "97258147",
            "_horizon_sid": "15173f2e-1379-49d3-8a6b-27445dcb610c"
        }
        # url = f"https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/file/{notice_id}"
        response = requests.get(url, headers=headers, cookies=cookies, params=o.get('data'))
        time.sleep(wait_time)
        print(response.text)
        js = response.json()
        datas = js.get('data')
        if datas == None or datas == []:
            print(f'notice_id:{notice_id},空数据跳过...')
            continue
        elif datas != None or datas != []:
            for data in datas:
                attachGuid = data['id']
                if bid_section_code == None:
                    bid_section_code = attachGuid
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
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                    "X-Dgi-Req-App": "ztbjg-portal",
                    "X-Dgi-Req-Nonce": "HTkXEGIVzYFuUGJJ",
                    "X-Dgi-Req-Signature": "948e136045f3074139f452c8a663a86904e02e02176f545fd9a0cd1931a7e7a1",
                    "X-Dgi-Req-Signatures": "a5a00d01059d6d2f6c73b14f3a2165378cf713a0addec564bd767b5ac6b88690",
                    "X-Dgi-Req-Timestamp": "1751322147890",
                    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"macOS\""
                }
                cookies = {
                    "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
                    "__jsluid_s": "d0af8236def3eba872f19902a8f35c15",
                    "openstack_cookie_insert": "16275321",
                    "_horizon_sid": "56846cc3-3f5d-4ead-a282-819238f16e30"
                }
                url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/his1/view-pdf"
                params = {
                    "attachId": str(attachGuid)
                }
                response = requests.get(url, headers=headers, cookies=cookies, params=params)
                # print(response.text)
                print(f'attachGuid:{attachGuid}')
                # print(response.text)
                time.sleep(wait_time)
                with open(f"./attach/{bid_section_code}.pdf", "wb") as f:
                    f.write(response.content)
                print(f'下载成功:{bid_section_code}.pdf')


if __name__ == '__main__':
     file = get_file_id()
