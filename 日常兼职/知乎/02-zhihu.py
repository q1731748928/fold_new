import urllib

import execjs
import requests

# 回答内容+作者id+回答时间+点赞数，不需要评论部分。计大约6万条数据。

cookies = {
    "_zap": "a151f011-0efd-402d-82bb-63e7def6b5e3",
    "d_c0": "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518",
    "__snaker__id": "1ZiWvADqW7hOm34T",
    "q_c1": "007f0ed3d6b847f6b6146e1e9ce7655e|1719583526000|1719583526000",
    "_xsrf": "VnM9zYPL0Rgzft96z3b0Vg0LtqvRwq6D",
    "__zse_ck": "004_d3Ua=EMC3kUbZi22ILTyedjNFlmN6ZBClmedkkfMQ0/rxUF8xwFh1bWVEfaVWZcb2Ce0uIXK6dMGLpJlL/08LUI8HVBkvrUpQdcoO5U6GKn5kzocL1i7eBfF6QUx5MoC-upqOaDmLbIxra9/gpmAulYDIyySG5kAPsgSR7Qc0kWsZg9YOjVOFb9ty4U7WotYxecrp5+vLDH6ZIyWFoISRxS1BXiap+3Nxg+gTzowv7SeVaqT+TXySCbRqewMR/+WdgHUstTOqet4eRuQmiMboPgxGScDVBHXvDrrIZgE3ei0=",
    "tst": "r",
    "gdxidpyhxdE": "zgsg4UxhKn58kxacYXclEJ2%5Cj3Xn%5CE7Sh6TMzon0RPSU55%2FpjXbMlZPTjwLgmh2YdK1ok0kjrbUrfOeb4tkyj9J%5CYGYLbmTszKCtwhrs8QgsQBNloJyPvuekCi%5Cs9bSu182rThSnRqO63OOwY5jlas%5CyRU%2BRNvQ5rYtLfwavpHjWHD%2BV%3A1745251725231",
    "captcha_session_v2": "2|1:0|10:1745250834|18:captcha_session_v2|88:V3lCV3RsRk5OSUx5K1V2bXZ6elZjU21kakRiVlRyWDh0TC9TbmtjRnRqcE5ESThSdWUvZUVSZ1QrMHNLVktFUQ==|03805153ce2cc91961ee7f18c95a7b5361a59cfc43351716c3b73eff8d792014",
    "captcha_ticket_v2": "2|1:0|10:1745250841|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfZkZIT3hQR3pTYjBCR1JtbUVuOG53TkVYVzE4YzYxKk5wZ2JxLmNKYUFmYlgzTUp3Lk1PS2VnTGV5KlRaY1JQZC5oM2RETWJEVGlsUWRxWU1hb1Eua1F5cXZ6WkVnbV9oMF9BWllQU2lDY1hSTVZFVmZBS3gwWEZVWjhwaDkyaFFXRm9wa2lMM1J2b0VNTkFCUVZiVC51eEtWaUExckFXRDNRUTJTQ1F1SEJBdzR0dG9VKkZXbV9wclUuZUFDTW5XYjBYdlVlaUtWcTJSNlhXZ0p4a204RXlaSUl3UnlqRlBjSnBEOXp4WFUqUzJZbU4qSndEVTlBWnIqNHFpRVZ1TWRBcEgwMXRET1l5bHRTTm5hcm1qa1ptMzFaOXFISHVOT3QwTmtPUVhhU2Q2S3AqNipVb0NhXzFrZkJQaGM0bXFPWnNQdW1aVURsUm53QVoqNVJ4cVR3MmQqakhDc2d4andNSl9sdk1mTXZ1aG9yMjVNbyo4M1ZvSzAuUzJ6bHdsRWRIRlplUjE1bWR2KkFOTnZSWXUwMlB3WllLaTJCbEI4WVUxNFUwVF9rMnA0UFJOa2hTc3hWemN5YlptcThzMVNXeGZlcTZTTTZoVmdFamhTemJ0cVlONVZjRDU0OWwzVEdMMWhDVHpyQzF0aldEQ05NWXBiZENheDZSUHE2NXlEX1NPT1k3N192X2lfMSJ9|52deedab981db9438ec4dd1cb50d322493e147b1f487e65f78c0435be613380d",
    "z_c0": "2|1:0|10:1745250842|4:z_c0|92:Mi4xckMwTUF3QUFBQUFCTUpMTk50N1hHQ1lBQUFCZ0FsVk5Hcmp6YUFBRHR1d0ZsR0hrckhOVk1KNjVHTFN0VFRrV2NR|5a7abab116b19ebe2f8f3a3c5445c49918ca4080850a2565844c717bca48006a",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1744869283,1745210417,1745250583,1745278129",
    "HMACCOUNT": "11F3EEC15F332D20",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745286659",
    "BEC": "8ce9e721fafad59a55ed220f1ad7f253"
}
url = "https://www.zhihu.com/api/v4/questions/277135177/feeds?"
sum = 0
max_limit = 500
params = {
    "cursor": "640183da45c6acbb2590d0b5f919593a",
    "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
    "offset": "",
    "limit": str(max_limit),
    "order": "default",
    "ws_qiangzhisafe": "0",
}
encoded_params = url + urllib.parse.urlencode(params)
# print(encoded_params)
# print(encoded_params)
ctll = execjs.compile(open('zhihu.js', encoding='utf-8').read())
_para = "3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YDR0ERtuQ6fqBX2ZgGemkUO17HkmuqOBpD_BWgN97QPY39wfZhRTS0tuo0Yqw_V1ZULBVCN9QuV_IHkqsv90su2x77wTbvXTFJLY7QSYebOfIAt12CXGEgOfUcXIIRFZcL_8ArS_jvOYTiFTr7gTdqfPH_P_aqkTSQUqS8tpS8FqM8FqSQUqS8tpS8FqM8FqSQUqS8tpS8FqM8FqSQUqS8tpS0fzVXXfuBH1jU2XPUHmQUtL69OCyhS_qqeGwhcYEugLY9w9ou3YYgXOsgg96X3xHw3CzwtLrUSVp9x9ZupOyDpfDvOyYBp8e7S8uJxqIbUGDULsWCcTVeY_TJxmaD3XbTXfXDwy_hgYCbXfDce_GvNLz9HKfqgsEGpMHgVf8CoMxU2OQ_OM4CO0_Jg_sGHYEJXMk9NKTqL9b0wVI9t1hJS1eRxqSgN8VJOC"
result = ctll.call('get_x_zse_96', encoded_params, _para)
# print(encoded_params)
# print(result)
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhihu.com/question/277135177",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": str(result),
    "x-zst-81": _para
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.json())
next = response.json()['paging']['next']
print("下页索引页面:", next)
print(response.json())
datas = response.json()['data']
last_cursor = ""
# for data in datas:
for i in range(len(datas)):
    sum += 1
    data = datas[i]
    excerpt = data['target']['excerpt']
    content = data['target']['content']
    print(excerpt)
    print("\n")
    if i == (len(datas) - 1):
        last_cursor = data['cursor']
        print(last_cursor)

