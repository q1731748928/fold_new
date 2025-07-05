import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://api.geetest.com/get.php"
params = {
    "gt": "c0084ad0567738668c18a81b2e9ca4cd",
    "challenge": "3741be5146ce46da67a0d7e4897898dc",
    "lang": "zh-cn",
    "pt": "0",
    "client_type": "web",
    "w": "kkA84PMbmC(3kwLH9cmSSSBg7mAoL3hKUuYBtccGeqfmvrU85hP6Ze66HKrFCUXaPC8puLO4WmYhaveqQwFTqEmqSr7UpS37YT)PC5B8PDH53FgkaRh7hlBq(fnXH(y(Pu8DoY2wPe7Xp4EOjdlD2qY4pUyceaWr21q3A5tvpHsVAfhrZc3cnZNfFgqJl5KmE(tCcSH8PI1ZchYKJAg5sHeNoqOM)XOi3xsch)EIQOUJgrgiQcZ((eIyrxtqQi)6oNKZHwchViF)oEIs71EoAGrTq69i)b2iqLBTrkae7qfeDU7Ynq4b7chE801i0D(62ItLxnXTeqQ2dx8(HLSNrh2pdXCnZsbBtkC5QuWmo8kK5)0qqUysN3260))BrWSGThHu60DZIdCrSJj)mBDgQlVBM)U0Le8XCBenSr4Slyqx4fjkjO7qiwdUpR29AYtAsdLgyG7SBP9VMkUIUj3pjNIkR9Wjud7)EQUrGQvh8WY4ktK5IIuZYGGoVoTLPFgMMTiQTZn1jgXVUQpjaAMSvQr0SDIkrs55ZkSFg6ldZVxuFWiK(bjvjvpY9jKjPoNEH1wodew(B3cwQ2dLaSDGliGOfjeKBFOtKbii8PydtreujfsV)0KhXRWinBQGwCXnfoBmwul9YbyzgEAP5lTFNHTf(aRuwbqIWnR7xWK35T89nOEtVaHVub7CLrDA7v8WqDzYpKyi3F9GY)lXEppLZhhsC91TCxfVkRRNK3LTPRbSF5uquDU3xoFuVZLi6YETM8gIloAS1Z0zuegTFIyTjG5eOW2zQlyS8B1IAYX5S7QYT5HpZ)awDzu4OV3ceDRJQslbMg0CQs4Bz4jI1qq3qmmTHN3UX7TWzHqrDXAz(7RsN24IZ)2coe6hrP7Z3mmFxtvtFAppB8uyzxrN7iNUBZv6I7cCdsaG4XtxPRZ(X4MMShcCmZzKcgX8po41x6Scs)sweA3)d38bsewb4fkhrpCdoaENnI9Lr2UpANlr2qqISezJD4P9yM0GAFWTv)LBPtgKTlS1YYfaO0auosGp61htxX3OACtDhmDS1uMtTZbTS0M()RYGC9Yc6L7YKH5bUcms)4rgxvs8eaDkfb2yHjv8BPvyIqkzytti3sA9MfEKdg9BIrByXI6HCs11v)av7Nq420LN05GGgMMAGeuk1A..32a5638fd5508e28c6246dfec8d8b57fd21a5bc7135a8ec5ff2df68b66a6e15ff6be826c21d867ee7ed918467786d1a6c5a1c70a77dc7dc01c0d385d0163b6f2e9319b49437f88457b4abb04aceccf72a3dbd8c8c375949a6addfaf4ef0ea5c7e978a5a7690afdfa0204e411bc348196c927329d8b19dec1c71d69de376cdda7",
    "callback": "geetest_1749264955134"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)