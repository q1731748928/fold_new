import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.7(0x13080712) UnifiedPCMacWechat(0xf264035d) XWEB/13634",
    "Accept": "*/*",
    "Host": "m.dianping.com",
    "mtgsig": "{\"a1\":\"1.2\",\"a2\":1745679357930,\"a3\":\"27vy60v30xu9528u0yw9zv1063u7y0wu8032936023x9797853y79xw6\",\"a4\":\"66388ead42d502dbad8e3866db02d5424799a1149c9b7456\",\"a5\":\"EtsLWK0sgxzUfzKxQ9kwBuQfKz2MkSz/EdvlUR2ke2F/8dOl01oFbz9Nzz2zaFFOnVdLkuGqwGXKRa2gPOurlHdUnFt7yOtH9aL/EFECA0/AmC+eEZANhBA0JWpYnzDhm6o7l/7rcg38Dyx+LXQkqL0h9kKtCBWX+zxSfE7OfaRGepPER3ps4P27Eq8NJ+RDRCYN3RJezD3D5ZuzHRM+RNIEMHi4FLbohbVXKpP9CMMrnetSRLU2LnsPeYgvCspRlM/qioNIxcvtRkhhZlbMZ/IGXJ9kwTIDNptdLeObtkqAKa5LOTwAAoPyBtJr\",\"a6\":\"w1.3eCHzQ3iXiwOIeCYpLVxRZD4BCoBhxvDl/nxW81gddSIRVn122anFRpN6eKoxvYouzJ+oVxewga/qJfgvfe3DlmIu37Ld5W8vPlempwtA1GMpdkNEk6s+LJPBCxlYWnstH0SCBmCboe60nxIOalmJ/OeJg8vG+b/s4s75GuZgeJ1doHRjCwc+JA7Qw4m60uFeMNtOX+S08DvpDIN0ZqtY4qondNE7ikbpoh5jq4KkEdmymWhfJG6JKnjudDixCt5rVfM2FcKPAsHXSgABMjQYYQU/UlUTbt2z0ITSqaXJ8Uf18oSeqDupGzaaP/0zS/ESh0tdzY4OdGLxWS73zgc73zDKpG/84jx77mwTjBPLx54fmnxyVxa+MQIYH1AvdmqZuaZZElxaiXLjCkBBIQ/AHWrRFBwwo20TMEbEBPkrTlSvpinsq0+7LnKrQ5IbWiRxpPI+QePfhIamu6Gqwg8WUnS2MNZuRhLRbBSnBEVdFV2JJcGRmVCcvcvaRP8EESCJ\",\"a7\":\"wx734c1ad7b3562129\",\"x0\":3,\"d1\":\"bb0688f40a6333907c4d65a4506ddd1b\"}",
    "openid": "-Pxv_17wIDSPX_CnK6Qqf6KAXmjCLpjfLPt5pCrlcfg",
    "channel": "weixin",
    "channelversion": "4.0.3.93",
    "minaversion": "9.82.2",
    "wechatversion": "4.0.3.93",
    "sdkversion": "3.8.1",
    "dpid": "-Pxv_17wIDSPX_CnK6Qqf6KAXmjCLpjfLPt5pCrlcfg",
    "Content-Type": "application/json",
    "openidPlt": "oPpUI0eO6yJlQZCdS_i6fxgj2rD0",
    "xweb_xhr": "1",
    "platformversion": "arm64",
    "platform": "Android",
    "token": "0202a820a7a5f54ea855c699cde70b7cbf58e0a7bca19d04109c4a768a62d242056c908d6c870bc75d17afa27c06ab5ea8cd76347ccb50b7ed5700000000902800001c5752e238b259f153b912623cab21ef2a109733671c05360281ef2f8bf9f927dcfac41d5e617f8bb6b3290ea2ca88af",
    "minaname": "dianping-wxapp",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx734c1ad7b3562129/554/page-frame.html",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "https://m.dianping.com/ugc/review/reviewlist"
