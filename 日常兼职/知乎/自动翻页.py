from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import By
import json
import time

import pymysql
from bs4 import BeautifulSoup
starttime = time.time()

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="zhihu")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 清空 bosszhipin 表
# cursor.execute("DELETE FROM bosszhipin")
# db.commit()

count = 0
from DrissionPage.common import Actions

from datetime import datetime

def parse_time(timestamp):
    # 给定的时间戳
    # 将时间戳转换为 datetime 对象
    dt_object = datetime.utcfromtimestamp(timestamp)
    # 打印结果，格式化为 '年-月-日 时:分:秒'
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

driver = ChromiumPage()
# co = ChromiumOptions().use_system_user_path()
# driver = ChromiumPage(co)
# co = ChromiumOptions().use_system_user_path()
# driver = ChromiumPage(co)
driver.get("https://www.zhihu.com/question/277135177")
# print(driver.html)
while True:
    # 滚动页面
    ac = Actions(driver)
    ac.scroll(delta_y=500)
    driver.wait(1)

    # # 等待数据
    # driver.listen.start("https://www.zhihu.com/api/v4/questions/277135177/feeds")
    # spu = driver.listen.wait(timeout=3)  # 设置超时时间为3秒，避免无限等待
    # if spu:
    #     sub = spu.response.body
    #     datas = sub['data']
    #     for data in datas:
    #         print(data)
    #         cursor_ = data['cursor']
    #         excerpt = data['target']['excerpt']
    #         content = data['target']['content']
    #         created_time = data['target']['created_time']
    #         author_id = data['target']['id']
    #         voteup_count = data['target']['voteup_count']
    #         # print(content, str(created_time), id, voteup_count)
    #         sql = "INSERT INTO zhihu_qa1_test (cursor_, excerpt, content, created_time, author_id, voteup_count) VALUES ( %s, %s, %s, %s, %s, %s)"
    #         val = (
    #             str(cursor_), str(excerpt), str(content), str(parse_time(created_time)), str(author_id),
    #             int(voteup_count))
    #         cursor.execute(sql, val)
    #         db.commit()
    # else:
    #     continue
    #     print("没有新数据，继续滑动...")
    # try:
    #     driver.listen.start("https://www.zhihu.com/api/v4/questions/277135177/feeds")
    #     ac = Actions(driver)
    #     ac.scroll(delta_y=500)
    #     driver.wait(3)
    #     spu = driver.listen.wait()
    #     sub = spu.response.body
    #     print(sub)
    #     # json_str = json.dumps(sub, ensure_ascii=False)
    #     # js = json.loads(sub)
    #     # print(json_str)
    #     # print(js)
    #     datas = sub['data']
    #     for data in datas:
    #         print(data)
    #         cursor_ = data['cursor']
    #         excerpt = data['target']['excerpt']
    #         content = data['target']['content']
    #         created_time = data['target']['created_time']
    #         author_id = data['target']['id']
    #         voteup_count = data['target']['voteup_count']
    #         # print(content, str(created_time), id, voteup_count)
    #
    #         sql = "INSERT INTO zhihu_qa1_test (cursor_, excerpt, content, created_time, author_id, voteup_count) VALUES ( %s, %s, %s, %s, %s, %s)"
    #         val = (
    #             str(cursor_), str(excerpt), str(content), str(parse_time(created_time)), str(author_id),
    #             int(voteup_count))
    #         cursor.execute(sql, val)
    #         db.commit()
    # except Exception as e:
    #     print(e.args)
    #
