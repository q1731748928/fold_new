import json
import re

import requests
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://s.taobao.com/",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
cookies = {
    "wk_cookie2": "13c615441b604430dbdf0ecff7fc93d1",
    "wk_unb": "UojQPGlx7CSOTg%3D%3D",
    "cookie2": "26d1f5d5e387d5255ee927f6e43abffd",
    "_m_h5_tk": "0befb941f9bd9caa7f465cc6906f0856_1722346911252",
    "_m_h5_tk_enc": "c1e823d64a3866f0600162482689c16f",
    "linezing_session": "XuBC2RoKNC5enBNGPfr4HuwH_1722340594214MH6c_1",
    "3PcFlag": "1722341494621",
    "sgcookie": "E100l01eQ3oPGV2ZRHsvaOV6lbACb95KQRi9a9Uvz6DpI5hpUQTV5EzaMQeuYfd11egZ8f8WKg0OGRQQwrnUsklIcxDjKhCuxjagf%2BjCCPBJnhNxeNSdAAyr8jvFs%2F9%2FZ%2BT0",
    "tracknick": "",
    "cna": "nzwvH1gJxh0CAXWTCDroOpVk",
    "JSESSIONID": "3FDD5E77B6C0BBA4E1008244B95343B4",
    "isg": "BN3d4pYYZ9RTSgMAXGBUX1Vd7L_X-hFMcMMeqJ-jCzRJVv-IZ08JHIfPgErQyikE",
    "tfstk": "fECr9ns65Bjjfu6H0nOeu_7qBSOJ6CE_a6tB-wbHP3xkVwYHTijQy3_32M5emwB7ypZ-84CVbXG728QnTBO3flN_1aUJ9Bq1Fj7xC0LBJexnAHY0VqAUGlN_1a2kyB_0fyCi5etHRBYkKBV0ueTnZHjHEIVDDeLnqecuuZxv-BmnE3ADmUTp-bc_RKJagFvu7aEHF63OmL-GuRhnTkTofh_k0Xch7EpzQaxqtXfVH1YZAhPqmn_hW9vVTSGv9Z6NY9j0-XxFnFSw5gNmaBXc01JGkllJ4tjRTQ9TT28VQZjPNZzI3MScWOdlZkhW29bctn1uRX-GCNd2k6ZxZHWcK_9J90qyu_7NT9SP0DL0KsCdUDDeEEL2frzcij_LW4H-RSDKpKjBuhaRyvHpEL82frzqpvp-OE-_yaC.."
}
url = "https://shopsearch.taobao.com/search"
params = {
    "initiative_id": "staobaoz_20240630",
    "q": "程十安的店",
    "spm": "a21n57.1"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.cookies)

response = requests.get(url, headers=headers, cookies=cookies, params=params).text

print(response)
# 使用正则表达式提取第二个 < script > 内容
script_regex = r"<script.*?>(.*?)</script>"
scripts = re.findall(script_regex, response, re.DOTALL)

# 如果有至少两个 <script> 标签
if len(scripts) >= 2:
    second_script_content = scripts[1].strip()

    # 使用正则表达式找到 shoplist 的 JSON 数据
    shoplist_regex = r"{\s*\"data\"\s*:\s*({.*?})\s*}"
    shoplist_match = re.search(shoplist_regex, second_script_content, re.DOTALL)

    if shoplist_match:
        shoplist_json = shoplist_match.group(1)
        shoplist_data = json.loads(shoplist_json)
        # 打印解析后的 shoplist 数据
        print(shoplist_data)
    else:
        print("No shoplist JSON found in the second <script> tag.")
else:
    print("No second <script> tag found.")

# print(response)
# tree = etree.HTML(response)
# hrefs = tree.xpath('//li[@class="list-info icon-5zhe"]//h4//a[1]/@href')
# print(hrefs)