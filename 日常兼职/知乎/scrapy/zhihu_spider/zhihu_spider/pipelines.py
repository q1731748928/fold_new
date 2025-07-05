# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class ZhihuSpiderPipeline:
    conn = None
    cursor = None
    def open_spider(self, spider):
        # 进行异常处理，可能会因为我们的疏忽或者数据库的更改造成连接失败，所以，我们要对这部分代码块进行异常捕捉
        try:
            # 连接数据库
            self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='zhihu',
                                        charset='utf8')
            self.cursor = self.conn.cursor()
            print('连接成功<<')
        except Exception as e:
            print(f'连接失败!!>>{e}')
            exit()  # 可以直接结束运行，按需求来设定


    def process_item(self, item, spider):
        cursor_ = item['cursor_']
        excerpt = item['excerpt']
        content = item['content']
        created_time = item['created_time']
        author_id = item['author_id']
        voteup_count = item['voteup_count']
        sql = "INSERT INTO zhihu_qa1 (cursor_, excerpt, content, created_time, author_id, voteup_count) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (str(cursor_), str(excerpt), str(content), str(created_time), str(author_id), int(voteup_count))
        self.cursor.execute(sql, val)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        pass
        # self.cursor.close()