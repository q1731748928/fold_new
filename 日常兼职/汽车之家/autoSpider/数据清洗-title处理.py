import json

import requests

import subprocess

import pymysql

def query1(sql):
    """
    不带参数查询
    :param sql:
    :return:
    """
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="car_info")
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.execute(sql)  # 执行sql查询语句
    result = cursor.fetchone()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果


sql = 'select  car_model_configuration from car_model where car_model_name = "海豹06 DM-i";'
result = query1(sql)[0]
json_dic = json.loads(result)
titlelist = json_dic.get('titlelist')
car_dict = dict()
car_list = list()
car_info_list = list()
for title in titlelist:
    itemtype = title.get('itemtype')
    groupname = title.get('groupname')
    sort = title.get('sort')
    # print(itemtype)
    items = title.get('items')
    new_list = list()
    new_info_list = list()
    for item in items:
        new_dict = dict()
        titleid = item.get('titleid')
        itemname = item.get('itemname')
        new_dict[titleid] = itemname
        new_list.append(new_dict)
        new_info_list.append(titleid)
    car_dict[itemtype] = new_list
    car_info_list.append(new_info_list)
car_list.append(car_dict)

# for car in car_list:
#     print(car)
for i in range(0, len(car_list)):
    for key,car_list in car_list[i].items():
        print(key, car_list)

# for car in car_list:
#     for key, values in car.items():
#         for value in values:
#             for va in value.items():
#                 va_0 = va[0]
#                 va_1 = va[1]
#                 print(va_0, va_1)

