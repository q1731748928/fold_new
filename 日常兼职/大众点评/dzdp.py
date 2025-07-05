# 我这边这次暂时需要1k条数据 ，但是品牌【老碗会】
# 上海地区所有门店底下的评论 可以帮我平均取一下子的
# 数据主要内容就是tips+用户名+评论内容+打分星级+日期 ，可以下周一前交付。你看可以吗？
import pymysql
import requests
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="part_time_job")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

headers = {
    "Host": "m.dianping.com",
    "openid": "6LhsR_sK1uagKLF0M2ZBPmh8hJSYd60LPW70JOhxS2s",
    "channel": "weixin",
    "channelversion": "3.8.10",
    "minaversion": "9.85.2",
    "wechatversion": "3.8.10",
    "sdkversion": "3.3.5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.10(0x13080a10) XWEB/1227",
    "dpid": "6LhsR_sK1uagKLF0M2ZBPmh8hJSYd60LPW70JOhxS2s",
    "Content-Type": "application/json",
    "openidPlt": "oPpUI0YAw882j2ilWslZ3CYBBLXI",
    "xweb_xhr": "1",
    "platformversion": "OS X 14.4.1",
    "platform": "Android",
    "minaname": "dianping-wxapp",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx734c1ad7b3562129/562/page-frame.html",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "https://m.dianping.com/ugc/review/reviewlist"
params = {
    "yodaReady": "wx",
    "csecplatform": "3",
    "csecversionname": "9.85.2",
    "csecversion": "1.4.0",
    "optimus_uuid": "19759f92796c8-208a6b79e9c8ec-0-0-19759f92796c8",
    "optimus_platform": "13",
    "optimus_partner": "203",
    "optimus_risk_level": "71",
    "optimus_code": "10",
    "tagType": "2",
    "tag": "好评",
    "offset": "150",
    "shopId": "644726394",
    "cx": "WX__ver1.2.0_CCCC_dfwOgF35EQNYzVh8i27kXL04k6XTiM6UIbLC34PDQwAlFFunePPYPkpJq4XJVRltidhrJWr7r1NZY58S2zwZNLhDW3M0QlkFrcE2pVHRnPzhLCmMZ07fFkSGcYn7seWOp2qiDmCMz9sGQ8X2SU+6DtX04SgxOScQwGgzyF72EcD7iYKL3hdlrSBQovqIvx2nwvqVuO/rOvynfpaaYS+kBDiJhEQxcAFH71v47kr9iplTmGwUkA/GxcYTSnOJfAr1m9TR3NiwDo3/qi/8UprQlxLXAdCuP636FAI4I42lBa+rJ5ZnGfO+2UiCPoB7m77mOlE/Pg1lB8MyXKlSPG02cuaFlXr957vJCI5cxjmtuuBDIj3tmNNEQFrMYcxArHccuhzS5DA2oMEZTXV4fbhsoYdVwgpNHnvreoWE8LZcPEQYxzfpR2l3D94d80UJMW+irDYAAhbt8mbAqS3PK44E9zJtbBzMHVrkVdicprLe/06KuIcdEGQFebfzec7wlYuhtC6TwTgJrHkI0A30CfRdaQdL1UhxcY+DBuG6ndfjNJTogvsGnQE1GMmM6AofrC4QAM76DXAsQJWGi3bABlu8vzc/5yExtcZcv5dOgx+7Y5GKiaaqoKQR9rjhhK16ZZTd2W7HLR2Ks8tX7/QpzCWOA1ph3b1K3jcmMWuUN5HTZcM2JBQeiUGvdsZx1gi427us1OzqzM1201gdIDv/yMb5Ef4xwnlup0cits6IUYqavtV8bD309ssWkNeMTd3OBWRYRb39YdCxYppWVGZG580+TxyenM74bi6gH1yqlJwtATI7qze7zBbRyurOotfV5R2d7fMuey7Aa3B3Kr5xDybp95wy0N1bz0Jd2H0sJ7ltkLSZIZaU98JTUgmkWoUdxgqiYz9jsvxr5GyCYGjK5rE3kwTE6uojtj+z0FjKcEK6BzBiEupFhjQpWIyqMq2dV98mlQyZrbZhtnHLz5r9JR0bkyA1DuJaKcamfHoO3USJvte3ole2d4lT3EAasCa1Z8Qj3JzJxAbtddJLCeMm1Hj8ewBdoseOARGRtB8GWhfCtItY/WyXm8PuLZlTjJFqK7wvAlok0+Kx5sixt0wI/scfJM+l4KentXrnKDZBMwW6gOuCzbVvMfAhRaKSFUJOO84OpfbuqTk736ONJ5Fsu27ElOdzqcfuoB0+uBnlqgV693MFo+GV4zeIpTlCsgyPhdgtIOjOvvUEydDeA9wlAMUKbeKAim3nq26wOoWGQYj9vigEZcx+VBzRjhRlgPrahkDctr1WLaSbiusoFsmoQGk6IwYOUvB6jJByHHYhoAuqB6PyTc/xOTeC70H/+0ELqeYbt3setplAFZb70ZksDPEwrUlZBza1xIQH6T2YWVPYs8W7TMhnyvXwbh5eKvho/uUU+nZ5a4wxLmNvd3zFeCcpwehTyVRX2SjJ44Ju64PFQmksl0OqBA+lQDhqaJTMKWrpBLJGAbDjqRCOHHriRdRq9I7OO0pVCwK2gD8JlK49hwN6GqdEgrwP+bWRN/LolH4plzofdSS8laJjViFlSC3tHIDVrqMUTf3/qZ03H2UlOhIqC7Scf/VLhHvOHiv4MOg9SaWGF4h+opW2ImaIcpGeQxN5tjEBAhnxuh3lQ7N9BoJqq9Eu41fC8fyyfSyDa5EGQvx+UbQOAxqUL+APu8dCrAXnXctXZ+EnOCFw9rsu8Myij8IjMiSw7phFVNLmC33nD1xAQB2wicJQI/qrsD2X1CGCaQ5oFYhjm/UQrh/88+1Rk7CvHdGLlKQGpKjs7SwNpyFnRAfWsL4JJu2dW/GjNnjbKbEy9+OZrfqlIEEhas4PwfjAH/ZdcmNdS7BLYyWsZa8SCBcuYiRQ3UWNWa1q6Q2jnHxq2FhJobolnyvfmi7xslXOGoPGLnEdXHqBEq3CX4zCigmp8k0olpPnuIDTir9yRz0/kyXKRcgAyto2Aho=",
    "mtsiReferrer": "%2Fpackages%2Fugc%2Fpages%2Freviewlist%2Freviewlist%3FshopId%3D644726394%26msource%3Dwxappmain%26tagType%3D1%26tag%3D%25E5%2585%25A8%25E9%2583%25A8",
    "_token": "eJx1Vseu7MYR%2FZe75TWY0wO0YB6mYQ5DQQtmcphzMPzvnmfJkhY20N11Kpyq7gZY7H9%2BzXL29QP6%2FlqXrx8widE4ASMoRqDU91f6p42EMAImEfj7K5l9%2FuvHrxiMfZMo8dtPg%2F3Rf6UQ6hvGSOS3779BBPuMnzHyJ%2BRrjNMmLvMF3MoUHP%2BD5nyv86Otl%2FVv8Ov763fvONQ%2F59cnQ%2Bf%2BzPDZwD%2Fgj%2Fsjof8l%2FvAhPxnNT8ZHxr8zceKbptHvnzX%2BCIJgEvpT%2F2yZJH%2FXPpz1r2r%2FzQn9f%2FBX3Q%2F4sJe67L9%2BfOXK6bdevpF6adtF4RwPymVaFIp2RqIVbNk61W4OmiBv9IEMsxQMUiBDvOaZ6FaVbiuzfM8MnX4LfApyEL6DKHrjNPlsDPAgAd6kexMY%2B66CG5nTo8TuOdCZVa7O47UMan6nYfW8IRxuS6EItcBKcm4xw4g6G6qDpQjSimtZN9hZ1ogKsroajuMQysc%2BgBYkzIaNulZcrZXbV1ghtAhInto7RyGBs68hfAiKUStKYT6FCJvmzoQ7eBRq9ObfZVGi5iB5cYq5Tn7ys4RpmMQAL%2Bs9Nbzf8MoaYflZ9YhDn%2Bb2RmEiyaP3c8%2Fnm0oHrrrKV1KpatjPrlSx8sRkSjRF05IEZOryMVA%2Fci5mCdDpmlW%2FYVHa3vbbPyxUfhFDPvKF4ffrlNxju165gTHyOtyyukKHcDNDQHfKxsxsuKQAK7sTR%2BhXUNyHNkm%2BDIbTPBe6Z7nvSJ5E%2Bj5tiWSG%2BUW1UQZsiB6dqYysvaQd7f2YrN60FiVtA7QkJajgSop4kMUk4iGH841GGK%2B30xQjcB95pmjele9skGY3GafyeojK5AxqMZgt%2FwwF3o2Sywm90%2BR3xfMip0%2B64Nn5Wxj25u1Ma9Nr4cLk2qTU6ajBIyduGdpW7ENC7vbatA2zE1Xjvcvh9LKj1zFSvRhXgiI6ZCyqzNNc4NlCpcerBQV0kysvp6GeJa%2FO89agzg6ygfZ2UzXR1lxX22wAh6hFXkD4svWsPuD61EumOb3pqmN2Da4paTbnDLmDZp%2BvCLCeH6OIKrRw0PMu9sWoSp%2FbU2Q7nxoIRJ%2F6zSv8J5VflfN0n6eLF0clD2r1atcyPcmt92R2Euo26ek0b85zK4a8cNfnoCirQ2Ak47urSu369rIacQj2W7hQD7Ib8LF%2BjmirzTvSz%2BoBXoEkNzFXPtY8iCk3Fu%2BqsuzMI5ZUBVD1fNj9qaMCPYdPfOY7jbok79LCFThqgqkq4RFK7kao9jGQ2soxWLV6XltyIuYPMBTd1rvTTXn0QhUcpB48oNl4TRvXEZ0HRtBFIQK3%2BMHdNXl05OGRELMnJS03wC87TPOoU3ssqRIVsVsAUHqEg85MzCYYrkI9bbtlj90U8bDheS6waNFXZ0uDkyUN1MnvXjW3WPaM5HD6eCsr0z6WxHLEEX5Vl3ql2Yx0UyxdXYazXkP37KgbTpdYK1KvfN0T0UJsFFuCYN4XTUqbHDxB%2FstXlRdRJIMlsHTqBER7sxaKLU5MDpa8TUECADhMtlbzAgvtOJ5gbITklkOEl00vslTjSBm2%2BHXSe%2FMsHa7DYo5LF0lAz3nccw9%2F7kyp8xJtwN7%2BYFTo5bGCCA592r0RUtFSF9VWsWqXO0HR3NhbfR2IrhpR33y7ajDzW9NLPKgfdr4OaoJMG8%2FjjJ3fEhqOGRTcdzNJFx5F1DuU63xbO89qO%2BI4mTh8UzyUlfEu5rEzqkxKSHBNGUWrDKCb8UbAqN6DMbW4ZcKzru%2FImGNI0F%2BCxL80GnBMJFh5fCBKj3w1qOzxIOjp4ir3oYYuMwjTJxcEU7jgJp%2BYDDhYNc2%2FYX58u7iYXM%2BqMTXN2X0SOY9zZr3A5728KFcPdo4tFiCdn9PA9wgH27bZlAl9lCv4pgPnHmv32UZoLFyeO5adoYGRhb3kd%2BtH4lTIR%2FoQVSCQgb7hF4SKeAkelEe2kpdoPuRslScf8CF%2BWJZmuGh86NHQvN9XLsmcxobdFlCL5bjjp921w0jGkUfG1SaOlgvEKtMuzAHMfGqH8lWPLSytVUwdZ0ZvWSBPn27LWrf6fAqUvai4c0UhXGyheAlFdg7mIexrcxM9f3w%2BWyrpEvkGc7K4isFgEgwNcqnEu5BEpNVvUHX1KZx9q%2BGhz45hR1xeQmT82ri3U9la0dz3sYh7zYbRpcuS7LxnchOjFGxKx%2BKuz18lG33XC1bPsUk%2F54z0OJt9SNwZFQ%2FYbxnYAF%2FZS0KhbLpF0Hsx0b333vU%2BC7vcCdNU47bCq663JaLidLG9AaGJm%2BPWFLF1kCqsAcwrrEpcD9Tbe5bZWn2xeQBpCbQNhS2xd%2B%2B88mFNbsLfYumBcwifEQsc2u%2FA4vkNxUg%2Bj1Jii7btSAreKR6Ub3D7GLN4uVUAsC%2FtnE3mG4BpEATyz2IgczAci4Ohy6IZ9DXgO6GuSUvNBtVdnzdRT7LXpXuZIthJREETLIMVD4xmZz4CBJ5Nyqw1zjuuujdPxrBhgTsrQQWtxxt1lSXFFRo2DP2cJW3aiffcPqpw03exmFxzbUzJME73YkE2mqkqs3bbJJn5epgmYF588ChhsoY1N03BTydbvR15BkUsqD54RLRYmABaqSBckAVA0PYOaAXIsO0C%2BNgvX%2F%2F6N5ciaPg%3D",
    "isNeedNewReview": "1",
    "pullDown": "false",
    "reLoad": "false",
    "hitTag": "好评",
    "device_system": "MAC",
    "wxmp_version": "9.85.2"
}
response = requests.get(url, headers=headers, params=params, verify=False)
def find_exist(comment):
    # 假设我们要检查的用户名

    # SQL 查询语句，检查 username 是否存在
    query = "SELECT COUNT(*) FROM dzdp WHERE  comment= %s"

    # 执行查询
    cursor.execute(query, (comment,))

    # 获取查询结果
    result = cursor.fetchone()

    # 如果查询结果大于0，说明该用户名已经存在
    return result[0]

reviewLists = response.json()['reviewInfo']['reviewListInfo']['reviewList']
shopName = "老碗会·陕西手工面(上海浦东长泰广场店)"
for reviewList in reviewLists:
    # tips 好中差评
    tip = str(params['tag'])
    # 用户名
    userNickName = reviewList['userNickName']
    # 评论内容
    children = reviewList['reviewBody']['children']
    comment = ""
    for children in children:
        children = children['children']
        for ch in children:
            if ch['type'] == 'text':
                text = ch['text']
                comment += text
    result = find_exist(comment)
    print("result:", result)
    if result > 0:
        print("当前评论已存在")
        continue
    # 打分星级
    accurateStar = reviewList['accurateStar']
    score = accurateStar / 10
    # 日期
    lastTimeStr = reviewList['lastTimeStr']
    try:
        sql = "INSERT INTO dzdp (shop_name, shop_id, tip, user_nick_name, comment, score, last_time_str) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (shopName, str(params['shopId']), str(tip), str(userNickName), str(comment), str(score), lastTimeStr)
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e.args)
