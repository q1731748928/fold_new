import requests


headers = {
    "Host": "www.bilibili.com",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://www.bilibili.com/guochuang/index/?from_spmid=666.5.index.0",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "if-none-match": "W/\"vkevkjoht63o0\"",
    "priority": "u=0, i"
}
cookies = {
    "buvid3": "531D4D39-76D6-8AAE-B95C-8C1940B9C2F586589infoc",
    "b_nut": "1718519386",
    "_uuid": "711075687-5454-1106E-423E-ED1F2BC5358286852infoc",
    "enable_web_push": "DISABLE",
    "home_feed_column": "5",
    "DedeUserID": "24752550",
    "DedeUserID__ckMd5": "ce9bf5d98619873f",
    "rpdid": "|(um~kl~|ll~0J'u~u)lumRRl",
    "header_theme_version": "CLOSE",
    "buvid4": "968F8BC1-97FB-2E33-AFF0-302FF3E865EE36799-024052100-QoxZfG9C%2Bye1vDaLi7Juzg%3D%3D",
    "LIVE_BUVID": "AUTO7917195816305731",
    "fingerprint": "ccb9d9c2e8eae53f582f47d8ec928f15",
    "buvid_fp_plain": "undefined",
    "buvid_fp": "ccb9d9c2e8eae53f582f47d8ec928f15",
    "PVID": "3",
    "enable_feed_channel": "ENABLE",
    "CURRENT_QUALITY": "80",
    "browser_resolution": "1728-910",
    "bp_t_offset_24752550": "1064254215473332224",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDcxOTQ2NDMsImlhdCI6MTc0NjkzNTM4MywicGx0IjotMX0.M3nVKOxgPBj0nqVEh8eeGBknQKeAtEpcbO1HWHKFl_Y",
    "bili_ticket_expires": "1747194583",
    "SESSDATA": "c7cbe7e6%2C1762487443%2C01fe1%2A52CjB-mxcq32jFS3W70wY0_Vxd6_GfajIuG2YNGi6BJK-7TKU_YLC1B03F9fRhzqKMjXESVnd3blFyTEc2Q3N0SFlueWhxTHpicEM5cjlZcnJSTzljSUhic3lKazJSVVVFNWY0aXRaUnNQOTJBUURaZWFKQkI1RmJsc3JTTzdDaUpsZ3dZeDc0blRRIIEC",
    "bili_jct": "3ba4afadb6d914e872dc0d9738c098b6",
    "sid": "767jzza6",
    "bmg_af_switch": "1",
    "bmg_src_def_domain": "i0.hdslb.com",
    "b_lsid": "410584103C_196BDF09BEB",
    "CURRENT_FNVAL": "16"
}
url = "https://www.bilibili.com/bangumi/play/ss48315"
params = {
    "from_spmid": "666.16.0.0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)