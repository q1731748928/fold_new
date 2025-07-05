import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://xueqiu.com/today",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "cookiesu": "671744296650662",
    "device_id": "ad434d5aff8b96c2c79a5ff950cc583b",
    "s": "c013a7ge1o",
    "acw_tc": "ac11000117443508898026736e00317d547c81927ff0c0c3947ca59df28973",
    "xq_a_token": "8227a6f1f070ca10a573ea273e25da157b017b89",
    "xqat": "8227a6f1f070ca10a573ea273e25da157b017b89",
    "xq_r_token": "8c19700a9bde6cebd6eb64490168b410844f0b33",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc0NjA2MTE1OSwiY3RtIjoxNzQ0MzUwODU5OTg3LCJjaWQiOiJkOWQwbjRBWnVwIn0.JmDBlfAW1Rwypu6sxBaP7IHU-6KTPoPfSvEIop8jQ6cuMwLSKhbkMJiBlO9tZIOMq6FBmPlHZt42Yafa2Cyn85OXgJLwxCtgpmGdDQ7d_OKWONhElFa6E8CEjZ7ElX2XbC4lEOczasvLltujjYqGR_izwnvU_NcCbC3S3cRMLBsS6-14eBFbiDUGRgM-h677dWospLpAi-jfgVDQg-oBnEPJATvPvOaLBH-FswW9OFp2hOaBjYXyKWfRy2mBGiu_ff5wchnYLkA8hfA0W2WK-DjoQ-C8FeKAqiKF5FViU_WJsl2q6EjYkEaxzPf1ZtPC3Aw27TGjhGUk_BaUjxXqag",
    "u": "671744296650662",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1744296651,1744350888",
    "HMACCOUNT": "788AC10A3780E5E2",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1744350894",
    ".thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7": "h3g6mVXpDwAfLWzB4zpHS4C8BGcSooBCYmqsNVYjr5X9FQJ/uh+1FHjiBnrMDIJiZ5tLJula0MS9hMf5NXWfiQ%3D%3D",
    "ssxmod_itna": "QqmxBDnD9Qq9G0D2DRrrD0iDpxTeDXDUkqiQGgDYq7=GFYDCODF3PW4BKm5G80QAGGD43G0OBKD/m0qeDZDGFdDqx0oi6i7Du=PB00Tbppe0rrR=C5F3KybcKbtG4Kg2Lvk67oYqxAoYD7QDb4DyDGU=DG6k4xGGf4GwDGoD34DiDDP5xDttaCqD7gbYEeTV9BiYWlbDm8w4TOqDmwFDnhWNxZbVYBbDG8FDzkWDff0TBCwDxY=DQwg=bgbDj+9T7FB4xYpm+W7hxBj1=Qi7njuNy7kiKAtyxhLqDhvpKGXG07DPiDe44wDxhxQE1KG5H0Dgix3BK2LhCgHyDqAEsCgxhBk+wCPRCGDowoxdhQohdhxqsgmb0+EO5q05noYeYelG4FDxfh5hizWiDD",
    "ssxmod_itna2": "QqmxBDnD9Qq9G0D2DRrrD0iDpxTeDXDUkqiQGgDYq7=GFYDCODF3PW4BKm5G80QAGGD43G0ODeDAD=D5NiW447P4B0oa+4q7D0HLLbYY6hyL3KT0LxjliMaR8o7tLDxtUbKY6ph9PBtDPMoyaqYxzHc4rw1YKM69stfB7q0pmgQI4C19d+gDHLcbqO+yGt8ApWoPNKBP4WZSv++pz=ZIfr+PpyKk86YhUmZ+ftZ9LYDOw7=eaWBP12RTOwPMhshpG4T0Ogxj47C5IVK97y2wzw5kp+VZ71ZMzNi=H+o89aFVxM4lXPFgLV3F1x1OOHDjFEx1cbOxCHb+D/xxEfhgfPvrFlq7gEbtRrgg1aDdZRazS+afPlBa1wrzh58Q3MSPSr5UgWvSs+nhb2r9OTMhDDMN4ONBYkEOdq+5/o=9gri3=iCN=OzDW4dZF0L+DqOTCmDQqUO7+SIpSPwQwPSiluA11z0k786IVQjOn6DwvFTpwEaquTvWQxcHDIWqq7OiTFW3j6s=djkw3H6P4bzsb48QmqDm7Oth1=jbUqY+fh3zb+lxRUkn7SNqT16CujCFNpzoZ3e280ON/gtsrdqbQ9r4bnDo4AHjaK3zSxx1orRhp1edF1TC8xUOf38EG75e7Dy0wGqXbhMLTwhslIHTNviibNhodB2l5hbbgYGDe7DVS5xyi5ZDqWDD3ehi/pshDx3DD"
}
url = "https://xueqiu.com/today"
params = {
    "md5__1038": "n4IxgD070=G=D=YDsTiQLywDfrEFDRD3aoD"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)