import ast
import json

import pymysql

# 连接到MySQL数据库
db_connection = pymysql.connect(
    host="localhost",          # MySQL 主机
    user="root",          # 用户名
    password="123456",  # 密码
    database="part_time_job"   # 数据库名称
)

# 创建一个游标对象来执行查询
cursor = db_connection.cursor()

# 执行查询以获取所有的 id 和 result_list
query = "SELECT id, data FROM xy limit 10"  # 替换 your_table 为你的表名
cursor.execute(query)

# 二手电子产品(手机、平板、电脑)，特征爬价格，成色，品牌，内存，颜色，保修状态，卖家信用，几人想要，地区
# 获取所有查询结果
results = cursor.fetchall()

# 打印每一行的 id 和 result_list
for row in results:
    id_value = row[0]
    result_list = row[1]
    print(result_list)
    # dict_obj = ast.literal_eval(result_list)
    # title = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('detailParams', {}).get('title', None)
    # price = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('clickParam', {}).get('args', {}).get('price',None)
    # area = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('area', None)
    # r2 = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', None)
    # print(r2)
# 关闭游标和数据库连接

