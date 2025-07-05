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
    "cookie2": "1e1cb58daadce2a15fa36eb105d28a15",
    "t": "fc8d259d200531c5e2e8e488f059379c",
    "_tb_token_": "5338b7eeeb97f",
    "thw": "xx",
    "xlly_s": "1",
    "wk_cookie2": "18c174b097e1ebe54db713e656b37e1e",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "8e57fb902191f59572688b4d11a8face_1746723465145",
    "_m_h5_tk_enc": "e16302b19518a85ce6b8d587c2e33eee",
    "mt": "ci=0_0",
    "3PcFlag": "1746715121396",
    "cna": "9nKjIKL8oGsBASQOA5Br4lQA",
    "wk_unb": "UUpgT7v4dXzD0aXquQ%3D%3D",
    "lgc": "tb749767430786",
    "cancelledSubSites": "empty",
    "dnk": "tb749767430786",
    "tracknick": "tb749767430786",
    "sn": "",
    "_hvn_lgc_": "0",
    "havana_lgc2_0": "eyJoaWQiOjIyMTk0MDg0NTcyMjIsInNnIjoiNzMxMGNjMDYyODc4YjYyNTVmZWEzZTA3MWE0MGIyOTkiLCJzaXRlIjowLCJ0b2tlbiI6IjE5NjRPb1B5UWZ4b1RDbmV6ZlNIR0lRIn0",
    "cnaui": "2219408457222",
    "aui": "2219408457222",
    "bxuab": "0",
    "x5sectag": "580266",
    "_samesite_flag_": "true",
    "sgcookie": "E100qqMqlGh8uKjFUxmklBvyzSnYuy1LaAfUJiX19rlFQmVE3JChxoLKm46ShaH8Df3SDkXk%2F2uYw5Oh5RDzUBuUlh0aAfw9G%2FDvqfASpiToFkI%3D",
    "havana_lgc_exp": "1777820834930",
    "unb": "2219408457222",
    "uc1": "cookie14=UoYaje6PgANPnA%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=Vq8l%2BKCLiYYu&existShop=false&pas=0",
    "uc3": "vt3=F8dD2EXbszFA0C93Lew%3D&nk2=F5RCYRLAR%2F32TSkR%2BHY%3D&id2=UUpgT7v4dXzD0aXquQ%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
    "csg": "b0bbabb9",
    "cookie17": "UUpgT7v4dXzD0aXquQ%3D%3D",
    "skt": "ca34f2de71e6ccc0",
    "existShop": "MTc0NjcxNjgzNA%3D%3D",
    "uc4": "id4=0%40U2gqwAR2GnijMUO5CRsSWOiqAJiEGtCK&nk4=0%40FY4Jj10%2B9qPyDQ1GSKMdEYaLpAcDnftWSg%3D%3D",
    "_cc_": "V32FPkk%2Fhw%3D%3D",
    "_l_g_": "Ug%3D%3D",
    "sg": "62e",
    "_nk_": "tb749767430786",
    "cookie1": "BqU5BnGEYetP5%2BbfYKWIsBYTMYkfUTTQSkWu0drMmTY%3D",
    "sdkSilent": "1746803234934",
    "havana_sdkSilent": "1746803234934",
    "x5sec": "7b2274223a313734363731363834302c22733b32223a2265326630306365393238353238336663222c22617365727665723b33223a22307c434b475238384147454a482f6d6f3048476738794d6a45354e4441344e4455334d6a49794f7a496942584e6a5a57356c4d4c375270717747227d",
    "isg": "BDQ0a9au4HuCiXpu1NsWP7CSBfSmDVj3f-vcnc6U8r9COdWD9h1phxS4uXHhxZBP",
    "tfstk": "gdntBwvahpBOwWoTKA8hoYGC9L9HEeDZpfk5mSVGlXhKsYggSxN0DjhxM54X_lmx9fDSSPDjm-iYbD0Gm5AaDxGuDQAkq3DZQkrXZQ0z0noLc-t0Ge46Ba6kBQAkqHY1dod9Zjfx4u9L3Ww_h-sXpkw8Howf5jNQR8wl1oGjGW1QQRsfCPZfRHNUhoNjGo9LAWyYcSGOEgNBCSsxz93lF_YTGisjvRU6-ANCcJoLBPFSCDIfcOyTW7M_9QqHv0ax6PnHX_ytRYhgBj-Pblax54ZsDQKTAYun1JhXwZFIycoYrcdRz5iagbEsJBsTclotrzrvyOynXvizkcROA5hEd4qZVBSxNvDobyovw6NqS8rQB2pfR5af4Zmo2PZGZ7ec5ppduZz_LN6Bv5RHMjlgp7vONZ74-9yLZpLNuZz_LJFkBp7VuyXF."
}
url = "https://h5api.m.tmall.com/h5/mtop.taobao.rate.detaillist.get/6.0/"

page_no = 0
count = 0
auctionNumId = 820916084335
while True:
    page_no += 1
    params = {
        "jsv": "2.7.4",
        "appKey": "12574478",
        "t": str(time1),
        "api": "mtop.taobao.rate.detaillist.get",
        "v": "6.0",
        "isSec": "0",
        "ecode": "1",
        "timeout": "20000",
        "type": "jsonp",
        "dataType": "jsonp",
        "jsonpIncPrefix": "pcdetail",
        "callback": "mtopjsonppcdetail3",
        "data": f'{{"showTrueCount":false,"auctionNumId":{auctionNumId},"pageNo":{page_no},"pageSize":50,"rateType":"","searchImpr":"-8","orderType":"","expression":"","rateSrc":"pc_rate_list"}}'

    }
    ctll = execjs.compile(open('/Users/hejie/PycharmProjects/turing_exec/日常兼职/taobao/淘宝h5/search/tb_search.js', encoding='utf-8').read())
    result = ctll.call('get_f', params.get('data'), cookies.get('_m_h5_tk').split("_")[0], time1)
    params['sign'] = result.get("sign")
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    time.sleep(wait_time)
    js_str = response.text.replace('mtopjsonppcdetail3(',"").replace("})","}");
    print(js_str)
    js = json.loads(js_str)
    data = js['data']
    if 'rateList' in data:
        count += 1
        rateLists = data['rateList']
        if rateLists == []:
            break
        for rateList in rateLists:
            feedback = rateList.get('feedback')
            print(str(page_no) + ":" + str(feedback))
print(count)