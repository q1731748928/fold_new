import requests


headers = {
    "Host": "api.bilibili.com",
    "sec-ch-ua-platform": "\"macOS\"",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "accept": "*/*",
    "origin": "https://www.bilibili.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.bilibili.com/bangumi/play/ep1524212?from_spmid=666.5.schedule.0",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=1, i"
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
    "b_lsid": "6891881010_196BD9532B8",
    "sid": "767jzza6",
    "CURRENT_FNVAL": "4048"
}
url = "https://api.bilibili.com/x/v2/reply/wbi/main"
params = {
    "oid": "114482755930925",
    "type": "1",
    "mode": "3",
    "pagination_str": "{\"offset\":\"\"}",
    "plat": "1",
    "seek_rpid": "",
    "web_location": "1315875",
    "w_rid": "6e6348357c9c7773a8490afdc166c6cf",
    "wts": "1746939165"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)