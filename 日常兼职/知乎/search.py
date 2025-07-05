import urllib

import execjs
import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhihu.com/search?type=content&q=%E5%90%B4%E4%BD%A9%E5%A5%87",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": "2.0_3bg3GZo=+=0C1yTOKMJLT+ahxgoLLUAigOB9wNK+dlUOiiuazz4XTyyOlRb9=pFg",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZs0Y0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTFA9f2Rp_kve8BDVqhGX160XKqBFYPJS9rhVMkeHmkwXGjCc_HUw1yBHLnDeTVMxOe_e1iq2XfbXBKeNG6uxqXBc8ObXmpwS_2rCL993p6Hc11_xmfvNOSqO1VCS1m8pOCGXYAhps2TpKB7FCOgpMFCL_e4cfEcHMzcXCeMp1kLL_kGpmOg_zBqFpWvN_8i3Ob6eqJRcL0uFK4vXGeBXmVgNVigcBKG21e_H0fBwKtUxLhhL8J8eqEbSsA9g9wUcqnhwKwwtsfrxyAwoG_wO_CrXBDBOfGUeYWJOC68es"
}
cookies = {
    "_zap": "a151f011-0efd-402d-82bb-63e7def6b5e3",
    "d_c0": "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518",
    "__snaker__id": "1ZiWvADqW7hOm34T",
    "q_c1": "007f0ed3d6b847f6b6146e1e9ce7655e|1719583526000|1719583526000",
    "_xsrf": "VnM9zYPL0Rgzft96z3b0Vg0LtqvRwq6D",
    "gdxidpyhxdE": "zgsg4UxhKn58kxacYXclEJ2%5Cj3Xn%5CE7Sh6TMzon0RPSU55%2FpjXbMlZPTjwLgmh2YdK1ok0kjrbUrfOeb4tkyj9J%5CYGYLbmTszKCtwhrs8QgsQBNloJyPvuekCi%5Cs9bSu182rThSnRqO63OOwY5jlas%5CyRU%2BRNvQ5rYtLfwavpHjWHD%2BV%3A1745251725231",
    "captcha_session_v2": "2|1:0|10:1745250834|18:captcha_session_v2|88:V3lCV3RsRk5OSUx5K1V2bXZ6elZjU21kakRiVlRyWDh0TC9TbmtjRnRqcE5ESThSdWUvZUVSZ1QrMHNLVktFUQ==|03805153ce2cc91961ee7f18c95a7b5361a59cfc43351716c3b73eff8d792014",
    "captcha_ticket_v2": "2|1:0|10:1745250841|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfZkZIT3hQR3pTYjBCR1JtbUVuOG53TkVYVzE4YzYxKk5wZ2JxLmNKYUFmYlgzTUp3Lk1PS2VnTGV5KlRaY1JQZC5oM2RETWJEVGlsUWRxWU1hb1Eua1F5cXZ6WkVnbV9oMF9BWllQU2lDY1hSTVZFVmZBS3gwWEZVWjhwaDkyaFFXRm9wa2lMM1J2b0VNTkFCUVZiVC51eEtWaUExckFXRDNRUTJTQ1F1SEJBdzR0dG9VKkZXbV9wclUuZUFDTW5XYjBYdlVlaUtWcTJSNlhXZ0p4a204RXlaSUl3UnlqRlBjSnBEOXp4WFUqUzJZbU4qSndEVTlBWnIqNHFpRVZ1TWRBcEgwMXRET1l5bHRTTm5hcm1qa1ptMzFaOXFISHVOT3QwTmtPUVhhU2Q2S3AqNipVb0NhXzFrZkJQaGM0bXFPWnNQdW1aVURsUm53QVoqNVJ4cVR3MmQqakhDc2d4andNSl9sdk1mTXZ1aG9yMjVNbyo4M1ZvSzAuUzJ6bHdsRWRIRlplUjE1bWR2KkFOTnZSWXUwMlB3WllLaTJCbEI4WVUxNFUwVF9rMnA0UFJOa2hTc3hWemN5YlptcThzMVNXeGZlcTZTTTZoVmdFamhTemJ0cVlONVZjRDU0OWwzVEdMMWhDVHpyQzF0aldEQ05NWXBiZENheDZSUHE2NXlEX1NPT1k3N192X2lfMSJ9|52deedab981db9438ec4dd1cb50d322493e147b1f487e65f78c0435be613380d",
    "z_c0": "2|1:0|10:1745250842|4:z_c0|92:Mi4xckMwTUF3QUFBQUFCTUpMTk50N1hHQ1lBQUFCZ0FsVk5Hcmp6YUFBRHR1d0ZsR0hrckhOVk1KNjVHTFN0VFRrV2NR|5a7abab116b19ebe2f8f3a3c5445c49918ca4080850a2565844c717bca48006a",
    "BEC": "8b4a1b0a664dd5d88434ef53342ae417",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745761607,1745817433,1745823373,1745989840",
    "HMACCOUNT": "11F3EEC15F332D20",
    "tst": "r",
    "SESSIONID": "GxPKjUTQvRgcMGGkWqiwnAA8uB7GIyqFkvJXGrw612G",
    "JOID": "U1oRB0qExYLnPbYFLfkjFMxUUlgywLvSqVfgV3zylOOEdfFBQFFzloo-swMotSCgk9JNUjgOwfy-ctN62x8h5n8=",
    "osd": "VlwXAE2Bw4TgOrMDK_4kEcpSVV83xr3VrlLmUXv1keWCcvZERld0kY84tQQvsCamlNVIVD4Jxvm4dNR93hkn4Xg=",
    "__zse_ck": "004_50HWWLazrIY/Anj8wvEb/56taDIwtfndk93/Y=97HFSEVD2I4RhG5ddf5C=Xqr89=Wv8157P1khxC9j9jk/lobR/ApA5s7Qw0ZV=ukeEwHctzC3NiN0lnL0qqYzsJm5j-wloF4CyafftuXA2qyDrSkJNDUj9+bCoG5r1zq69R3iybWnj3B8NjKn3TaLqUP1ZHEOt/CfrUHKFeTGOuA5Q5gGyp1AW+0tGfTZXoxmhFUZjl6blELq1u40p1mMFP52evgwW7KioKNjxgiwtk+/72AI+8p/aZVCzMI8YRyWkdPvs=",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745989853"
}
url = "https://www.zhihu.com/api/v4/search_v3"
params = {
    "gk_version": "gz-gaokao",
    "t": "general",
    "q": "猿人学",
    "correction": "1",
    "offset": "0",
    "limit": "20",
    "filter_fields": "",
    "lc_idx": "0",
    "show_all_topics": "0",
    "search_source": "Normal"
}
encoded_params = url + "?" + urllib.parse.urlencode(params)
ctll = execjs.compile(open('zhihu.js', encoding='utf-8').read())
_96 = ctll.call('get_x_zse_96', encoded_params, headers['x-zst-81'])
headers['x-zse-96'] = _96
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.text)
datas = response.json()['data']
for data in datas:
    if 'object' in data:
        datas = data['object']['data']
        for data in datas:
            excerpt = data['excerpt']
            content = data['content']
            created_time = data['created_time']
            author_id = data['author']['id']
            voteup_count = data['voteup_count']
            print(excerpt, content, created_time, author_id, voteup_count)

