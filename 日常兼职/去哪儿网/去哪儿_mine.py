import time

import pandas as pd
import requests
import bs4

# 要求包含以下数据项:攻略标题、用户名、途径路线、行程、出发日期、行程天数、人物标签、玩法标签、人均费用、照片数量、文字内容(一段即可)、图片内容(-张即可)

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "QN1": "0000f58034fc6eeb2028c102",
    "qunar-assist": "{%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}",
    "QN205": "organic",
    "QN277": "organic",
    "csrfToken": "ycmCGEtCc8G3ore9LP6kef76ky11Pjbn",
    "QN269": "C0880F90322011F0A4BFF616F22825C0",
    "_i": "ueHd8LkXXXVXpinydHURR4XgH7yX",
    "_vi": "e4pGovwBe2b4RsoX71GBU5mxZ69Yr2VIS7ffnCWL517HsdbsMipEkkXaKWiOwzSg9JTiyQ154EIrNOnKbrHd6J2TPxVUEGNS-mPIiIV24g--v5j3B1t1VNa6YrW3HxTOS8ScICgo5HF_hw-KJ6OXjxkNzLiPCU6hnxQl9iLCdfM4",
    "QN48": "tc_71ca9604ef4b3fc4_196d7d34760_3e01",
    "Hm_lvt_c56a2b5278263aa647778d304009eafc": "1747377670",
    "HMACCOUNT": "11F3EEC15F332D20",
    "fid": "beddf55e-231e-407b-91d2-ba8ea14ab3db",
    "JSESSIONID": "5D04055CB079D87AD49F89D161B628A5",
    "QN267": "9417864053057562d",
    "ariaDefaultTheme": "undefined",
    "Hm_lpvt_c56a2b5278263aa647778d304009eafc": "1747377680",
    "QN271": "840328d2-c588-4310-95e3-754c6142da71"
}

data_list = []
for i in  range(1, 15):
    url = f"https://travel.qunar.com/travelbook/list.htm?page={i}&order=hot_heat"
    response = requests.get(url, headers=headers, cookies=cookies)
    print(f'第{i}页的数据')
    time.sleep(3)
    # 要求包含以下数据项:攻略标题、用户名、途径路线、行程、出发日期、行程天数、人物标签、玩法标签、人均费用、照片数量、文字内容(一段即可)、图片内容(-张即可)
    # 观看数、点赞数、收藏数、分享数、评论数量、评论内容。
    bs = bs4.BeautifulSoup(response.text, 'lxml')
    b_strategy_lists = bs.select('ul.b_strategy_list')
    for b_strategy_list in b_strategy_lists:
        lists = b_strategy_list.select('li.list_item')
        for list in lists:
           # 攻略标题
           # 用户名
           usernames = list.select('p.user_info>span.intro>span.user_name>a')
           username = '暂无数据'
           route = '暂无数据'
           itinerary = '暂无数据'
           day = '暂无数据'
           cost = '暂无数据'
           trip_tag = '暂无数据'
           photo_count = '暂无数据'
           view = 0
           like = 0
           share = 0
           comment = 0
           favourite = 0
           for username in usernames:
               username = username.get_text()
           places = list.select('p.places')
           # 途径路线
           # 行程
           if len(places) > 1:
               route = places[0].get_text()
               itinerary = places[1].get_text()
           # print(route, itinerary)
           # 出发日期
           departure_dates = list.select('p.user_info>span.intro>span.date')
           for departure_date in departure_dates:
               departure_date = departure_date.get_text()
               # print(departure_date)
           # 行程天数
           days = list.select('p.user_info>span.intro>span.days')
           for day in days:
               day = day.get_text()
           # 人物标签
           # tags = list.select("h2.tit")
           # for tag in tags:
           #      print(tag)
           # 玩法标签
           # 选择所有符合 'p.user_info > span.intro' 的标签
           intro_tags = list.select('p.user_info>span.intro')
           # 遍历所有匹配的标签，检查该标签内部是否包含 <span class="trip">
           for user_info in intro_tags:
               # 查找该 <span class="intro"> 标签内部是否有 <span class="trip">
               trip_tag = user_info.find('span', class_='trip')
               if trip_tag:
                   trip_tag = trip_tag.get_text()
               # 人均费用
               cost = user_info.find('span', class_='fee')
               if cost:
                   cost = cost.get_text()
               # 照片数量
               photo_count = user_info.find('span', class_='photo_nums')
               if photo_count:
                   photo_count = photo_count.get_text()
           pic_lists = list.select('li.pic:first-of-type> a:nth-child(2) > img')
           for pic_list in pic_lists:
               src = pic_list.get('src')
           # for pic_list in pic_lists:
           #     pic_list = pic_list.select('img').get('src')
           #     print(pic_list)
           # print(trip_tag, cost, photo_count)
           # 选择所有符合 'p.user_info > span.intro' 的标签
           hrefs = list.select('h2.tit>a')
           # 观看数、点赞数、收藏数、分享数、评论数量、评论内容。
           nums = list.select('p.user_info>span.nums')
           for num in nums:
                views = num.select('span.icon_view>span')
                likes = num.select('span.icon_love>span')
                for view in views:
                    view = view.get_text()
                for like in likes:
                    like = like.get_text()
           # print(view, like)
           for href in hrefs:
               title = href.get_text()
               url = href.get('href')
               index = str(url).split("/")[-1]
               # 详情页
               detail = 'https://travel.qunar.com/travelbook/note/' + index
               response = requests.get(detail, headers=headers, cookies=cookies)
               bs = bs4.BeautifulSoup(response.text, 'lxml')
               # 文字内容(一段即可)
               texts = bs.select('p.first')
               li_lists = bs.select('ul.clrfix')
               for li_list in li_lists:
                   # 分享数
                   shares = li_list.select('li.nav_item.share>div.sharCT>span.num')
                   comments = li_list.select('li.nav_item.comment>div.commentCT>span.num')
                   favourites = li_list.select('li.nav_item.view_collected>div.collectCT>span.num')
                   for comment in comments:
                       comment = comment.get_text()
                   for favourite in favourites:
                       favourite = favourite.get_text()
                   for share in shares:
                       share = share.get_text()
               for text in texts:
                   text = text.get_text().strip()
           # print(title, username, route, itinerary, departure_date, day, trip_tag, cost, photo_count, view, like, share, comment, text, src)
           data = {
            'title': str(title),
            'username': str(username),
            'route': str(route),
            'itinerary': str(itinerary),
            'departure_date': str(departure_date),
            'days': str(day),
            'tags': str(trip_tag),
            'cost': str(cost),
            'photo_count': str(photo_count),
            'text_content': str(text),
            'image_content': str(src),
            'views': str(view),
            'likes': str(like),
            'favorites': str(favourite),
            'comments': str(comment),
            'shares': str(share),
            'url': str(detail),
            'trip_days': str(day),
    }
           print(data)
           data_list.append(data)
# 创建 DataFrame
# df = pd.DataFrame(data_list)
# # 将 DataFrame 写入 CSV 文件，定义表头为 'likes' 和 'comments'
# df.to_csv('output.csv', index=False, header=True)
# print("CSV 文件已保存！")

