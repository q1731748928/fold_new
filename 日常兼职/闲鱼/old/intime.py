import requests


headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.goofish.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.goofish.com/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
cookies = {
    "cna": "nqV+IIqtKjoBASQOA5CIE9nT",
    "_samesite_flag_": "true",
    "cookie2": "18b67e595a8ab34a7180e5c92c2e8efa",
    "t": "4a5c37ffbcc87f6313d26c0e63bf171b",
    "_tb_token_": "ee355ab30e573",
    "xlly_s": "1",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "bf8b158f1b150b26e91259960e2f7408_1744300302828",
    "_m_h5_tk_enc": "8edf2ac0c8ea712f3c17d1ed28375bd5",
    "tfstk": "gvbrgM661eXb5UbzKIYEbJP6PA8JrU2sLw9Bt6fHNLvoP4Mh0OXvFMsWFXSVKtKWEw5K8Bfhp7pQwo1RweL3CR6U5_C8FU7ija-niKfvOBv3c3vm08lgCRa_lucD88y1FqTtdoRpnQAHx3V4oQdp-BxkqSJDTCnnE9Y3gSRB9QDk-QcDiBdB-pXH-S5DHBlZDn-auCxuOgv8HUmsZ3vGZKun7fdyqo1SA2uFcQ-Pntv2aQ72a3JMD01tUN5GZNdFJ5meL1IlFIBU7-8czT7k0ezEkU1NmT-V4Ju2DifO-nSYQcCOZTSMja44Mn7R1UvVJW3pEg1hRH7uIX9lyT_2XwHzhps1GaxVI-gVpHSljUbUQrjPkvd0PrQd4vmeqId2CSP2Nk9pV6eVATiKvnXBgdNRwDnpq3R2CSPqvDKDwIJ_w_C.."
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlehome.home.webpc.feed/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "34839810",
    "t": "1744294039980",
    "sign": "57ce0702a51927e4041a9f48ed0ef808",
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlehome.home.webpc.feed",
    "sessionOption": "AutoLoginOnly",
    "spm_cnt": "a21ybx.home.0.0"
}
data = {
    "data": "{\"itemId\":\"\",\"pageSize\":30,\"pageNumber\":1,\"machId\":\"\"}"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)