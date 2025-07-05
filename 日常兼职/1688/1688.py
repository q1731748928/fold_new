import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://fuzhuang.1688.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "SameSite": "none",
    # "cookie1": "Vq8zmU87VRT41jRTqkRLXbMwvv%2FlR4azHtTcsNsNxZo%3D",
    # "cookie2": "1b1f4f9a1dfeac93e7514021d7921419",
    # "cookie17": "UojQPGlx7CSOTg%3D%3D",
    # "sgcookie": "E100WjDJ6QdynZVqWWht5ZNsnztkIfdHqdOOGWBVYWTnZQ8vhuiPzSW5j1a0XO2%2B3ulhRH6lNm6ms%2FB8AiiThvyblwCX2JgAqTKMBJGr5Mnx3QYIMJx2iw8O2lOdjGwnM6sx",
    # "t": "c60530851ba3e459fac6d339470c68f3",
    # "_tb_token_": "fa95e37483616",
    # "sg": "e8a",
    # "csg": "a098eb0c",
    # "lid": "gohejie",
    # "unb": "1945588948",
    # "uc4": "nk4=0%40Bp0aPKw4F7Y4bCMfAHySLgdD&id4=0%40UOBUl95hM%2FPWhWrRd2fOHg2lk0l0",
    # "_nk_": "gohejie",
    # "cna": "ljusIB+hJHUBASQOA5DKifif",
    # "mtop_partitioned_detect": "1",
    # "_m_h5_tk": "d39b291d8c35422e85ec9de3ab88f0fe_1747282359130",
    # "_m_h5_tk_enc": "3e3d5e296e5c860b9362af158278593e"
}
url = "https://widget.1688.com/front/getJsonComponent.json"
params = {
    "callback": "jsonp_1747275162497_51134",
    "namespace": "cateMarketOfferList",
    "widgetId": "cateMarketOfferList",
    "methodName": "execute",
    "sceneId": "194498,192002,197762,213250,17282,17474,16962,17026,17410,17922,17538,18050,16514,16834,18114,18754,91010,98306,265218,1441730,1988354,1988290,1988226,2003458,1939010,2242050,2243266,2227970,2212482,2685186,2695682,2695618,3382146,3368258",
    "mockDate": "",
    "_": "1747275393710"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)