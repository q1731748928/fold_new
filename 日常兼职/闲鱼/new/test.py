import random
import time

import execjs
import pymysql
import requests

time1 = round(time.time() * 1000)
wait_time = random.uniform(3, 5)
# 二手电子产品(手机、平板、电脑)，特征爬价格，成色，销量，品牌，内存，颜色，保修状态，卖家信用，好评率，卖家评论数，几人想要，地区
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="part_time_job")
cursor = db.cursor()
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://2.taobao.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://2.taobao.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-fetch-storage-access": "active",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "a0818127ce439095f04a1dd1f3aa6021_1746885229369",
    "_m_h5_tk_enc": "77a21b7db46767d06ccdfbecff0bc9d9"
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.wx.search/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": "1746880032899",
    "sign": "0057e96b0b6a03ca01f2a2180ef47615",
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlemtopsearch.wx.search",
    "sessionOption": "AutoLoginOnly",
    "c": "a0818127ce439095f04a1dd1f3aa6021_1746885229369;77a21b7db46767d06ccdfbecff0bc9d9"
}
data = {
    "data": "{\"searchReqFromPage\":\"xyMiniHome\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

RequestsCookieJar = response.cookies
_m_h5_tk = RequestsCookieJar.get('_m_h5_tk')
_m_h5_tk_enc = RequestsCookieJar.get('_m_h5_tk_enc')

i = 0
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": str(_m_h5_tk),
    "_m_h5_tk_enc": str(_m_h5_tk_enc)
}
# keywords = ['二手手机', '二手平板', '二手电脑', '二手智能手表', '二手耳机', '二手相机', '二手电视', '二手音响', '二手手环', '二手显示器', '二手打印机', '二手投影仪']
keyword = '二手手机'
while True:
    i += 1
    data = {
        "data": '{\"keyword\":' + '\"' + keyword + '\"' + ',\"pageNumber\":' + str(
            i) + "," + '\"rowsPerPage\":30,\"plateform\":\"pc\",\"searchReqFromPage\":\"xyHome\",\"bizFrom\":\"home\",\"searchTabType\":\"SEARCH_TAB_MAIN\",\"sortField\":\"\",\"sortValue\":\"\",\"propValueStr\":\"\"}'
    }
    ctll = execjs.compile(open('sign_new.js', encoding='utf-8').read())
    sign = ctll.call('get_sign', data.get('data'), cookies.get('_m_h5_tk').split("_")[0], time1)

    url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.wx.search/1.0/"
    params = {
        "jsv": "2.7.2",
        "appKey": "12574478",
        "t": str(time1),
        "sign": sign,
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.wx.search",
        "sessionOption": "AutoLoginOnly",
        "c": "67d4c5674d9fd8a9dcbb977224da25b3_1746879053461;5f4d8ae2092b66357043cbc89276ed79"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    print(response.text)
    time.sleep(wait_time)
    data = response.json()['data']
    resultLists = data.get('resultList')
    # 二手电子产品(手机、平板、电脑)，特征爬价格，成色，品牌，内存，颜色，保修状态，卖家信用，几人想要，地区
    if resultLists == [] or resultLists == '' or resultLists == None:
        break
    if resultLists != [] and resultLists != '' and resultLists != None:
        for resultList in resultLists:
            # 标题
            title = resultList.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get(
                'detailParams', {}).get('title', None)
            if title != '' and title != None:
                print(title)
                try:
                    sql = "INSERT INTO xy_back (keyword, title, page, result_list) VALUES (%s, %s, %s,%s)"
                    val = (str(keyword), str(title), i, str(resultList))
                    cursor.execute(sql, val)
                    db.commit()
                except Exception as e:
                    print(e)
