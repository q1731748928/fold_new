import base64
import json
import random
import time

import pymysql
import requests
import execjs
import ddddocr

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="part_time_job")
cursor = db.cursor()
wait_time = random.uniform(1, 3)

# 公
# 评
# 侯
# 项
# 包
# 设
# 工
# 监
# 咨

class ZbtbCaptchaSolver:
    def __init__(self, js_file="gj.js", check_js_file="get_postjson.js"):
        self.js_file = js_file
        self.check_js_file = check_js_file
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://zbtb.gd.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://zbtb.gd.gov.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "X-Dgi-Req-App": "ztbjg-portal",
            "X-Dgi-Req-Nonce": "501iFRjEQQHS5pyI",
            "X-Dgi-Req-Signature": "7213e168b97756018563bca8660a7d6755ffcf8d93a4fb21344999f7a2dc13e5",
            "X-Dgi-Req-Signatures": "58503fdbc59a6ccaafc833d549deb4299fb055f04494d8c71974a7406ce78989",
            "X-Dgi-Req-Timestamp": "1747125880919",
            "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.cookies = {
            "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
            "openstack_cookie_insert": "97258147",
            "_horizon_sid": "ca7b5dd5-2b22-4778-a341-354e4c046852"
        }

    def set_headers(self, data):
        with open(self.js_file, encoding='utf-8') as f:
            js_code = f.read()
        ctll = execjs.compile(js_code)
        result = ctll.call("get_data", data)

        self.headers['X-Dgi-Req-App'] = str(result.get('X-Dgi-Req-App'))
        self.headers['X-Dgi-Req-Nonce'] = str(result.get('X-Dgi-Req-Nonce'))
        self.headers['X-Dgi-Req-Signature'] = str(result.get('X-Dgi-Req-Signature'))
        self.headers['X-Dgi-Req-Timestamp'] = str(result.get('X-Dgi-Req-Timestamp'))
        self.headers['X-Dgi-Req-Signatures'] = str(result.get('X-Dgi-Req-Signatures'))

    def get_captcha_images(self):
        url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/get"
        data = {"captchaType": "blockPuzzle"}
        self.set_headers(data)
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=data)

        originalImageBase64 = response.json()['data']['repData']['originalImageBase64']
        jigsawImageBase64 = response.json()['data']['repData']['jigsawImageBase64']
        secretKey = response.json()['data']['repData']['secretKey']
        token = response.json()['data']['repData']['token']

        image_data1 = base64.b64decode(originalImageBase64)
        image_data2 = base64.b64decode(jigsawImageBase64)
        with open('dd1.jpg', 'wb') as file1:
            file1.write(image_data1)
        with open('dd2.jpg', 'wb') as file2:
            file2.write(image_data2)
        return token, secretKey

    def solve_captcha(self, token, secretKey):
        with open('dd1.jpg', 'rb') as f:
            target_bytes = f.read()
        with open('dd2.jpg', 'rb') as f:
            background_bytes = f.read()

        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        Y = det.slide_match(background_bytes, target_bytes)['target'][0]

        with open(self.check_js_file, encoding='utf-8') as f:
            js_code = f.read()
        ctll = execjs.compile(js_code)
        pointJson = ctll.call("get_postjson", Y, secretKey)

        data = {
            "captchaType": "blockPuzzle",
            "pointJson": str(pointJson),
            "token": token
        }

        self.set_headers(data)
        check_url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/check"
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(check_url, headers=self.headers, cookies=self.cookies, data=data)
        return response.json()['data']['repData']['token']

    def search_notice(self, token, page_no, page_size, keyword):
        url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/notice/search"
        o = {
            "data": {
                "type": "trading-type",
                "publishStartTime": "",
                "publishEndTime": "",
                "keyword": keyword,
                "thirdType": 12,
                "siteCode": "44",
                "secondType": "A",
                "projectType": "",
                "dateType": "",
                "searchType": "pf",
                "pageNo": page_no,
                "pageSize": page_size,
                "openConvert": False
            }
        }
        self.set_headers(o)
        self.headers['Vtoken'] = token
        data = json.dumps(o.get('data'), separators=(',', ':'))
        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.text

    def find_exist(self, noticeId):
        # 假设我们要检查的用户名

        # SQL 查询语句，检查 username 是否存在
        query = "SELECT COUNT(*) FROM gzztb WHERE notice_id = %s;"

        # 执行查询
        cursor.execute(query, (noticeId,))

        # 获取查询结果
        result = cursor.fetchone()

        # 如果查询结果大于0，说明该用户名已经存在
        return result[0]


