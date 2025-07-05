import requests

cookies = {}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.jd.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
}

params = {
    'h5st': '20250301231213857;r99ax3swca9999p5;b5216;tk03w5d731a7618nTJHfHeNWpR5OC_U45nG35746E4tGhbn-2yuQvOPD0FqlGLv7N3MvvCBUp5FFQ1xHDg3foakII-gA;e80d9483d88dc515afb3a0958fdecac410c607dc8cc71896e7afdb36fe3a9a3e;5.0;1740841933857;XRJ6PRHMp0GLg1GB28i9m5CBg1293Z3L3ZyA3ZXRPpXL5x2RrMjB3ZXRPp3R4UGLhNDM4ImMoN2Bm12Bi1WAiVTLg5GA4AjBzAzBnRzR5x2RpAV_yQDAiQXR5xZO3BjBiNGLoFGBmRzB3YGA0YGMpRWMjJ2MhVTAi9mM3AjN3Z3L3NCBjgDB2QXR5xZO312OphHMjcEAt0zA6EW-3Z3L3ByR5Z3XtR3Do8zAA4i-PQ2R5x2RscTArUz93ZXRPp3RnN2_w80R5x2RzYyR5Z3XtlSR5x5M5x2RpVG83QXR5ZXRPpXN5x2RhFyB3ZXR5Z3XtVWRfRnMkQzR5ZXR5xZOkRWRfR3MkQzR5ZXR5xZOpZ3L3FG83QXR5ZXRPpXN5x2RlFyB3ZXR5Z3XtJGM5x2RmFyB3ZXR5Z3XtRGO5x2RnFyB3ZXR5Z3XtRXMrV2OpRXRfRHNkQzR5ZXR5xZOpZ3L3tj83ZXR5Z3XtFWRfRn9tQXR5ZXRPpXN5x2RtQXR5ZXRPpXN5x2R18yR5ZXR5xp75x2R1gDAl4CA3ZXRPpH6eY3L3ZS93ZXRPp3RlBW75tWMjhD-CYnLphXNoZXELYn9icTAr0jE3Z3L3VD8mQXR5xp7;4ef60a848982edf537e6c6d0d32837fa0c8618d7d42a66cc0dc9da5439561acc',
    'appid': 'www-jd-com',
    'body': '{"page":1,"pagesize":25,"area":"22_1930_0_0","source":"pc-home"}',
    'clientVersion': '1.0.0',
    'client': 'pc',
    'functionId': 'pc_home_feed',
    't': '1740837059325',
    # 'uuid': '76161171.17407174357931755805150.1740717436.1740799308.1740836843.5',
    # 'loginType': '3',
    # 'x-api-eid-token': 'jdd03TMCSF47R7PGBYVJMC2DDA4BEFBN6LOXW2JZRXF5IT7YF5UYYFBCDTKXOPXDRTRQW4TZLCNHSV4XJLU2V3QZDSZUX4MAAAAMVKH3C67QAAAAACBVHGORSZ3KZHMX',
    # 'callback': 'jsonpMore2Goods',
    # '_': '1740841520362',
}

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers).text
print(response)