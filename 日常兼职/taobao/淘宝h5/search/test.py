import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.taobao.com/?spm=tbpc.mytb_index.1581860521.1.78bd782doRME2A",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "_m_h5_tk": "8e57fb902191f59572688b4d11a8face_1746723465145",
    "_m_h5_tk_enc": "e16302b19518a85ce6b8d587c2e33eee",
    # "_hvn_lgc_": "0",
    # "havana_lgc_exp": "1746746235796",
    # "havana_lgc2_0": "eyJoaWQiOjIyMTk0MDg0NTcyMjIsInNnIjoiNzMxMGNjMDYyODc4YjYyNTVmZWEzZTA3MWE0MGIyOTkiLCJzaXRlIjowLCJ0b2tlbiI6IjE5NjRPb1B5UWZ4b1RDbmV6ZlNIR0lRIn0",
    # "uc1": "cookie21=WqG3DMC9Eman&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&cookie14=UoYaje6Pg1KFKA%3D%3D",
    # "isg": "BLm5Vdlb9bTFZ6f54cDDAI2pyCOTxq14cmDhqtvuNeBfYtn0Ixa9SCeh5maUXkWw",
    # "tfstk": "glBrKMb6fpbbfULJZt9E_FxJGmJJdpz1t9TBxMjHVUYoFYghgGQePkFJFs8FoZ8kR3TSYJ7NAud72MmexZ_c8BEJReYFRMf7cRw12gppKpz_CR9GK3hfUe0BKLp0cnOhBRw12gfhmKebC9ZW6KT-tvbHZIjDjEYHKQcu0ExeXX0l-wq2nHKwq4AHtm0DAEYHKpbhmo-Bo3vHKfEvgCy2jQqIEgxealRXaFjkuvSR33ArwgYqKvXVaQ8iLEknKt-PD2lCAY2wo_1hFKXuo29cXs_k0dyEYn5NmLxPJRHJEGjctQWUOcLdgif6gsn72nWPb9-wMW0BRCWcFLC47ATGMMXeigUZ6n1hfT1FPrHHP1ScuC6jlA9cUaWkgdjy62K0F-Bda2cHZnK25or2fn8uaQztLmhK9IbB0FZR2XhpZQ-25orq9XdD4n8_2gC..",
    # "cnaui": "2219408457222",
    # "aui": "2219408457222"
}
url = "https://h5api.m.taobao.com/h5/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedresv2/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": "1746715150293",
    "sign": "14f095caddbbf1f0d8febb625c8f4a4b",
    "api": "mtop.tmall.kangaroo.core.service.route.AldLampServiceFixedResV2",
    "v": "1.0",
    "timeout": "3000",
    "dataType": "jsonp",
    "valueType": "original",
    "jsonpIncPrefix": "tbpc",
    "ttid": "1@tbwang_mac_1.0.0#pc",
    "type": "originaljsonp",
    "callback": "mtopjsonptbpc2",
    "data": "{\"params\":\"{\\\"resId\\\":\\\"33974682,34552784,35329530\\\",\\\"bizId\\\":\\\"443,443,443\\\"}\"}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)