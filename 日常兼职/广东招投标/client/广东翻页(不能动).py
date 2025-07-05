import json
import subprocess
import requests
from urllib.parse import urlencode
import os
import time
import random
# -------------------- 通用工具函数 --------------------
'''把json参数变成字符串'''
def generate_query_string(data):
    processed_data = {
        key: str(value).lower() if isinstance(value, bool) else value
        for key, value in data.items()
    }
    sorted_items = sorted(processed_data.items(), key=lambda x: x[0])
    return urlencode(sorted_items)

'''把data参数传入JS解密'''
def get_js_headers(params_str, method='POST'):
    node_path='/usr/local/bin/node'
    #node_path = r"D:\nodejs\node.exe"
    js_path = r"/Users/hejie/PycharmProjects/turing_exec/日常兼职/广东招投标/client/0416.js"
    #js_path = r"D:/nodejs/node_global/0416.js"

    try:
        result = subprocess.check_output([node_path, js_path, method, params_str],
                                         text=True,
                                         stderr=subprocess.STDOUT)
        return json.loads(result.strip())
    except subprocess.CalledProcessError as e:
        print("执行JS脚本失败:", e.output)
        return None
    except json.JSONDecodeError:
        print("JS脚本输出格式错误")
        return None

#print(os.path.exists(node_path))
#print(os.path.exists(js_path))


# -------------------- 滑块验证模块 --------------------

import requests ,base64 ,json
import subprocess
from urllib.parse import urlencode
import ddddocr

'''把json参数变成字符串'''


'''获取滑块图片:get请求获取bg,tg,key,token'''
def get_slider_img():

    data1={'captchaType': "blockPuzzle"
          }
    data1_query = generate_query_string(data1)
    js_data = get_js_headers(data1_query, 'POST')
    if not js_data:
        exit("无法获取初始JS参数")
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "29",  # 如果你的请求体(body)长度不同，请相应调整这个值
        "Content-Type": "application/json",
        "Cookie": "_horizon_uid=f7484e37-ce23-4c24-afbf-4a7764b1ca29; __jsluid_s=e5950f11413ee8fdb05b3f7e28ace3d9; openstack_cookie_insert=16275321; _horizon_sid=e331fcbd-b556-4488-9d0a-98034a45c601",
        "Host": "zbtb.gd.gov.cn",
        "Origin": "https://zbtb.gd.gov.cn",
        "Referer": "https://zbtb.gd.gov.cn/",
        "Sec-Ch-Ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-DGI-Req-App": "ztbjg-portal",
        'X-Dgi-Req-Nonce': js_data['nonce'],
        'X-Dgi-Req-Signature': js_data['signature'],
        'X-Dgi-Req-Signatures': js_data['signatures'],
        'X-Dgi-Req-Timestamp': str(js_data['timestamp'])}

    url_img_get='https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/get'
    response = requests.post(url_img_get, json=data1, headers=headers)
    time.sleep(random.randint(1, 3))

    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None, None, None

    try:
        result = response.json()
    except ValueError:
        print("响应不是合法的 JSON 数据")
        return None, None, None

    if 'data' not in result or 'repData' not in result['data']:
        print("响应结构异常:", result)
        return None, None, None

    rep_data = result['data']['repData']
    bg = rep_data.get('originalImageBase64')
    tg = rep_data.get('jigsawImageBase64')
    token = rep_data.get('token')
    secretKey=rep_data.get('secretKey')
    print(f"签名{token}")
    print(f"密钥{secretKey}")
    if not all([bg, tg, token]):
        print("缺失必要参数:", rep_data)
        return None, None, None

    return bg, tg, token ,secretKey # 正确返回三个参数

"""识别滑块缺口位置并返回偏移量slide_x"""
def calculate_slide_offset(bg, tg):
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    try:
        bg_bytes = base64.b64decode(bg)
        tg_bytes = base64.b64decode(tg)
        res = det.slide_match(tg_bytes, bg_bytes, simple_target=True)
        return res['target'][0]
    except Exception as e:
        raise Exception(f"滑块识别失败: {str(e)}")


'''调用pointjson加密slide_x和secretKey算法'''
def EncryptAES(x,secretKey):
    #node_path = r"D:\nodejs\node.exe"
    node_path = '/usr/local/bin/node'
    js_path = r"/Users/hejie/PycharmProjects/turing_exec/日常兼职/广东招投标/client/slider3.js"

    # 调用 Node.js 执行 JS 文件并传入参数 x
    # 调用 Node.js 执行 JS 文件并传入参数 x 和 secretKey
    result = subprocess.run(
        [node_path, js_path,str(x),  str(secretKey),],  # 参数依次为：node路径、js文件路径、x值、密钥
        capture_output=True,  # 捕获输出
        text=True,  # 输出以字符串形式返回
        encoding='utf-8'  # 设置编码格式
    )

    if result.returncode == 0:
        print('调用加密算法成功')
        return result.stdout.strip()  # 返回加密后的字符串
    else:
        raise Exception(f"调用失败: {result.stderr}")


