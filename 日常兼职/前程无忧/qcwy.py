import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "account-id;": "",
    "cache-control": "no-cache",
    "from-domain": "51job_web",
    "partner": "www_google_com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "property": "%7B%22partner%22%3A%22www_google_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D000000%26keyword%3D%25E7%2588%25AC%25E8%2599%25AB%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26searchType%3D2%26keywordType%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%2C%22keywordType%22%3A%22%22%7D",
    "referer": "https://we.51job.com/pc/search?jobArea=000000&keyword=%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&searchType=2&keywordType=",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sign": "57e3fbd9efdf2fd5d9af9a39f08276e4887231ba8dd26d9986d6866cd193f807",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "user-token;": "",
    "uuid": "5370d7e3515f1fc9c0f37d6dc022bd14"
}
cookies = {
    "partner": "www_google_com",
    "seo_refer_info_2023": "%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22referHost%22%3A%22www.google.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D",
    "privacy": "1744285137",
    "guid": "5370d7e3515f1fc9c0f37d6dc022bd14",
    "sajssdk_2015_cross_new_user": "1",
    "Hm_lvt_1370a11171bd6f2d9b1fe98951541941": "1744285138",
    "Hm_lpvt_1370a11171bd6f2d9b1fe98951541941": "1744285138",
    "HMACCOUNT": "788AC10A3780E5E2",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%225370d7e3515f1fc9c0f37d6dc022bd14%22%2C%22first_id%22%3A%221961f7efc14fcc-0c3e4bfe089186-1b525636-1930176-1961f7efc152a8b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2MWY3ZWZjMTRmY2MtMGMzZTRiZmUwODkxODYtMWI1MjU2MzYtMTkzMDE3Ni0xOTYxZjdlZmMxNTJhOGIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI1MzcwZDdlMzUxNWYxZmM5YzBmMzdkNmRjMDIyYmQxNCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%225370d7e3515f1fc9c0f37d6dc022bd14%22%7D%2C%22%24device_id%22%3A%221961f7efc14fcc-0c3e4bfe089186-1b525636-1930176-1961f7efc152a8b%22%7D",
    "nsearch": "jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
    "search": "jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21",
    "JSESSIONID": "5518D604D98D07D085D1BD59C2840D1B",
    "acw_tc": "ac11000117442938260607550e00761050309afe1944d940340f0fd8f8293d",
    "ssxmod_itna": "Qq+2GKDIx0oxXDRDCo=wN4BIuo4REo40K+e+jQD/YDfgxiNDnD8x7YDvzANCmb+n3rLFfetYwIYQ7OiqdpQNQBGfKfGCBxGIDeKG2DmeDyDi5GRD0FKQD445GwD0eG+DD4DW8qDUZENqDd9Z9Cy6cOpca89xGWv=KDm1KDRroDSQ7sVOyFr75Di=oDXoYDa=KDu6yOsxi8D7FLvxE1D7PpA9fAwxi3fDvA+40Okb9HTm5s/1KXNQi4FxxedZireWDqsA0DwAaieDRxwW0dCyrYo0idYh4e6VEnOYD===",
    "ssxmod_itna2": "Qq+2GKDIx0oxXDRDCo=wN4BIuo4REo40K+e+QG9bTDBdP7QHGcDedrD=",
    "acw_sc__v2": "67f7cfc37f5efbfaa656501b29748579efa3c5be"
}
url = "https://we.51job.com/api/job/search-pc"
params = {
    "api_key": "51job",
    "timestamp": "1744293827",
    "keyword": "爬虫工程师",
    "searchType": "2",
    "function": "",
    "industry": "",
    "jobArea": "000000",
    "jobArea2": "",
    "landmark": "",
    "metro": "",
    "salary": "",
    "workYear": "",
    "degree": "",
    "companyType": "",
    "companySize": "",
    "jobType": "",
    "issueDate": "",
    "sortType": "0",
    "pageNum": "1",
    "requestId": "",
    "keywordType": "",
    "pageSize": "20",
    "source": "1",
    "accountId": "",
    "pageCode": "sou|sou|soulb",
    "scene": "7"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)