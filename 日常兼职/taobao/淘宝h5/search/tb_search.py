import json
import random
import time

import execjs
import requests

time1 = round(time.time() * 1000)
wait_time = random.uniform(10, 30)
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://s.taobao.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=pikpak&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.search_manual.0&ssid=s5-e&tab=all",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "cookie2": "1e1cb58daadce2a15fa36eb105d28a15",
    "t": "fc8d259d200531c5e2e8e488f059379c",
    "_tb_token_": "5338b7eeeb97f",
    "thw": "xx",
    "3PcFlag": "1746699510696",
    "xlly_s": "1",
    "unb": "1945588948",
    "uc1": "cookie14=UoYaje%2FwAAEK0g%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&existShop=false&pas=0&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D",
    "sn": "",
    "uc3": "nk2=BJlIz0%2BX0w%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UojQPGlx7CSOTg%3D%3D&vt3=F8dD2EXa2WU3c5J9S5U%3D",
    "csg": "053b195d",
    "lgc": "gohejie",
    "cancelledSubSites": "empty",
    "cookie17": "UojQPGlx7CSOTg%3D%3D",
    "dnk": "gohejie",
    "skt": "e6efaa8185e450e7",
    "existShop": "MTc0NjY5OTUxMw%3D%3D",
    "uc4": "nk4=0%40Bp0aPKw4F7Y4bCMeLW8kB58N&id4=0%40UOBUl95hM%2FPWhWrRd2fPq%2BWzl6mJ",
    "tracknick": "gohejie",
    "_cc_": "URm48syIZQ%3D%3D",
    "_l_g_": "Ug%3D%3D",
    "sg": "e8a",
    "_nk_": "gohejie",
    "cookie1": "Vq8zmU87VRT41jRTqkRLXbMwvv%2FlR4azHtTcsNsNxZo%3D",
    "wk_cookie2": "18c174b097e1ebe54db713e656b37e1e",
    "wk_unb": "UojQPGlx7CSOTg%3D%3D",
    "sgcookie": "E100l1lNlobzIfSZGPpchaEi33p2WqFLzq9HmKfGPZ%2Bv2w%2FViaKNcOMm4f%2BhC9M4XvW9oyrwhB7vm2Rk5maCxVmXrwCgtGRJ2v4BFAXXrFW9qk7jvMigLCiuJDJtwTJIZVCT",
    "_hvn_lgc_": "0",
    "havana_lgc_exp": "1746730617847",
    "havana_lgc2_0": "eyJoaWQiOjE5NDU1ODg5NDgsInNnIjoiMWRjOTU2ZWJhN2NhYWQ4YWI1MDQyNmI2ZmU5ZDUzMGMiLCJzaXRlIjowLCJ0b2tlbiI6IjFwbzBqTXl5c2pBdUpXY19sSlRxbUZBIn0",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "3f3d166e79f00edf1170653c3937442f_1746716964684",
    "_m_h5_tk_enc": "139bc2d274b7b5bb6ef92da13e6d0bf9",
    "bxuab": "0",
    "aui": "1945588948",
    "sca": "03356a8f",
    "_samesite_flag_": "true",
    "havana_sdkSilent": "1746796240485",
    "cna": "Gwf4HuwY6TYCAXWTCb2wNzA5",
    "sdkSilent": "1746796272756",
    "tfstk": "gyjtatwwhJHTFnS9KOznoTtTAQy3WyXas1WSmIAil6CdhBm0Qh42DsddgCYMfCmvDtCVisB4QKOfGsdcSyqlQO-2c7xYquXZdSPYTGKji9twnFP3KXqlQO-qBjwlRuDYIWnk1qOfGHTBeK-XCCi6dJpvFctX1EGIRLOBcnTXlpOBFKuslFg_p9OehnOfGFwpRBJj6tiWOROjDakp3zH79OojcMp9RyX6OAxRvdpBNOsKV0MwBFd5CBNoQwN2k1LOxlhyBw6RsdC44c-6kN_WfiF8XH6P-19dG73vOaINDUjTw4R1bI5JfwFIXntNXaYyDzHwKGBC4EIa6DOOT9_kbgNED_6hEG8FD7hBgNvyAdQLh2O6lg7RqgL6jbAJnVwLpqu25pusdkdw62bPDpduBbgqueDepQ2L7qu25pJpZReEuq8nL",
    "isg": "BAIC4s4r3sFGgczE1tU4dRK0Uw5k0wbtXQ3Kt0wbFHUyn6IZNGJp_NXRT5vjy36F"
}
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
params = {
    "jsv": "2.7.4",
    "appKey": "12574478",
    "t": str(time1),
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "timeout": "10000",
    "type": "originaljson",
    "dataType": "jsonp",
    "bx-ua": "231\\u00214hG3H4mUXoS+j3xBdk3GUzGjUGg0uSOn+fYFmLQQwGng0wmHntUSK+9gzeiUmeFNM+I/rW6sSybb6IXbLtFyLMrEKRoaRfifVPxuUvmd40yQXLS5Idm/FmCpI4b+XjRoRBHuRrUgFPIF+L0i3kZOg0CH447PY823T8nUCFI8enVTaURv6v9IwzkL4OZ3SADA1YfpzI6WxV3s9B0ee3jZSvcv+ycx+jYE51JhXuTlSKBrUFXOFBjSYiD+Ou8n+Zd++6WF1cGC0sgRHJBh+++j+ygU3+jOQN3DP1ANF4k3k8Tk90EEMFLiXPFvTj1hUiGmm+Z/BbesNVYnd+RfscLgYjwAlBMBs1xQQrvTxPpZ1MlWPWNNZKblNqRvQLoTf/zXhRTm6qxB57+YexAQlgLPIC6UqfApKdPXkfMjg3pWUXQGyAtRz0j65/lUrTtoRMF2jvFZjwaEL6s1+LMCPrwyR4byBa25E6ed+VB8OtZ8eAe9W3oZTHcXZH8VhOtzMQ0/WKjSi+Qr2yGfc+NZov+xvBDSei+GXWsihOQtiv0mWdaZq1r87G7SahO+q86IIWWJIC39+lPMv73/kYmGkxd3NMug5PrZ4GWkqh3bLOlxIyog5DxDJ18ri6fg3T3TqS/cR7UOcV0OBNUfTBkqAVUAiXzn75zC+fJK9iHK+fY1IsIQvwVyVw4BSyWyC4uJHQjXfvoleLsXgkDKtzFSdG82GpwyhY5ayIxp3vM0gLIqs+C2vaIxhBn/XWeV45eqZfT4/F7DQbqN8SQWQhbWtRUlIoPvVoi5odyhQXGfDKNuU4RTCbP7nnpBYDOarWfgD88UwgnZ1S8qNV6qg2CnwzurKABsnA/vNLxo1Jxa410H1tPJfNABvTykQMnUhLnxn0/u9mrrxgjl0Yf1pzsYs0fXqz1282UFs3vmu/xYV3XceP0m+vJ4m502QxPrk0rQDxyefbpyBiR96brT8VvoDIiKFT5K6uCx4L/acLsaISOYWbs2rwJOwKc4ZWxx6SfYnOOjyT0IunbJqXEbSvoYYlgcVqMAC3E6l+9Q5SJBrnIkhHfDLVnmpAQ5uKUtdH00BabTC2UrJA45vAcxiaZpDD3iscGH56C7dsLYKhNfh/wnUKJF+n9CFPNPPxwgFNL8t2pFg89jwERBSAQV1HkhS6TMQfIDY23G8S57NvU1CMyAjCFaAFu1kf7UIAwZZ8yDIC00EAP1+ZEF3to+2kYD61HXx2M4kH6BZU12TfqdHzcTohzLbIq+3pgYbrmRghj1dlyg15fHqxK51iZkBkOqPVyo4bET2kE+glnjfs+4W6EIZwSt1/RdSXr+1lj5D5pPSmtuEjjkVxf1yzc2LmPiFaWHGS+JRzF3w2SNsS+Zpu0TaOCjA1ExzhC9/i/Odcze4hDmgYpaKzYTr2fiHe8qR/RBNkE5C42ljvoWurHSetL9TCl1V01S/0m8kH2ICZnZm5C9Exr6x0WHRPV+45ftK6NBwynLDoIuN3GLMvC/2qwcOWCnvpO7uMwczeaV4XeYqs6KmQ6HzdA8YIRfxgRNoNwo7MXzshSko9+uxoZfxXbDn0epX3HKWSRTsABTXakGmNQlBKeVg6nfx/fN4vezkac6oij1ArDPYIdWPH5vz5gAgg4Ta0pXli7+f725005y0ClhbgAHI8pBd5lFyS+MznEvKcdae60yrFeqB9NC+ExFXXCWK8bECnIHYES=",
    "bx-umidtoken": "T2gAe7izNprUiqkUMxbqQUGocDLXll82cq0q7yXZt83saI65QI90YvC5aUL0OG5xmtM=",
    "bx_et": "g8_xa2V217hAp87vZsroj6TYPpPuXuf4nt5ISdvmfTBR1L0ggEqwWOpRQKxDlK09W1BNIOCagC91COpGmu4hgs8w5JYT-yfqNRyTUZLsI_T2snyuZY4hgs8ZMANhVycTi83Hhc91CUtW9BT6GKgXN7d9OqT6hhMSVB9W5Ft6fQ9WOCojfnibw_9y1F91CnNJVLRs6P3BFS9sWMlJ_khQbsus5advVufXFjYdyIKvds_-R2G2MnpCGLwnggwwXtKArrHeMg1dnIBa8q8XXisBlNeLkU1FqtORCJn9FMQVWHbYpDJfudWplgeSkFTVkMxeWkh2ZZC58hQ4H49AU_sHuwwrW91ltZ-PWJHWQiAePII8109Xfg7R-wKXovvpsmN8wcowcQojNzp2H0jFWQp3MviZb3cywpV80cowcQRJKSFrbc-oa"
}
data = {
    "data": "{\"appId\":\"46853\",\"params\":\"{\\\"itemId\\\":\\\"679825339660\\\"}\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

RequestsCookieJar = response.cookies
_m_h5_tk = RequestsCookieJar.get('_m_h5_tk')
_m_h5_tk_enc = RequestsCookieJar.get('_m_h5_tk_enc')


cookies = {
    "cna": "9nKjIKL8oGsBASQOA5Br4lQA",
    "thw": "cn",
    "t": "c60530851ba3e459fac6d339470c68f3",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": _m_h5_tk,
    "_m_h5_tk_enc": _m_h5_tk_enc,
    "_tb_token_": "fa95e37483616",
    "xlly_s": "1",
    "cookie2": "1b1f4f9a1dfeac93e7514021d7921419",
    "3PcFlag": "1747273883007",
    "wk_cookie2": "137c18fd2e615a9a1de6967127e0d00c",
    "wk_unb": "UojQPGlx7CSOTg%3D%3D",
    "sgcookie": "E100WjDJ6QdynZVqWWht5ZNsnztkIfdHqdOOGWBVYWTnZQ8vhuiPzSW5j1a0XO2%2B3ulhRH6lNm6ms%2FB8AiiThvyblwCX2JgAqTKMBJGr5Mnx3QYIMJx2iw8O2lOdjGwnM6sx",
    "unb": "1945588948",
    "csg": "a098eb0c",
    "lgc": "gohejie",
    "cancelledSubSites": "empty",
    "cookie17": "UojQPGlx7CSOTg%3D%3D",
    "dnk": "gohejie",
    "skt": "9a2c1bb2247f98df",
    "tracknick": "gohejie",
    "_l_g_": "Ug%3D%3D",
    "sg": "e8a",
    "_nk_": "gohejie",
    "cookie1": "Vq8zmU87VRT41jRTqkRLXbMwvv%2FlR4azHtTcsNsNxZo%3D",
    "uc1": "existShop=false&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie14=UoYajLe7kWmg3A%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=URm48syIIVrSKA%3D%3D&pas=0",
    "sn": "",
    "uc3": "lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dD2EXQf%2BD9UaBJzvw%3D&nk2=BJlIz0%2BX0w%3D%3D&id2=UojQPGlx7CSOTg%3D%3D",
    "existShop": "MTc0NzI3Mzg4Nw%3D%3D",
    "uc4": "nk4=0%40Bp0aPKw4F7Y4bCMfAHySLgdD&id4=0%40UOBUl95hM%2FPWhWrRd2fOHg2lk0l0",
    "_cc_": "WqG3DMC9EA%3D%3D",
    "_hvn_lgc_": "0",
    "havana_lgc_exp": "1747304991818",
    "havana_lgc2_0": "eyJoaWQiOjE5NDU1ODg5NDgsInNnIjoiMWI5YzY3ZWQxMGQ5NzNhYzFmYjEzNzg0YmFmMGRkZDciLCJzaXRlIjowLCJ0b2tlbiI6IjFuOG1nTFZlbUdaa1RzYXBicUphUzJRIn0",
    "bxuab": "0",
    "aui": "1945588948",
    "sca": "6396edf4",
    "_samesite_flag_": "true",
    "sdkSilent": "1747363521007",
    "havana_sdkSilent": "1747363521007",
    "tfstk": "gB8Ewf9fGav__iXdxF_z01Ctab_dlakj8U65ZQAlO9XhdQflzdvS99OopL8PIQKI9gMLaWLw3zaIpDduza_ohxgjlBhdyaDfZaae-9CJsTc1xJRhJWbohxgbf5jKdavWx6Kp7lfAI6fltgcNS_f5r_4HEOjGiswhrLvlSPfAwu2lEa0gIOClrTvlrf7GB__lEfnFbiuNiMcSLW2XO05CYtAhQzRp76jUvBXarzYwxMW0lOzurF5H6BJEMy0VIHtkRNYnI8_MMh9h_Zuza1-2swfeeqUd-IAMqM8rVSBJbCxfbhFI918egU5VX025Fi8MRwKZ3r6DXQYPjBH4D1tkGetydAUldnRMQiT_Cr_M8p8hbZjrV8CiRVLJY8qPx1CNhflauEf1xWELNVq82Gv5_tGp9uERxM5Nhfla2uIGt1Wj9BC..",
    "isg": "BEJCPn4enjh9zoJe0YFLCq2mk06kE0YtCmQcdoxbbrVg3-JZdKOWPcgZj9ujir7F"
}
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"

params = {
    "jsv": "2.7.4",
    "appKey": "12574478",
    "t": str(time1),
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "timeout": "10000",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp5",
    "data": "{\"appId\":\"34385\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc\\\",\\\"page\\\":1,\\\"n\\\":48,\\\"q\\\":\\\"小米手环9\\\",\\\"qSource\\\":\\\"url\\\",\\\"pageSource\\\":\\\"a21bo.jianhua/a.search_manual.0\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"p4pS\\\":null,\\\"categoryp\\\":\\\"\\\",\\\"ha3Kvpairs\\\":null,\\\"myCNA\\\":\\\"Gwf4HuwY6TYCAXWTCb2wNzA5\\\",\\\"screenResolution\\\":\\\"1728x1117\\\",\\\"userAgent\\\":\\\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36\\\",\\\"couponUnikey\\\":\\\"\\\"}\"}",
    "bx-ua": "231\\u00218u43tAmUppA+job+dA3sru+jUCg32xTcI9QnxMDGrTnM2MlrTwPsP24S7y72KKXu/5b032ZBHPI5DHa9KWgNvWitv2j78RpsRrCyxl9RdrXpog3HVF6BcznaJX7xGUynF8LNUZUI49Brmj447hiF/sV1L5QXXSzpdxHE+tI9Ap68rk38Q1Kd5ElasDpoZ+hScFp8FI66mKj3LJp1T14RzznklqpcT7OBHJsrmfATPUPhAEa+iZD6wK+r+wLepADqk+I9xGdFJuJLOJlCok+++4mWYi++6bKhj0lk3IBDjDj5v8uhhoxaGL2xao4S5cGF+AADlyb4ozjczCswg7wbKVqGdvks4hQpE/gjRpKUqYFi/Akq46b2siF7VTWHpzzuhZ3lhUSfNh6dRinsPNfA3j5kpQYhKv3mqixgZVoIUjbMcgjfFBI9WEvPEZzOswFX47eNYmeqnYgJr2d8f6DhMjyOmt14Ad3X5kUIpK23IT4xgiJQlF5VBzPzlJpkDfxz55GFHIKiGIG0aENnRU4NkI/h6hB/KZjbRIaRpTxAKvRzxFgpnnDAtdy/KxI6n1Sk9qZbsDmXDJ/TSRMjrFvTTeo0xBbyZzUvlo4Af36PeC/l8+pk3aDoHdogxAvp2a7MwNA6GdupqKVBbbEKujfcx6W7JpF8pXZBVMQYOBZ63LAJbqDzqoRHYv6nWfxeWef2t2MbkoUkQXmdWStlTcyOxs9VleJigAxzoaNcjFqWeuRD2VPdn7ReUhpS9QJkHiCejgz+RlOWUwPWZdqsm1upkUUlaUy0QI9WT5JtpA2OsR2AOxQF0dQ03alyW2cjYvAC3MtUpCafBlz1r7Mn7Y2n89GwBp//nDTq2eH3u/uCon+W2g50dFwPjT5MVmlo6fsH3yDWfyhpyQISoFMQN+revJ1+Hme43QXzG+czjfsUq39wRZdKIobzWIY8Xqvi/v3xkRCFwOqTaEzeuHBaknu3rqMruTSSsf2ZdSCVRMgrMRLaYkdOcvPMtdRWKJ3QKmgkUAFmXgzNw2jICFvaKFlK3+qAaovdbSX7HRRKK39CEyByWliiBQRbqUC40O1HTXE/+oM1T34wKFLiXQXGcgkNzOrmOe7MCpkRZxiQAEbxwxl530UM+Beqnbt4cwRFXusBzrPUR57D+DsVIMEMz8kYeTA0zv3DaDi3AfUZD99TBs1Afb6FGfOqLw67KGcNSwIDBQWmysPpVYrh8t5FOjnQVB+VeqfdQWRJOZdauAJ/Zf4Kzw431cYFT8a1DPN1JID2m/h1l3ON0XMlcnlMeGy9OrHh8yj4h7LNAxToYPBw0A7qNh781J4kcLtogrj34Zh7R1YUW27+CF2d0jLoYFvNjUpE+snKpUM28qrbOd9G4uGNsjsRJJgQRZGNZp+BXnlwywZs4uMRcWO/na2nMOE7maolPZY3zRtxRIx5Vok8F//GMNlFz+8JmFmAUWxKZxLStKHJYknJ5Dgqp18enqEV3D7xv+==",
    "bx-umidtoken": "T2gAe7izNprUiqkUMxbqQUGocDLXll82cq0q7yXZt83saI65QI90YvC5aUL0OG5xmtM=",
    "bx_et": "gpTtw8cNGXF9BdYOtCo3mQ_tRTlnZDAZIdR7otXgcpppG94m_NmVkKBp3OjG5O4AkIp2nKdq_s6XhKBDjD0k_C7VlYbxr4AaOxkxLFQbnB_NiGkntJ0k_C746-GkA4Vxsvhdfo6XhwsCZ_bf1O6j9M1PdP1b5swI99WCGs6fCJ6CZ_f_1K_j9B6FGZ16hiGpOfEUP9G1hrKz9so8NlXulrTd6GiH19afTeCOXTO6Jrabg1IOFC6IE5-I3ipOXe0TU1KBwdf934zN5iK6VNTxeVQBaHv19KM8D9tJ7EIkWYEPCFW2eNtKdPQf7FKl4Zn8_6Y9OUSv7AUCBpRBqN8SLrpWtQYNYEH8dt-Gaw19vjZCCiszyUYRfN2lesqs9XE40G1UfWgdQOEH4ECdEfe70oS3T6Bo9cr40G1F9TctTorVxW5.."
}
ctll = execjs.compile(open('./tb_search.js', encoding='utf-8').read())
result = ctll.call('get_f', params.get('data'), cookies.get('_m_h5_tk').split("_")[0], time1)
params['sign'] = result.get("sign")
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.text)
js_str = response.text.replace('mtopjsonp5(',"").replace("})","}");
js = json.loads(js_str)
data = js['data']
itemsArrays = data['itemsArray']
for item in itemsArrays:
    auctionURL = item.get('auctionURL')
    print(auctionURL)