'''检验滑块响应：check验证'''
def check_slider(token,pointjson):
    data={
        "captchaType": "blockPuzzle",
        "pointJson": pointjson,
        "token": token
    }
    data_query = generate_query_string(data)
    js_data = get_js_headers(data_query, 'POST')
    if not js_data:
        exit("无法获取初始JS参数")
    url='https://zbtb.gd.gov.cn/ztbjg-portal/center/captch-portal/check'
    headers={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "111",  # 注意：这个值应与实际发送的数据长度一致，requests通常会自动处理
        "Content-Type": "application/json",
        "Cookie": "_horizon_uid=f7484e37-ce23-4c24-afbf-4a7764b1ca29; __jsluid_s=e5950f11413ee8fdb05b3f7e28ace3d9; openstack_cookie_insert=16275321; _horizon_sid=e331fcbd-b556-4488-9d0a-98034a45c601",
        "Host": "zbtb.gd.gov.cn",
        "Origin": "https://zbtb.gd.gov.cn",
        "Referer": "https://zbtb.gd.gov.cn/",
        "Sec-Ch-Ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-DGI-Req-App": "ztbjg-portal",
        'X-Dgi-Req-Nonce': js_data['nonce'],
        'X-Dgi-Req-Signature': js_data['signature'],
        'X-Dgi-Req-Signatures': js_data['signatures'],
        'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
    }
    res=requests.post(url,json=data,headers=headers)
    time.sleep(random.randint(1, 3))

    print(res.json())
    return res.json()


'''封装处理函数过程，方便调用'''
def process_total():
    try:
        # 获取验证码数据
        bg, tg, token, secretKey = get_slider_img()
        if not all([bg, tg, token, secretKey]):
            exit("获取验证码失败")

        # 计算滑块偏移
        slide_x = calculate_slide_offset(bg,tg)

        # 生成加密参数
        pointJson = EncryptAES(slide_x,secretKey)

        # 提交验证
        success=check_slider(token, pointJson)
        print(success)
        return token

    except :
        return False



# if __name__ == '__main__':
#     result = process_total()
#     print("验证结果:", result)







