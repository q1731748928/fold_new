# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs
import time


time1 = round(time.time() * 1000)

cookies = {
    'miid': '113103321016989797',
    'thw': 'cn',
    'lgc': 'hebinbin727316511',
    'tracknick': 'hebinbin727316511',
    'wk_cookie2': '11e54270ce964612f111c4c5d668fad5',
    'wk_unb': 'UNN5F4WOdl9Fgg%3D%3D',
    'WAPFDFDTGFG': '%2B4cMKKP%2B8PI%2BNDbN6et2eh14YG5xNoOwMG%2BawQ%3D%3D',
    '_w_app_lg': '0',
    'havana_lgc2_0': 'eyJoaWQiOjMzNDYyMjg2MDAsInNnIjoiODMyNTYxMmQ0Y2RiNDJlZmQ0ZWQxNWRmNmFkZjJjZjUiLCJzaXRlIjowLCJ0b2tlbiI6IjFTZy1tekFKQnhRT016aXpBZ3pyTlZBIn0',
    '_hvn_lgc_': '0',
    'havana_lgc_exp': '1713151205388',
    'sgcookie': 'E100Q6TfLpons7SIJhfS5ap19VF7QspLcCxCwRhJFosmJEES50cNlPTFZcMrJJV5SRIjgSUgO101zbLdlKJJ33Q6DYI%2BsSO6gNjLg6ceKcXQrfOO%2BBOidWh7UGcdc%2Ff3w9Dd',
    'dnk': 'hebinbin727316511',
    '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
    '3PcFlag': '1714398621099',
    'uc3': 'id2=UNN5F4WOdl9Fgg%3D%3D&nk2=CygBYgFPHkPEpNbAQUdOzjk%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3e3WMShTU3VFeWk%3D',
    't': 'd9a6596b0c73a7d7b02ad6061da2892e',
    'uc4': 'nk4=0%40CW%2Fk%2F5MQvRBUodRkXJ9BLJwhLr9h9ihsMPSVaQ%3D%3D&id4=0%40UgQxkF0hTBb70UqO3%2FCA8avhIcuk',
    'xlly_s': '1',
    'cna': '2XK/Hh0+1yICAa8A4NYJbkcd',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '5ee3c13e629f9712a17d06c90d92a31e_1715095517738',
    '_m_h5_tk_enc': '5e0290da248219398d76574e665a6be9',
    'cookie2': '2cb056fdb337025faf5d2109ca008e5d',
    '_tb_token_': 'ee0e54bee1655',
    'isg': 'BKCgHAw50tnxNG0yWXxfhiwqca5yqYRzI-wGPxqxILtOFUA_wrg0A-mjrb2VpTxL',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 't=de5684f55d6fdf83a8fbd198af4d0e92; miid=113103321016989797; thw=cn; lgc=hebinbin727316511; tracknick=hebinbin727316511; mt=ci=-1_0; cna=XGH3HVCTpxICAXH2a8s70Hdr; 3PcFlag=1709214369609; sgcookie=E100VZvwxgW5XLw4%2BbuiJzFOSIqO5vR7EqbU%2Bg8PW5LKV0RX7tlmdFaxyOlpTtoMKbWIUVJRvMvIpqjWUnmcpwcKv0SgMOwe6UbKBQ%2BPEJcwfJ88pD%2B331c77Pl9bHlrDi9V; uc3=nk2=CygBYgFPHkPEpNbAQUdOzjk%3D&vt3=F8dD3erwcZ2nlte4nMc%3D&id2=UNN5F4WOdl9Fgg%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; uc4=nk4=0%40CW%2Fk%2F5MQvRBUodRkXJ9BLJwhLr9gBlDjomBGiA%3D%3D&id4=0%40UgQxkF0hTBb70UqO3%2FE0kBpSFHrY; _cc_=Vq8l%2BKCLiw%3D%3D; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=7ce31d192e69921da02c06db77f6a41e_1709559218560; _m_h5_tk_enc=8adf647cc90d3b69f38685eadfe55ba1; cookie2=22b77bc5399dd9b743bced5af30657d0; _tb_token_=e701f73d3e654; isg=BDc326TzHusXy5pX6skAm49HxiuB_AteCf98lInlxIbrOFZ6kc9WrutTHphm0OPW',
    'pragma': 'no-cache',
    'referer': 'https://uland.taobao.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.5.1',
    'appKey': '12574478',
    't': str(time1),
    # 'sign': '560f58d330a520002adfc0fdd137cde1',
    'api': 'mtop.alimama.abyss.unionpage.get',
    'v': '1.0',
    'AntiCreep': 'true',
    'timeout': '20000',
    'AntiFlood': 'true',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp2',
    'data': '{"biz":"kgb_common","query":"{\\"keyword\\":\\"女装\\",\\"pid\\":\\"430673_1006\\",\\"sbid\\":\\"pcrm\\",\\"refpid\\":\\"mm_26632360_8858797_29866178\\",\\"clk1\\":\\"front_0.nhmixpfuxs\\",\\"page\\":2,\\"count\\":60,\\"offset\\":120}","feature":"predict_desc,promotion_price","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.53.203.55_22132687_1709556425393","ctm":"spm-url:a2e0b.20350158.31919782.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632360_8858797_29866178%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3Df5f9bbff708c8376b6f9d81a9aeb011f%26upsId%3Df5f9bbff708c8376b6f9d81a9aeb011f%26spm%3Da2e0b.20350158.31919782.1%26pnum%3D2"}',
}
sign1 = execjs.compile(open('demo1.js', 'r', encoding='utf-8').read()).call('main123', params['data'], time1)
print(sign1)
params['sign'] = sign1

response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.alimama.abyss.unionpage.get/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
).text
print(response)