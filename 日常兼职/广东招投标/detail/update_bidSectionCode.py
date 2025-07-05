# 连接到MySQL数据库
import json

import pymysql

db_connection = pymysql.connect(
    host="localhost",  # MySQL 主机
    user="root",  # 用户名
    password="123456",  # 密码
    database="part_time_job"  # 数据库名称
)

cursor = db_connection.cursor()
query = "SELECT notice_id, data, title  FROM gzztb_detail where  bid_section_code is null"
# Number of rows to insert at once
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    notice_id = row[0]
    data = row[1]
    title = row[2]
    js = json.loads(data)
    datas = js['data']
    if len(datas) > 0:
        # if 'bidSectionCode' in datas[0]:
        #     bidSectionCode = datas[0]['bidSectionCode']
        #     sql = """
        #            UPDATE gzztb_detail
        #            SET bid_section_code = %s
        #            WHERE notice_id = %s
        #         """
        #     # 使用参数化查询执行
        #     cursor.execute(sql, (bidSectionCode, notice_id))
        #     db_connection.commit()
        if str(datas[0]).__contains__('bidSectionCodes'):
            for data_s in datas:
                for data in data_s:
                    bidSectionCodes = data['bidSectionCodes']
                    try:
                        sql = """
                             UPDATE gzztb_detail
                             SET bid_section_code = %s
                             WHERE notice_id = %s
                         """
                        # 使用参数化查询执行
                        cursor.execute(sql, (bidSectionCodes, notice_id))
                        db_connection.commit()
                        break
                    except Exception as e:
                        continue
                        print(e)
            # bidSectionCodes = datas[0]['bidSectionCodes']
            # sql = """
            #        UPDATE gzztb_detail
            #        SET bid_section_code = %s
            #        WHERE notice_id = %s
            #     """
            # # 使用参数化查询执行
            # cursor.execute(sql, (bidSectionCodes, notice_id))
            # db_connection.commit()