# -------------------- 主爬虫逻辑 --------------------
def fetch_and_save_data():
    output_dir = r'E:\Python_For_Beginner\广东\广东内容'
    #output_dir = r'D:\PycharmProjects\pythonProject\广东\广东内容'
    os.makedirs(output_dir, exist_ok=True)

    # 初始请求获取总页数
    data1 = {
        "type": "trading-type",
        "dateType": "",
        "keyword": "候选",
        "openConvert": False,
        "pageNo": 1,
        "pageSize": 10,
        "projectType": "",
        "publishEndTime": "",
        "publishStartTime": "",
        "searchType": "pf",
        "secondType": "A",
        "siteCode": "44",
        "thirdType": 10,
        "total": 408,
        "totals": 408,
    }

    data1_query = generate_query_string(data1)
    js_data = get_js_headers(data1_query, 'POST')
    if not js_data:
        exit("无法获取初始JS参数")

    headers1 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_horizon_uid=f7484e37-ce23-4c24-afbf-4a7764b1ca29; __jsluid_s=e5950f11413ee8fdb05b3f7e28ace3d9; _horizon_sid=18f786a8-4ff9-4f93-b7c2-e5a6dac3e2e5; openstack_cookie_insert=76780951',
        'Host': 'zbtb.gd.gov.cn',
        'Origin': 'https://zbtb.gd.gov.cn',
        'Referer': 'https://zbtb.gd.gov.cn/',
        'Sec-Ch-Ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Vtoken': '0',
        'X-Dgi-Req-App': 'ztbjg-portal',
        'X-Dgi-Req-Nonce': js_data['nonce'],
        'X-Dgi-Req-Signature': js_data['signature'],
        'X-Dgi-Req-Signatures': js_data['signatures'],
        'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
    }

    url = 'https://zbtb.gd.gov.cn/ztbjg-portal/center/notice/search'
    res1 = requests.post(url, json=data1, headers=headers1)
    print(res1.status_code)

    result1 = res1.json()
    print(result1)
    num = result1["data"]["pageTotal"]
    print(f"总页数: {num}")

    param_list = []
    for n in range(7, 8):
    #for n in range(1, num + 1):
        if n<6:
            data2 = {
                "type": "trading-type",
                "dateType": "",
                "keyword": "候选",
                "openConvert": False,
                "pageNo": 1,
                "pageSize": 10,
                "projectType": "",
                "publishEndTime": "",
                "publishStartTime": "",
                "searchType": "pf",
                "secondType": "A",
                "siteCode": "44",
                "thirdType": 10,
                "total": 100778,
                "totals": 100778,
                }
            data2["pageNo"] = n
            data2_query = generate_query_string(data2)
            js_data = get_js_headers(data2_query, 'POST')
            if not js_data:
                continue

            headers1.update({
                'X-Dgi-Req-Nonce': js_data['nonce'],
                'X-Dgi-Req-Signature': js_data['signature'],
                'X-Dgi-Req-Signatures': js_data['signatures'],
                'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
            })

            res2 = requests.post(url, json=data2, headers=headers1)
            time.sleep(random.randint(1, 3))
            if res2.status_code == 200:
                result_data = res2.json()
                print(result_data)



        else:
            token = process_total()
            print("验证结果:", token)
            data2 = {
                "type": "trading-type",
                "dateType": "",
                "keyword": "候选",
                "openConvert": False,
                "pageNo": 1,
                "pageSize": 10,
                "projectType": "",
                "publishEndTime": "",
                "publishStartTime": "",
                "searchType": "pf",
                "secondType": "A",
                "siteCode": "44",
                "thirdType": 10,
                "total": 100778,
                "totals": 100778,
            }
            data2["pageNo"] = n
            data2_query = generate_query_string(data2)
            js_data = get_js_headers(data2_query, 'POST')
            if not js_data:
                continue

            headers1.update({
                'vtoken':token,
                'X-Dgi-Req-Nonce': js_data['nonce'],
                'X-Dgi-Req-Signature': js_data['signature'],
                'X-Dgi-Req-Signatures': js_data['signatures'],
                'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
            })

            res2 = requests.post(url, json=data2, headers=headers1)
            time.sleep(random.randint(1, 3))
            if res2.status_code == 200:
                result_data = res2.json()
                print(result_data)

        if result_data.get("errcode") == 0:
            for item in result_data["data"].get("pageData", []):
                param_list.append({
                    "projectCode": item.get("projectCode", ""),
                    "siteCode": "44",
                    "tradingProcess": item.get("tradingProcess", ""),
                    "tradingType": item.get("noticeSecondType", ""),
                })
        print(f"第{n}页收集到{len(param_list)}个项目")

    # 抓取详情页并保存
    base_url = "https://zbtb.gd.gov.cn/ztbjg-portal/center/trading-notice/detail"
    for idx, params in enumerate(param_list):
        data3 = params  # 直接使用字典
        data3_query = generate_query_string(params)
        js_data = get_js_headers(data3_query)
        if not js_data:
            continue

        headers2 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': '_horizon_uid=f7484e37-ce23-4c24-afbf-4a7764b1ca29; __jsluid_s=e5950f11413ee8fdb05b3f7e28ace3d9; openstack_cookie_insert=76780951; _horizon_sid=99823c3e-52aa-4a1c-b71a-60bf230f4285',
            'Host': 'zbtb.gd.gov.cn',
            'Referer': 'https://zbtb.gd.gov.cn/',
            'Sec-Ch-Ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'X-Dgi-Req-App': 'ztbjg-portal',
            'X-Dgi-Req-Nonce': js_data['nonce'],
            'X-Dgi-Req-Signature': js_data['signature'],
            'X-Dgi-Req-Signatures': js_data['signatures'],
            'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
        }

        detail_url = f"{base_url}?{data3_query}"
        # 更新headers
        headers2.update({
            'X-Dgi-Req-Nonce': js_data['nonce'],
            'X-Dgi-Req-Signature': js_data['signature'],
            'X-Dgi-Req-Signatures': js_data['signatures'],
            'X-Dgi-Req-Timestamp': str(js_data['timestamp'])
        })
        res3 = requests.get(detail_url,  data=data3, headers=headers2)
        time.sleep(random.randint(1, 3))
        if res3.status_code == 200:
            try:
                res3_data = res3.json()
                print(res3_data)
                # filename = f"project09_{idx}.json"
                # with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                #     json.dump(res3_data, f, ensure_ascii=False, indent=4)
                # print(f"保存文件: {filename}")
            except Exception as e:
                print(f"解析失败: {str(e)}")
        else:
            print(f"请求失败: {res3.status_code}")


if __name__ == "__main__":
    fetch_and_save_data()