import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.lefigaro.fr/international/dossier/tensions-entre-la-russie-et-l-ukraine-tout-comprendre-a-la-menace-d-une-invasion-russe",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
cookies = {
    "ak_bmsc": "1AB042374CE821A9BE6843281B7BEDE2~000000000000000000000000000000~YAAQj5TYF0h5hhCWAQAAHbybIhvp0+dNeAOzE2IuTdS3dEK/M2FsmpK1/j+TPO8ezDpeXJnvLubOaywo8rpOTy4d6OM+bK5yZ4hWhoGN7jhGE7UUQcKhL5C7jmspyLhcfq1ej+x9BhCH90FOIqBSIFITKctqdToHUVm4dEco3oX7S7SbiDf0c1412UuBjf9dKLklUQIdJAu3tlmEQEr5fKLUnshpzkf8e1G2lXJQGyN1is6aCuYOT8r/VXyC4fUONsJWZsM2POTCqpxQhgMtkldBCWJVDQmuzvtfeh2XVDhR27JUp/3lgs3G6BoHlOhMY55IE+GLimAumok/1105BEg+G135zTQ3M+1hsNLUuddFmd1/sqbyjOYZVDZoYAcAv14G98viiR8+7gY5",
    "fig_save_consent": "4CpzOUOcYWiYOlIlcbf7LpNE9yKPCB4Z",
    "uhz": "5SDp3gnhaZF",
    "Wysistat": "0.6157275606989545_1744337359767%C2%A71%C2%A71744337376259%C2%A71%C2%A71744337359%C2%A70.6157275606989545_1744337359767%C2%A71778465359767",
    "___nrbic": "%7B%22isNewUser%22%3Atrue%2C%22previousVisit%22%3A1744337376%2C%22lastBeat%22%3A1744337376%2C%22currentVisitStarted%22%3A1744337376%2C%22sessionId%22%3A%2227c102e4-5a8d-4943-8f76-02e0b501a884%22%2C%22sessionVars%22%3A%5B%5D%2C%22visitedInThisSession%22%3Atrue%2C%22pagesViewed%22%3A1%2C%22landingPage%22%3A%22https%3A//www.lefigaro.fr/international/dossier/tensions-entre-la-russie-et-l-ukraine-tout-comprendre-a-la-menace-d-une-invasion-russe%22%2C%22referrer%22%3A%22https%3A//www.google.com/%22%2C%22lpti%22%3Anull%7D",
    "___nrbi": "%7B%22firstVisit%22%3A1744337376%2C%22userId%22%3A%2285f3bca8-664e-46a8-8299-1f75fb6515b3%22%2C%22userVars%22%3A%5B%5D%2C%22futurePreviousVisit%22%3A1744337376%2C%22timesVisited%22%3A1%2C%22userType%22%3A%220%22%7D",
    "compass_uid": "85f3bca8-664e-46a8-8299-1f75fb6515b3",
    "_gcl_au": "1.1.952720040.1744337378",
    "_ga": "GA1.1.ccd.5SDp3gnhaZF",
    "fig_session_started": "true",
    "fig_sessions_cpt": "1",
    "_scid": "_znxW5gLiW_V2hHEH_cApxhOvdnH1fPl",
    "_scid_r": "CLnxW5gLiW_V2hHEH_cApxhOvdnH1fPl2u8d5g",
    "_fbp": "fb.1.1744337381267.514305694120915522",
    "fig_firstparty": "oeR4uiefl9FmNaFJSuLEGAVrTl4WUBGU",
    "_ScCbts": "%5B%5D",
    "_MFB_": "fHwyfHx8W118fHx8",
    "m_ses": "20250411100942",
    "m_cnt": "0",
    "_lr_retry_request": "true",
    "_lr_env_src_ats": "false",
    "_uetsid": "080e1cc0167a11f0b7a1dfea34e16d52",
    "_uetvid": "080e0c30167a11f0a0f4d1338c2215e2",
    "_pin_unauth": "dWlkPU1qSmxZVFUwT0RVdE5tVXpNeTAwTnpKa0xXRTVaalV0TVdNeVlXVTNaall4WlRjMw",
    "_tt_enable_cookie": "1",
    "_ttp": "01JRH9RBWCGW86SZY1A4Z87J4A_.tt.1",
    "ttcsid": "1744337383311.1.1744337383311",
    "ttcsid_CQ3AK03C77UAOAV5CBB0": "1744337383310.1.1744337383532",
    "_ga_NLLLBBNGFK": "GS1.1.1744337377.1.0.1744337384.54.0.0",
    "_sctr": "1%7C1744300800000",
    "__gads": "ID=4a0927f81c9fd1b6:T=1744337389:RT=1744337389:S=ALNI_MY2bAk3mXQv8x7eOJxuIjMGZ4f_vA",
    "__eoi": "ID=da3d4fc648736963:T=1744337389:RT=1744337389:S=AA-AfjYISxUewiGmgY-V3FWKuY7d",
    "_lr_sampling_rate": "100",
    "cto_bundle": "PusZ6F9Ya2pVWGY3V0VSOXI1eWs2REZRTUM1JTJCMUp3UXI2WnB6cEROOE81Z0hsZk5Wd01Oenk2aGhrMXhmVVRjc3I2QjglMkJJQ0laaWU1UHZ5TU5YbWZIdHV6anQ2alQ2YmUlMkIlMkI3ajE4eXkwV0lIakIwWjFycngyTnlORUdFVTZzczJSVXk0eXdpUjkyYkE2U2FheXFZdktObGNmQSUzRCUzRA",
    "_dd_s": "rum=0&expire=1744338320366"
}
url = "https://www.lefigaro.fr/international/dossier/tensions-entre-la-russie-et-l-ukraine-tout-comprendre-a-la-menace-d-une-invasion-russe"
params = {
    "page": "2"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)