if __name__ == "__main__":
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
        "X-Dgi-Req-Nonce": "YxNE8UztuPiNpx6Z",
        "X-Dgi-Req-Signature": "f439803c5eee2454fb99eb242c0dd3108c48d7143ad1bfb37e1ac7e19f9eac0d",
        "X-Dgi-Req-Signatures": "b1843791b102343cf65a3be79056238c7cb6baf24780af27bc04381105f55248",
        "X-Dgi-Req-Timestamp": "1747130202020",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    cookies = {
        "_horizon_uid": "860eabf9-418b-4b8e-8bc5-61f7d4879d89",
        "_horizon_sid": "e4b59674-dcf7-4911-b2f7-bd2c4b5fe1c7",
        "openstack_cookie_insert": "16275321"
    }
    solver = ZbtbCaptchaSolver()
    i = 51
    keyword = '中'
    while True:
        i += 1
        token, secretKey = solver.get_captcha_images()
        token = solver.solve_captcha(token, secretKey)
        time.sleep(wait_time)
        result = solver.search_notice(token, i, 50, keyword)
        time.sleep(wait_time)
        js = json.loads(result)
        pageDatas = js['data']['pageData']
        if pageDatas == []:
            print('数据为空,程序退出')
            break
        for pageData in pageDatas:
            notice_id = pageData.get('noticeId')
            result = solver.find_exist(notice_id)
            if result > 0:
                if result > 0:
                    print("当前信息已存在")
                    continue
            else:
                notice_type = pageData.get('noticeType')
                notice_type_desc = pageData.get('noticeTypeDesc')
                notice_second_type = pageData.get('noticeSecondType')
                notice_second_type_desc = pageData.get('noticeSecondDesc')
                notice_third_type = pageData.get('noticeThird')
                notice_third_type_desc = pageData.get('noticeThirdDesc')
                project_type = pageData.get('projectType')
                project_type_name = pageData.get('projectTypeName')
                site_name = pageData.get('siteName')
                site_code = pageData.get('siteCode')
                region_code = pageData.get('regionCode')
                region_name = pageData.get('regionName')
                notice_title = pageData.get('noticeTitle')
                highlight_notice_title = pageData.get('highlightNoticeTitle')
                highlight_notice_content = pageData.get('highlightNoticeContent')
                link_url = pageData.get('linkUrl')
                publish_organ = pageData.get('publishOrgan')
                publish_way = pageData.get('publishWay')
                publish_date = pageData.get('publishDate')
                document_number = pageData.get('documentNumber')
                project_code = pageData.get('projectCode')
                create_at = pageData.get('createAt')
                publish_date = pageData.get('publishDate')
                if_result = pageData.get('ifResult')
                edition = pageData.get('edition')
                trading_process = pageData.get('tradingProcess')
                enact_date = pageData.get('enactDate')
                datetime = pageData.get('datetime')
                execute_date = pageData.get('executeDate')
                datetime = pageData.get('datetime')
                pub_service_plat = pageData.get('pubServicePlat')
                bidding_state = pageData.get('biddingState')
                bidding_state_desc = pageData.get('biddingStateDesc')
                data_source = pageData.get('dataSource')
                notice_nature = pageData.get('noticeNature')
                sql = """
                    INSERT INTO gzztb (
                        page_no, keyword, notice_id, notice_type, notice_type_desc,
                        notice_second_type, notice_second_type_desc, notice_third_type,
                        notice_third_type_desc, project_type, project_type_name, site_name,
                        site_code, region_code, region_name, notice_title, highlight_notice_title,
                        highlight_notice_content, link_url, publish_organ, publish_way,
                        document_number, project_code, create_at, publish_date, if_result,
                        edition, trading_process, enact_date, execute_date, pub_service_plat,
                        bidding_state, bidding_state_desc, data_source, notice_nature
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                """
                val = (
                    i, keyword, notice_id, notice_type, notice_type_desc, notice_second_type,
                    notice_second_type_desc, notice_third_type, notice_third_type_desc, project_type,
                    project_type_name, site_name, site_code, region_code, region_name, notice_title,
                    highlight_notice_title, highlight_notice_content, link_url, publish_organ, publish_way,
                    document_number, project_code, create_at, publish_date, if_result, edition, trading_process,
                    enact_date, execute_date, pub_service_plat, bidding_state, bidding_state_desc, data_source,
                    notice_nature
                )

                cursor.execute(sql, val)
                db.commit()
        #     siteCode = pageData.get('siteCode')
        #     url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/detail"
        #     params = {
        #         "projectCode": projectCode,
        #         "noticeId": noticeId,
        #         "tradingProcess": tradingProcess,
        #         "siteCode": siteCode
        #     }
        #     o = {
        #         "data": params
        #     }
        #     solver.set_headers(o)
        #     solver.headers['Vtoken'] = "0"
        #     response = requests.get(url, headers=solver.headers, cookies=solver.cookies, params=params)
        #     time.sleep(3)
        #     print(f'response:{response.text}')