print(sum)
# for excerpt in excerpts:
#     print(excerpt)
# content = response.json()['data']['content']
# print(excerpt)
# print("\n")
# print(content)
# print(response.text)101_3_3.0+/api/v4/questions/277135177/feeds?cursor=7e3ec17e3cc4bcce3c3ea77d520e5239&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=7&order=default&platform=desktop&session_id=1745286661730409977&ws_qiangzhisafe=0+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog%3D%7C1719583518+3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YDR0ERtuQ6fqBX2ZgGemkUO17HkmuqOBpD_BWgN97QPY39wfZhRTS0tuo0Yqw_V1ZULBVCN9QuV_IHkqsv90su2x77wTbvXTFJLY7QSYebOfIAt12CXGEgOfUcXIIRFZcL_8ArS_jvOYTiFTr7gTdqfPH_P_aqkTSQUqS8tpS8FqM8FqSQUqS8tpS8FqM8FqSQUqS8tpS8FqM8FqSQUqS8tpS0fzVXCBgUpMfCem-cLKUrXfb4oGxbOG2htLihOBVgUK19xsQbe0cUN_gv3mNh2LWuFOkupfwvr0icX8yBFCvhHBico1HqwVe9VyhGH8OGQC6QXY-CcTVeYLgvHLQhcmwvOYYJXYTq9CoBX9sq30jhH8gco0jDgYOu3YB4w1PvLCEBxxbJx0QUwMTvOq27SBIbHq4Gg_NheCW9OKS9pGY0S9nrVZVUFBNvOC
# print(response)
