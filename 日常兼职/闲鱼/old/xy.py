import random
import time

import execjs
import pymysql
import requests
c
wait_time = random.uniform(30, 60)
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
    "referer": "https://2.taobao.com/search?word=%E4%BA%8C%E6%89%8B%E7%94%B5%E8%84%91&spm=a2170.xianyu_tbpc_search.0.0",
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
    "cna": "nqV+IIqtKjoBASQOA5CIE9nT",
    "t": "4a5c37ffbcc87f6313d26c0e63bf171b",
    "xlly_s": "1",
    "sgcookie": "E100wIObr0k7iuwLcAVUNxOYvUbhfT7y28GKgex6G2%2B0ynBsWvvA4I4Jqf26tpiXxywF00wTxpE%2BnVJwT2GnMnXjkKi0lJRlmgGe4fwM8JsWLfXIyQOTrrtRdr%2Flk%2B8S5i%2BU",
    "tracknick": "gohejie",
    "unb": "1945588948",
    "isg": "BFpa-X7a5kuTOGrnhweccK3VqwZ8i95ltdVir2TTZO241_sRTBsQdCJmp6PLB1b9",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "c08426fdb1770ff15d64203c5b8866e8_1746850883244",
    "_m_h5_tk_enc": "1db830b70c0b4cf60ae5cbc9ce7c1a4a"
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
for i in range(1, 6):
    data = {
        "data": f'{{"keyword":"二手手环","pageNumber":{i},"rowsPerPage":300,"plateform":"pc","searchReqFromPage":"xyHome","bizFrom":"home","searchTabType":"SEARCH_TAB_MAIN","sortField":"","sortValue":"","propValueStr":""}}'
            # "{\"keyword\":\"二手手机\",\"pageNumber\":1,\"rowsPerPage\":300,\"plateform\":\"pc\",\"searchReqFromPage\":\"xyHome\",\"bizFrom\":\"home\",\"searchTabType\":\"SEARCH_TAB_MAIN\",\"sortField\":\"\",\"sortValue\":\"\",\"propValueStr\":\"\"}"
    }

    ctll = execjs.compile(open('sign.js', encoding='utf-8').read())
    result = ctll.call('get_f', data.get('data'), cookies.get('_m_h5_tk').split("_")[0], time1)
    params = {
        "jsv": "2.7.2",
        "appKey": "34839810",
        "t": str(time1),
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.pc.search",
        "sessionOption": "AutoLoginOnly",
        "spm_cnt": "a21ybx.search.0.0",
        "spm_pre": "a21ybx.home.searchInput.0"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    RequestsCookieJar = response.cookies
    _m_h5_tk = RequestsCookieJar.get('_m_h5_tk')
    _m_h5_tk_enc = RequestsCookieJar.get('_m_h5_tk_enc')

    cookies = {
        "cna": "nqV+IIqtKjoBASQOA5CIE9nT",
        "t": "4a5c37ffbcc87f6313d26c0e63bf171b",
        "xlly_s": "1",
        "sgcookie": "E100wIObr0k7iuwLcAVUNxOYvUbhfT7y28GKgex6G2%2B0ynBsWvvA4I4Jqf26tpiXxywF00wTxpE%2BnVJwT2GnMnXjkKi0lJRlmgGe4fwM8JsWLfXIyQOTrrtRdr%2Flk%2B8S5i%2BU",
        "tracknick": "gohejie",
        "unb": "1945588948",
        "isg": "BFpa-X7a5kuTOGrnhweccK3VqwZ8i95ltdVir2TTZO241_sRTBsQdCJmp6PLB1b9",
        "mtop_partitioned_detect": "1",
        "_m_h5_tk": _m_h5_tk,
        "_m_h5_tk_enc": _m_h5_tk_enc
    }

    ctll = execjs.compile(open('sign.js', encoding='utf-8').read())
    result = ctll.call('get_f', data.get('data'), cookies.get('_m_h5_tk').split("_")[0], time1)
    params = {
        "jsv": "2.7.2",
        "appKey": "34839810",
        "t": str(time1),
        "sign": result.get("sign"),
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.pc.search",
        "sessionOption": "AutoLoginOnly",
        "spm_cnt": "a21ybx.search.0.0",
        "spm_pre": "a21ybx.home.searchInput.0"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    time.sleep(wait_time)
    data = response.json()['data']
    resultLists = data.get('resultList')
    # 二手电子产品(手机、平板、电脑)，特征爬价格，成色，品牌，内存，颜色，保修状态，卖家信用，几人想要，地区
    count = 0
    if resultLists != [] and resultLists != '' and resultLists != None:
        for resultList in resultLists:
            # 标题
            title = resultList.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('detailParams', {}).get('title', None)
            if title != '' and title != None:
                count += 1
                print(title)
                try:
                    sql = "INSERT INTO xy (keyword, title, page, result_list) VALUES (%s, %s, %s,%s)"
                    val = ('二手手环', str(title), i, str(resultList))
                    cursor.execute(sql, val)
                    db.commit()
                except Exception as e:
                    print(e)
            # # 价格
            # price = resultList.get('data', {}).get('item', {}).get('main', {}).get('clickParam', {}).get('args', {}).get('price',None)
            # print(f'{title},{price}')
            # # 成色
            # price = resultList.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('fishTags', {}).get( 'price', None)
