import requests


headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
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
    "sec-fetch-storage-access": "none",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "ac12deac2b481eca08be4c3644bbc802_1746878626092",
    "_m_h5_tk_enc": "655df6873257dff085811723fb5873bb"
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.wx.search/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": "1746870741876",
    "sign": "61159a81a130c63ca73fdba2d67c5eca",
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlemtopsearch.wx.search",
    "sessionOption": "AutoLoginOnly",
    "c": "ac12deac2b481eca08be4c3644bbc802_1746878626092;655df6873257dff085811723fb5873bb"
}
data = {
    "data": "{\"keyword\":\"二手手机\",\"pageNumber\":1,\"rowsPerPage\":30,\"plateform\":\"pc\",\"searchReqFromPage\":\"xyHome\",\"bizFrom\":\"home\",\"searchTabType\":\"SEARCH_TAB_MAIN\",\"sortField\":\"\",\"sortValue\":\"\",\"propValueStr\":\"\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)