params = {
    "yodaReady": "wx",
    "csecappid": "wx734c1ad7b3562129",
    "csecplatform": "3",
    "csecversionname": "9.82.2",
    "csecversion": "1.4.0",
    "optimus_uuid": "19670639418c8-2307f6febfaaec-0-0-19670639418c8",
    "optimus_platform": "13",
    "optimus_partner": "203",
    "optimus_risk_level": "71",
    "optimus_code": "10",
    "tagType": "2",
    "tag": "好评",
    "offset": "0",
    "shopId": "1130214190",
    "cx": "WX__ver1.2.0_CCCC_dfwOgF35EQNYzVh8i27kXL04k6XTiM6UIbLC34PDQwAlFFunePPYPkpJq4XJVRltidhrJWr7r1NZY58S2zwZNLhDW3M0QlkFrcE2pVHRnPzhLCmMZ07fFkSGcYn7seWOp2qiDmCMz9sGQ8X2SU+6DtX04SgxOScQwGgzyF72EcD7iYKL3hdlrSBQovqIvx2nwvqVuO/rOvynfpaaYS+kBDiJhEQxcAFH71v47kr9iplTmGwUkA/GxcYTSnOJfAr1m9TR3NiwDo3/qi/8UprQlxLXAdCuP636FAI4I42lBa+rJ5ZnGfO+2UiCPoB7m77mOlE/Pg1lB8MyXKlSPG02cuaFlXr957vJCI5cxjmtuuBDIj3tmNNEQFrMYcxArHccuhzS5DA2oMEZTXV4fbhsoYdVwgpNHnvreoWE8LZcPEQYxzfpR2l3D94d80UJMW+irDYAAhbt8mbAqS3PK44E9zJtbBzMHVrkVdicprLe/06KuIcdEGQFebfzec7wlYuhtC6TwTgJrHkI0A30CfRdaVmUrdmMV4yS7GcBUhLT5K0PV1gTm5Ki783CsTa/UOyEWLdOGV15bG8kAAuQpqoMZPFexFgkFlQ/ptY8Pc6A47NbV511bAMi/kJmvBQ6Gsjy0jQxiBglvECRpjerM+bZtFXMvG+cHg1YkhemXrAp2+Dz7f+QA8uYRHiQLw47qQVF+Ujsqw9VmMJ7IoSWW+AuoR5gOWD8n9SnZKxRLNTlo91GEWT8SiSed1FLaRqVPDM0D1PNG0VzsiiBszpMiqX54C/+nWVH8W3Z35YuR3bD6/oFsvovyTz5sf3NfcUslpQZp9kSObaCN1Za0GbthY8dr0sH4rcYP3aS1tdBcyvO4TwpXaEmdGsVjpHorxnQ0IVU+qzX6vyn67+xyhdE5O7+Ua4EYUeMI5sbxaoUzy/K/VhHGhEv4PM/4FbNjj+dhfcnIk1hRd69kv/2fE+1cJ7W8Ix6B9KZEBX+IigozAGE0g+HSro12ZWl/bscSvI60JQYoAIBFPKwXAzJD/46dcfN21uND+ZPfApq34P3L04s2K/DYPOFxNXK57eu91DzLCPU1bQ0sAtm5b19qMoPGLKdnomtnMhFVv9P4QYrA8mDDBY4jRNDiorVlIwqQWFPtayTsMZJYB93ThAO+0XsvIjjoLOm0xlTVR74qdZRBxEpGk9/C9wXAiDuXb1swv91kte+u7F6x+d5VM0mDroViOoQUv7XrpHHiEdnRlmOBxxpAyx8KhGKsNrHKjDfaNibYWC+MCjPPMNvVciyFEmKmmdtbC2zhbcR1tJoS8oceZrVnjAdYf7OJFJrZ8dvVsAcUoegtDZXuJxxFxuO5St7A0Ca2nAQIdccet5H24tVqklnejNMMYh0K7iW653jEafirCZ4FZxoFEir2d5FreLZ4Lyw8AN9hM5mf4MqTYZxIwNGWS1VrN6TdBSqPm7JB4xfekD3XnLf5KSPK8t4pWmpuGay5hMYYznohv+ZBCa3tti1zj6cXRxWVrWyFzx0N1cGhZf4Vt9oFnQ8eYi0xH65dTzzkIRHihXydwEb7ArM4Sz1yZRGZjZW9quFhkrx49YWpZCesiBfCZrrA8tiJCtQjAKND0utv5IG2gTrwJ5xq118A/olA4/TFPQFBwmuGMzWCaQg1VlWNxoFn5pkigtL4LDp3sLFVxlznr9juyqJyztmhiy53fuJL8PdkXlNKcZSbzwtjO/LRKQZ7uriMsc1MTCb/U8lfE0IKKe/UcTdk0ToCJkGk+IYPnLFOo0poP18jIyXz1cWB10qN2SrjuUBAWWuadX8bHlswn+hNN2UJxl1AAq3ILNqecAo9hZgdfeH5GPtu/HZSjQuhIlzPqXWa+mTydre+tUanHX3+E8kIGtDEtzfBAIHeTzcYb6F2XzIP8MubiH8lESV1AyGSKWhFwlwOg==",
    "mtsiReferrer": "%2Fpackages%2Fugc%2Fpages%2Freviewlist%2Freviewlist%3FshopId%3D1130214190%26msource%3Dwxappmain%26tagType%3D1%26tag%3D%25E5%2585%25A8%25E9%2583%25A8",
    "_token": "eJx9lNeSo1gSht%2BlbqkQ3vUdwjthBAiY2AucEB4Bwmhi332pUnVPz27NRkih5P%2FynJN58kd%2Fvg1y%2BvYDen%2BbxrcfMInhBLF%2FSJxC39%2BSXxpJozhJYdj7Wzx43NuPPzAYeycp6F8fgr0%2F%2F0Eh1DuME7vyW4hg%2B%2BcjR95T3vooqaI8G8FHnoD9ZzRkc5EtdTFOv4Vv728v2nfFx%2Fdt36FxPnZACPxAIDBEoyT%2BjpD4gSRRbI%2F3FQiBHb5EjPqloQcYeYkQSe3hpwgfPiTsQJAw9crDiQOJIR9PO0AP5H4O8UrG6ANJEy%2BAHDDir70x5ABR%2BFcl8AF%2BpX0QFD%2FAGER8HEzQB%2Fo3giAHCofxFyIPP4%2BHf1tAHHDsZzr0m479pcMkecBf%2Fbx%2FdPN5HR86tusUAqGfYO%2BJRn6eDKP7euR1WTvCDhQJ%2F1qGwAfsq%2BWd7SW%2BLgqG%2F6ZDP3Wa3gtHvzrHqAP587Lo38%2FYayGgz1Y%2Fxld9jG%2F%2Fjf53jARKku8fo%2F8sBfva7p2E9%2Fv9CL4QgqAH%2FFfX1D6lVwWfeN95%2Br8GeYe%2Fs8iX%2Bt8m%2BZL%2FbpOX%2BL1RXux7q3yxb83yYt%2Fb5cW%2BMcwLfGeZF%2FnONJ%2FkW9u8yD8Y5wX%2FyTov%2Bp15XuQ7%2B3yS7w30Qt9baGf7iMcib99%2BvGXK6tVu9iC13LvN1%2FOijQ4TwUmVh2gnbKoSeu6516XVkw3vFGEToK4ewNWiyWy%2BCsaWrieS8pyPSwkoOnW7Qg8zfoIY4Jsac%2B1Iupy3CgT0Fm5Wk8bOTndHRA%2FPzl4SwJZFWOUZXVRER6BJSY9Yq%2BlShnjRGS4JdDgd73brFszkkVP12OvkYMbyLH3pFWQUH6ajwe58XBlSiu1c7QsZzcC0jj2ifbY2f%2FNYHi77TTQdvwUbk%2B%2BrocuMUxFOTcNQK2456Y21OTazKVMhPRTwkZTvLsrdPXpdFJdhGrA30pBiT0UYYEbjq3Y5LkuG0JUfrJvETfZi3S%2BXrkWqQTq3kIzk4nh0A2BCqBm%2FX4QcgKYjDHRpNDLcJJqZ0tDug%2BNyynM4WuykVGoHJpzXO3pl45W981bDTAJ0YpTolGk3zKLvPRYBbFfeVcLeZha%2BTZORdhhDwLB2bI9QebkgObMo2qWfebWxaWgiqE45d9DcXhp1ys%2B6zsFBwoPOFC%2BJ27DrYjPlCWRluWhbOdko0EEiGsU4IGO16UjUdVNIK3zRHeIpHINYjoxzLZa4y5yFCnGUkGDxm7Jk6EmWrcadUv6BbeQN72Z1VW2Ca3VJc7zCP9mn5kLdzxjVOxGC7n2BZEM%2B8Ph4TUXLyxMsmFqhnVMWOaeYLbYWVfX01sM1bVkbZF7jKr0Lrl%2BCxlOkjGktBiIzL5ap2EYY1zdkStJeZxVty8EedYuJC2jtLMx9eXY7HRRkgYeDDpPjKR0xYItNOmhduhZWEg0cIEsDnGKZqilspjGc7uoA9mg0T21kRlYXWTv1LC7UBkB6%2BlNLODXrkG5r3XGiba88YREXd7kKdCEgkgLWAMBoqQ5h1yhJnRMNI4FwDGkBje7hQlmbS18rIlPsQs6Fe1NKpe8LfnKVYfFkudWSnCwSnVBkTMqWefoKjskntLDwZi90Tgp8kdECtOCJ0NPSfZamogYnmu%2Fsh12prk4w1I1SICa6tOXY8bPYZ1dEPq00J6rrBjjhnbqSjExm9s2Zjy7sJ%2Bbskh3CloOp26ZytCIg4PWTHxdl1R6fK6X1xkU2aKogfKwKg2O1yoXX%2Bq4QXKKIgiKz1eNqey5efrOa4u6WxCRxmQGdVZvd2DrLKV%2FFZlkkOzLg2XUTwVvIE6kTV7f7DTIGXVHqIZBI1VV1SdKgUeOhk7sPLb8jkkTQHAlke%2FeObAiQ1Mu3te4U5TJzbJ8YDUBDui2GbdxvjF0rjbGEAqoBdyHO7oY7y8jKciOvnSCFuSVnOtXdey5gQ6yYU0GHZ3QjxlXs5eSax2MFyOw5OBGXxxFEbdm9DlkFqI2mdZuNFiqX6E9Ovzb4ZTnmFUGuD%2B5UjcYQ2pBBsDrNbBVPcbkXgMdrA7uMHpOzrT7BqUY4AMPsOaAiFdnfkIpPCehSTMVYTVwrB8asJeNy2oDJqdpxUkmt7hxpKBWlBYqCyzG6lyp%2B1vBmJNlcut%2BrvCuNU0M3EJ1Z85rc2DqGDdUuryFnWAMvS4hOR9sUNo9Ay5JMXsNHNI30AD05lp%2FEbhsAO2NR0bZ8rFDYIsA5nm2YUA2EpFxKGhXbS8jfOZIZ2Oa0LEbvpLUESXRwxJOnaTTRZrhlW6imIi7y%2Ft8ElafRsQnZjUARTnBzbM%2BsbgwS1Z2KMgfWPqutO0jUeWwuYMZcocHPw1un9uleQq7pUEE7WXq72U9UxBscpt2uXbAhf5rxGthF7vKYgPai82zuMg6E3r0eF55fOocWrxzu%2B7ogYZIpnQl%2FK2Dk2RRVTpCqXXQb7cfsgHPiTdVR1qLG88hO4TQ6E3ru4poCJfo2w5cJpCReMMsKhf3WZgUopODCnyOVynTTI5xHj2seHLZnOxvU%2FX2AK2dSo4td4RvpznRuXtqwurps0ZdOLXG4bWJ2nAkFW0T1aMywDkXrEcamkI%2FPTDP5fZIxz93Q1eBvtzqJjP6pcmrYMOadTi7rPIDixWVaGo2zjMghJ9tqqUDV8WY8CCNye%2BDJ1CeeVEGZVL1ZYyeq7MnYd5tqjpaBEo0h0Rcdn7RnAd7IvOJztBgWGWtlT1LnJAFTdQGsJkjE%2BqKdV2W6pHHlSxZdO2l5BmszRqhNAK8o4MGZJpIADYLA6QqCbSvBoBcbIR4%2BYlKngfvVpMWZ7Ouhx%2FHKMqwcoK4N54iRbYAU2DjDA4QcgJ%2BZFjQidcIBH2T6uErswidza%2ByKQg%2FOd0ancoNMr8aSlw64maNdIrrvgbDkZyqaYQTomdYMNBaoC3JlYhIgeCUhPFWQNylnxqKiMc1aBKsIJgPvNqCg9lCQ50ABoUPyyDVh4fk5aMt8va4zdpnJjDbBC6iHALBRGghs97d%2F%2Fwd9pvkd",
    "isNeedNewReview": "1",
    "pullDown": "false",
    "reLoad": "true",
    "hitTag": "好评",
    "device_system": "14.4.1",
    "wxmp_version": "9.82.2"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)