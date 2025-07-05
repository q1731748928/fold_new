import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
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
    "x-zse-96": "2.0_2VHrkSHh=YgqmotpuMdpDLG7b5SxujsurGduf61FsnZWIiwH3mN=ANbSS24gGZUh",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZs0Y0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTF7S0LhSsIvHBGQX0bqr9pgcBeTLfvge_DrHqahxKHwpO5ULO60VfgDoBLbSTVeH_9vCKZ9csQ0pLZBofQue0cqoMwC2GshXLFqLqLDwLTGNMB9C0fvo8Cwt1yvSmmiX0TUxKywCmJB28YBcCCG_Bo8ofuvCOG_2CbeXBUDOfAJO_vGpmVg_zhUpK-B2fdBcmqCOONwNOWBoYBCC_IhcmIuwYarNK2Uo0oUgM0BwKBgc117H9-Uw0OCCmXhXBdhLZUgLZfcxseMcqBhS8NuVqhGeXEBHqRww1CUOLeQxs"
}
cookies = {
    "_xsrf": "VfXRcdZbSdiNpzsMS2GSCG9Z0flm9YsJ",
    "__zse_ck": "004_WdIn8oBn9OBD4EEYndE1Tr2BSatp3YEaxGEdR6QUeTiPACVJXxsF=UhT1jOmUEoaXmuAbi=FryFjlcCaO/gPXoMUjU0miemU7u/iKzen26e4=9WeZAaRL7Xt6vliI21q-YEdHtdPeAAGkSQumT/EL9aw+GSVphDx/KaAEpQIn9qr6wxAt/vSLpA3rvp2p/THocvLSP7MBflxAPe8RoXsjaoezFMEr8lZQ/AqrOwY6FMymnED7lIozsHM8aRxJnGsqsJVF/eCz8OG2RtsiNpwMbbEfvg0lwHVO7Y7p+D+VVbg=",
    "_zap": "951612f8-eede-4175-aeee-786d7b2832c3",
    "d_c0": "ZYMTMkk2WBqPTr7OinvheEW9GFBszJk54AQ=|1745376409",
    "gdxidpyhxdE": "fGIW8X%2FXSvqbuwoA0MEoxzBgg%5CDTv%5C6HAad%2F28Js78THZUMpJLR5w157VWVsaaaPeL1pcxt7E7Qw6jRh3EcMmon2Tbc57Tg08P733j9aQWo%2BMuvkPSZiG7e%2F8UxtdChzyzVpc%5CzcHb5Zv%2BdnZ0jmsLz0fxCxHP%5CM9wpiRaNf0hHfpzDK%3A1745377311505",
    "captcha_session_v2": "2|1:0|10:1745376430|18:captcha_session_v2|88:WHZucnpJNGxOU3JRZlBUeHh5ckp4cjdBaWFOYWQ3NldLeVBYMEpjTFRsYmZ2UmVRZzhRZ05Pd09BRGdacUZMMQ==|34fda641479a1c54821ec06b377890d4072345fc2faeb39c2189d54f71667ec9",
    "captcha_ticket_v2": "2|1:0|10:1745376441|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfY2V2dUY4S3doX3JtWWJBYjBtajlJMzBKbHhfbjFQdGx4SzJYa2xMTEVkei5jYUM4S1FVdEhpVUlfTHhmM3FkQU1CME5OX01BZG9yZVZZQXRBV0d1R1NzT0dXRXRoSjRjTHc1dFV1dnRsUUxDaWhXWWkyS2dlcnJqUEFiZXg4djN5SGhfUXA4NDVCT2E5NjI1bVRMUXVMYTVuclJiWkRxYWhnSDB0MGtvaFNDeWRrX3pyT2lielNBWWpGd3hsanF4eVIqR2JhODZIdHZnNUtvVTBfR1Z5U3RMUEFFeVB6dEZLdk9BYVdMMmhOQWdCREdic2pTOFdPaTlzR2tfa2tTSGxMS3pFZExvQ2pITzFxdmMxYWYxMDVfSmlKdnlnNGFIVVVQRlJmcEZ6TzVaKm5uRm9vandpT1ZJcVUqbUJsR0lxdHFTdktlREZQKmR4NXF3VmJqeGZjbG0qbkFzSFFiaHZjWEU2Mm9MZjljMWJPZm8wZmpJTEcwUXZSYW9LcnBGTHo4NjZBTHouWktUc1FHeFJBQ2FpWEl6Z2MyZEwxMVhyYVZIS2FheGc4blJ4bkZRVEpRTENvMVc1bnhPa2hZcHguTjlXUypZQlNlMWpqSUxRYldqMlBUa2p6LnRobWR3T2JKYkpTemNRdXlQM3RzR25yVTNzVypyb0pKa2NqRXpBb1lULlg3N192X2lfMSJ9|9424418965d78ef225225f4cfd8b4e60c0b39dbcf420283112a519d5fa64b548",
    "z_c0": "2|1:0|10:1745376468|4:z_c0|92:Mi4xcVBCZ1hnQUFBQUJsZ3hNeVNUWllHaVlBQUFCZ0FsVk4wNkwxYUFBaUNGaEZMbmx4TkZ2UlcxTjQ3NG1hazY3cXdR|2e2d8b36c855a640b8a9d4b0e6748facb3c453d3d99c23875e007f6aab49a4e4",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745379780,1745379863,1745380111,1745380355",
    "HMACCOUNT": "22F445EBADF206B7",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1745380944",
    "BEC": "d892da65acb7e34c89a3073e8fa2254f"
}
url = "https://www.zhihu.com/api/v4/questions/277135177/feeds"
params = {
    "cursor": "640183da45c6acbb2076fbbaf919593a",
    "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
    "limit": "5",
    "offset": "192",
    "order": "default",
    "platform": "desktop",
    "session_id": "1745380942333531456",
    "ws_qiangzhisafe": "0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

next = response.json()['paging']['next']
print(response.json())
print(next)