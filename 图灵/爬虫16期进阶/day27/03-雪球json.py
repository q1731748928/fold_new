import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://xueqiu.com/today?md5__1038=n4IxgD070%3DG%3DD%3DYDsTiQLywDfrEFDRD3aoD",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "elastic-apm-traceparent": "00-4f589cf2bdd5308b12574fb1d4166d5f-b7632d3090b9f2c8-00",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "cookiesu": "671744296650662",
    "device_id": "ad434d5aff8b96c2c79a5ff950cc583b",
    "s": "c013a7ge1o",
    "acw_tc": "ac11000117443508898026736e00317d547c81927ff0c0c3947ca59df28973",
    "xq_a_token": "8227a6f1f070ca10a573ea273e25da157b017b89",
    "xqat": "8227a6f1f070ca10a573ea273e25da157b017b89",
    "xq_r_token": "8c19700a9bde6cebd6eb64490168b410844f0b33",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc0NjA2MTE1OSwiY3RtIjoxNzQ0MzUwODU5OTg3LCJjaWQiOiJkOWQwbjRBWnVwIn0.JmDBlfAW1Rwypu6sxBaP7IHU-6KTPoPfSvEIop8jQ6cuMwLSKhbkMJiBlO9tZIOMq6FBmPlHZt42Yafa2Cyn85OXgJLwxCtgpmGdDQ7d_OKWONhElFa6E8CEjZ7ElX2XbC4lEOczasvLltujjYqGR_izwnvU_NcCbC3S3cRMLBsS6-14eBFbiDUGRgM-h677dWospLpAi-jfgVDQg-oBnEPJATvPvOaLBH-FswW9OFp2hOaBjYXyKWfRy2mBGiu_ff5wchnYLkA8hfA0W2WK-DjoQ-C8FeKAqiKF5FViU_WJsl2q6EjYkEaxzPf1ZtPC3Aw27TGjhGUk_BaUjxXqag",
    "u": "671744296650662",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1744296651,1744350888",
    "HMACCOUNT": "788AC10A3780E5E2",
    ".thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7": "W79cuuF/U+xaw1EM84XKLCDJ7kPtIOtnoQjhA1m4k6kZxSt+hRQVZmPAZfaqCEcaORIWuYR21vUmoCNQzjIj/w%3D%3D",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1744351240",
    "ssxmod_itna": "QqmxBDnD9Qq9G0D2DRrrD0iDpxTeDXDUkqiQGgDYq7=GFYDCODF3PW4BKm5G8mYiAg4AibD0vezGDA5Dn8x7YDtxfP4q7UED5KsaibD5Poy01DEmCY=kDE43K5nKuSuEp7DnDiD844G2DYoDCqDS9DD9UoeD4b3Dt4DIDAYDDxDW7eDBne2=DGp31Wbdgkw4hD23xif=KQp=DitOxi5rgnu3gwG3xDf7xB6ixAfxNru=/qGnD0QpyYp3x03ONrOG5eGWQSrGxKGuRp0VGxu=MCwjcwUxR3LqDh5mKDN348DPiGYsY0zKbbNKG5H0Dgix3BKGYdmodZbhNQdNYe1qC+kimqegEP5ht1nYO257Gd+W4djQM7DldY/D52w4FDxIh5hB1WiDD",
    "ssxmod_itna2": "QqmxBDnD9Qq9G0D2DRrrD0iDpxTeDXDUkqiQGgDYq7=GFYDCODF3PW4BKm5G8mYiAg4AiDG4eKiYaUQOboyncMHisB8+PwD"
}
url = "https://xueqiu.com/statuses/hot/listV2.json"
params = {
    "since_id": "-1",
    "max_id": "-1",
    "size": "15",
    "md5__1038": "n4AxgDRD2Ae7qRDBqDwWxUhiDuDfrxhGRwubrD"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)


