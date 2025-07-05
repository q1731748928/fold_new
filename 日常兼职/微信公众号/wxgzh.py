import requests


headers = {
    "Host": "mp.weixin.qq.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8.8(0x13080811) XWEB/1216 Flue",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "document",
    "referer": "https://mp.weixin.qq.com/s?search_click_id=4265800889456148-1746528992277-9421596614&__biz=MzIyMTQwNjE3OQ==&mid=2247543615&idx=2&sn=986090219eff03fe88ad28a53c0d4eed&chksm=e92749f1047c9ee168576bbb2a6c07585f02cadd1d654c8f96c764a53a277a35e229b3bb9537&scene=7&key=daf9bdc5abc4e8d05ee1a4b9d7e6467ee1e8eb7c48c4a9915024b8f684286abdb2f739b75af00017ad2b253bc4981b9ab840a521d81e8f2a68d18a6343fc4d1be1aa256027d75ed58482f90b8fa6f62700cdf085c3d885a90bca4e3f36d740d0bec6a3d8e6cb710a661f1c89e60ed0fb11b19cd8d94c6f91793a6f0b41fa9331&ascene=65&uin=MTE0NTMwODAzMQ%3D%3D&devicetype=iMac+Mac14%2C10+OSX+OSX+14.4.1+build(23E224)&version=13080811&nettype=WIFI&lang=zh_CN&countrycode=CN&fontScale=100&exportkey=n_ChQIAhIQzZ5XC1esrfDf9L4g0fQH8BKDAgIE97dBBAEAAAAAAFydL8A5J7IAAAAOpnltbLcz9gKNyK89dVj0h6fexbTDUE4JjJDZoYGRu3acwmL0kIGSB4E0oALpRFlx4Oh6z8RJfbXMiHkItT5u%2Ba%2FrR%2BWhZQxaDnKwrmBYg8ThQ4QRNMeOSjQ%2FQ%2F7NQdS7Rv5WusvVtzW5h%2FU%2FJDFSxUksGavDFpMIS8GyOMuCJLLcYrMsWrbiYMfHmPgSk5neb0fT%2F0mdFQXUkYbjG7HqkUyNSPZwzqPk9kQN9nnlWfF%2FtUulAWvnDykd7N29K804qu7SGFzP6S2l6CZbU8HhGEbowvIjW6lqAi5f3B57Nxbr02BphPawkd5PR7E%3D&acctmode=0&pass_ticket=6AA7v8cseKMn7kE%2F%2B0LvWWrW5EI4WpuZQeLqzz274a6C0162XRS7kNdOFDXcc2xz&wx_header=0",
    "accept-language": "zh-CN,zh;q=0.9"
}
cookies = {
    "rewardsn": "",
    "wxtokenkey": "777",
    "wxuin": "1145308031",
    "devicetype": "iMacMac1410OSXOSX14.4.1build(23E224)",
    "version": "13080811",
    "lang": "zh_CN",
    "appmsg_token": "1320_LykxrX9HTweJ6ayXSnIf4UrQ3IvQpJwK4Cr3ynnQo3-JO-oJVhj08i8lxrYNChM2yrn2j5cT3DFQvv31",
    "pass_ticket": "6AA7v8cseKMn7kE/+0LvWWrW5EI4WpuZQeLqzz274a6C0162XRS7kNdOFDXcc2xz",
    "wap_sid2": "CP+GkKIEEooBeV9IRmxBSWxHOElvRXY4NWVNaXNrYkVFM0NfcVRISktMbWoyTmdJNTM1WlhiNUxjMlVjTHQ0ZUF3TjV5SFBtTnhabHMyOVFnX2hVZkNXUzRxbW9QaHFkNnpRajlkY2ttS2VaQVZhYW9rTWlGajdMSHN4T0wwYlhiclN6OTNUX21qM1BnWVRBQUF+MOHV58AGOA1AAQ=="
}
url = "https://mp.weixin.qq.com/s"
params = {
    "search_click_id": "4265800889456148-1746528992277-9421596614",
    "__biz": "MzIyMTQwNjE3OQ==",
    "mid": "2247543615",
    "idx": "2",
    "sn": "986090219eff03fe88ad28a53c0d4eed",
    "chksm": "e92749f1047c9ee168576bbb2a6c07585f02cadd1d654c8f96c764a53a277a35e229b3bb9537",
    "scene": "7",
    "key": "daf9bdc5abc4e8d027f696e9f2341bc3d3aca163437d745c73e1510f8dc51b4b2d311fd533c31ed38dc69d5c47c222f999c9ff9f02e5faf6d6744d9e66fdd59bbab48cb4b469e0ed9c6d570d698cd2aa8d778be6156166e22969733af0fc7f3a322b62b5dedae063c05b2ed7897f776efbc5a6dc985e4461b0942ce407891621",
    "ascene": "65",
    "uin": "MTE0NTMwODAzMQ==",
    "devicetype": "iMac Mac14,10 OSX OSX 14.4.1 build(23E224)",
    "version": "13080811",
    "nettype": "WIFI",
    "lang": "zh_CN",
    "countrycode": "CN",
    "fontScale": "100",
    "exportkey": "n_ChQIAhIQL8cf0pYScHDT5j7PNxAsYBKDAgIE97dBBAEAAAAAAEpeEpnsj3oAAAAOpnltbLcz9gKNyK89dVj0xXSaga9ZlmUzNUUZVbL900uQFOdOjh5C8vnmcnloolmDA23wxQFIVsgzymALpOzAR6h3/8oV+9rIhITTmEey0nvh5tqfqKybmTGL75eOE66VD3A0vaPqnt5h2nW4ll/+xq/QZDI+KbM7ylcgXotZsEWsdGfNHlCtjs9+RU+C5SbBge7Gxx6Hj8wORvcW8IomOvyAk3qyscmIiwwEnr+5MdL6zGuzaMk8mwSD/PeU+TmdY+w3JXn70BLvsdJ1/LYSd/d3c1c0REaw51EqBphb7kyvzA5WlzCjI+9ioog=",
    "acctmode": "0",
    "pass_ticket": "PV5qBoWqpkjrcD+wMV1cJBkaC6/6HlkoapjjXiGA1NNxSqGKWzQe1VsoHqF2uR6+",
    "wx_header": "0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)