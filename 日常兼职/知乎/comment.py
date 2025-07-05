import urllib

import execjs
import requests



cookies = {
    "d_c0": "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518",
    "z_c0": "2|1:0|10:1745250842|4:z_c0|92:Mi4xckMwTUF3QUFBQUFCTUpMTk50N1hHQ1lBQUFCZ0FsVk5Hcmp6YUFBRHR1d0ZsR0hrckhOVk1KNjVHTFN0VFRrV2NR|5a7abab116b19ebe2f8f3a3c5445c49918ca4080850a2565844c717bca48006a",
}
url = "https://www.zhihu.com/api/v4/comment_v5/articles/25415549/root_comment?"
params = {
    "order_by": "score",
    "limit": "20",
    "offset": ""
}
encoded_params = url + urllib.parse.urlencode(params)

ctll = execjs.compile(open("/Users/hejie/PycharmProjects/turing_exec/日常兼职/知乎/zhihu.js", encoding='utf-8').read())
result = ctll.call('get_x_zse_96', encoded_params)
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhihu.com/search?type=content&q=%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": str(result)
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.text)
# print(response)
# "101_3_3.0+/api/v4/comment_v5/answers/3190774612/root_comment?order_by=score&limit=20&offset=+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"
# "101_3_3.0+/api/v4/comment_v5/answers/3190774612/config+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"