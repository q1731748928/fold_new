from curl_cffi import requests

cookies = {
    'azSsQE5NvspcO': '605ns9lubqUyXJhlVtrYF7Jq4QRbpYqKMe7hoA2hN2szsNivXNWgMnfrGy9S.TjX3hCZcRQIH07pHZWd4oYLE4PA',
    'arialoadData': 'false',
    'ariauseGraymode': 'false',
    'azSsQE5NvspcP': '0X36LTadCagr9bMC2FUajqTNb_9wFgW3wAsDfU8V5jV_OSjsGpefMXYFMNXhK.Uv71jaI9KQfGNxrkI0YiWVW5viiMR0r37Zg5WTONEQ6nGx51Q1OV1b7EaZD8gqti4S02rBwQ5SshTXunx_SWheqFkK1Qzjg37XF8MuHtuSCnpGwWsKQsZTizE7HIxbvsVrdDtxJ4n0qDOdaw.djNGEFiCEgsnpS6Kudadx_LPe.qUVVOyuIsEuQayOargXEdOQNbTXUJxb7CVzyvIKDOej4Ozf0HHrh1ybjXJIms_3xwQSQZvD2j5V2d8q5.BQKcBjhBtXkmKez9FhRu51aq1N7yYrIB55sZVfdLViiX.dQRQhXryDI.RH522.fozsHFzeNVi99xD05vXwn8AxrkGoBWFDaq39OL9oTV1uMBoLha40',
}

headers = {
    'Host': 'cdagri.chengdu.gov.cn',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://cdagri.chengdu.gov.cn/nyxx/c109536/zwgk_list.shtml',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Cookie': 'azSsQE5NvspcO=605ns9lubqUyXJhlVtrYF7Jq4QRbpYqKMe7hoA2hN2szsNivXNWgMnfrGy9S.TjX3hCZcRQIH07pHZWd4oYLE4PA; arialoadData=false; ariauseGraymode=false; azSsQE5NvspcP=0X36LTadCagr9bMC2FUajqTNb_9wFgW3wAsDfU8V5jV_OSjsGpefMXYFMNXhK.Uv71jaI9KQfGNxrkI0YiWVW5viiMR0r37Zg5WTONEQ6nGx51Q1OV1b7EaZD8gqti4S02rBwQ5SshTXunx_SWheqFkK1Qzjg37XF8MuHtuSCnpGwWsKQsZTizE7HIxbvsVrdDtxJ4n0qDOdaw.djNGEFiCEgsnpS6Kudadx_LPe.qUVVOyuIsEuQayOargXEdOQNbTXUJxb7CVzyvIKDOej4Ozf0HHrh1ybjXJIms_3xwQSQZvD2j5V2d8q5.BQKcBjhBtXkmKez9FhRu51aq1N7yYrIB55sZVfdLViiX.dQRQhXryDI.RH522.fozsHFzeNVi99xD05vXwn8AxrkGoBWFDaq39OL9oTV1uMBoLha40',
}

response = requests.get('https://cdagri.chengdu.gov.cn/nyxx/c109536/zwgk_list_2.shtml', cookies=cookies, headers=headers)
