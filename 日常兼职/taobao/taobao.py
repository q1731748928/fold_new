import execjs
import requests
import time

time1 = round(time.time() * 1000)

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://s.taobao.com/search?_input_charset=utf-8&commend=all&ie=utf8&initiative_id=tbindexz_20170306&localImgKey=&page=1&q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&search_type=item&source=suggest&sourceId=tb.index&spm=a21bo.jianhua%2Fa.201856.d13&ssid=s5-e&suggest=history_1&suggest_query=&tab=all&wq=",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
cookies = {
    "wk_cookie2": "13fd32a126a395f65f1bbc538a36d6f7",
    "wk_unb": "UojQPGlx7CSOTg%3D%3D",
    "cookie2": "1e9474c7a330c63d243d4d1013f1578f",
    "_m_h5_tk": "588fc951c2921d8b60457f2d58d220d3_1722337936742",
    "_m_h5_tk_enc": "a16571f655a439097a20feaa1e859f7b",
}
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
data = "{\"appId\":\"34385\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc\\\",\\\"page\\\":\\\"1\\\",\\\"n\\\":48,\\\"q\\\":\\\"%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"categoryp\\\":\\\"\\\"}\"}"
ctll = execjs.compile(open('taobao_app.js', encoding='utf-8').read())
result = ctll.call('get_f', data, cookies.get('_m_h5_tk').split("_")[0], time1)
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": time1,
    "sign": result.get("sign"),
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp4",
    "data": data
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.cookies)
print(response.text)
print(response)
