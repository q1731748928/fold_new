import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "origin": "https://x-edu-pdfjs.ykt.eduyun.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "range": "bytes=100139008-100204543",
    "referer": "https://x-edu-pdfjs.ykt.eduyun.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-nd-auth": "MAC id=\"7F938B205F876FC3C7550081F114A1A44EDF73D57C282D9FE1ECA21FA42141F3D7C080C6939ACCE76212AA04733DD873092E7EF4943088AC\",nonce=\"1747961696422:6VC3GGLN\",mac=\"dJCdONZEmZXaTD0WfxDxEWm2TJenMsacdI H3c/6llc=\""
}
url = "https://x-edu-pdfjs.ykt.eduyun.cn/generic/web/viewer.html"
params = {
    "isPreview": "1",
    "file": "https://r1-ndr-private.ykt.cbern.com.cn/edu_product/esp/assets/5bd0a1a5-4465-48f7-ac81-825b4b941eea.pkg/义务教育教科书•英语_三年级_下册_北京出版社_1739512502101.pdf",
    "headers": "{\"X-ND-AUTH\":\"MAC id=\\\"7F938B205F876FC3C7550081F114A1A44EDF73D57C282D9FE1ECA21FA42141F3D7C080C6939ACCE76212AA04733DD873092E7EF4943088AC\\\",nonce=\\\"1747961959934:8RLBMGL8\\\",mac=\\\"ggADwm5/7I1JByjX7eHSTrw4rpNDkv6sDPFiDCTQmqk=\\\"\"}"
}
response = requests.get(url, headers=headers, params=params)
with open(f"./pdf/test.pdf", 'wb') as f:
    f.write(response.content)
print('下载完成')