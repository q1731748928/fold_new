# -*- coding: utf-8 -*-

import requests

headers = {
    "pragma-uuid": "bd5d8747-e7d5-420d-a95e-3016828cd9ce",
    "pragma-os": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "pragma-dpid": "d2cd855d3f4141beae220b1cc58132c6a172563694337095119",
    "M-SHARK-TRACEID": "11d2cd855d3f4141beae220b1cc58132c6a172563694337095119c2040417430841264019765b2",
    "pragma-device": "00000000000000",
    "picasso": "JOYPicassoModules/picassoviewcontroller_joyhome_dp:0",
    "pragma-unionid": "d7d2b75bb92e475e8d1dc656fe204cf6a172563694346591702",
    "network-type": "wifi",
    "Host": "mapi.dianping.com"
}
url = "https://mapi.dianping.com/mapi/joy/event/index/widelydzrecom.joy"
params = {
    "start": "0",
    "limit": "10",
    "cityid": "344",
    "longitude": "0",
    "latitude": "0",
    "apiexperiment": "channelold",
    "ugctag": "loadugctag",
    "rank": "loadrank"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)