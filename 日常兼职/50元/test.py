import time

import requests
from bs4 import BeautifulSoup
import random
headers = {
    'User-Agent': random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
    ]),
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br'
}

base_url = "https://news.cctv.com/china/"
params = {
    'q': '关键词【经济】',
    'c': 'news',
    'range': 'title',
    'num': 20,
    'col': '1_7',
    '_': str(int(time.time() * 1000)),  # 防缓存
    'callback': 'jsonp_callback'
}

resp = requests.get(base_url, params=params, headers=headers, timeout=20)
print(resp.url)
resp.encoding = 'utf-8'
print(resp.text)
soup = BeautifulSoup(resp.text, 'lxml')
print(soup.select('.result'))
