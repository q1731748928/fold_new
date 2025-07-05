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
car_title_list = list()
car_title_id_list = list()
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
    car_title_id_list.append(new_info_list)
car_title_list.append(car_dict)

car_ll_list = list()
for car_title in car_title_list:
    # print(car_title)
    for key, values in car_title.items():
        for value in values:
            for va in value.items():
                car_ll_dict = dict()
                va_0 = va[0]
                va_1 = va[1]
                car_ll_dict[va_0] = va_1
                car_ll_list.append(car_ll_dict)
                # print(va_0, va_1)



datalist = json_dic.get('datalist')
car_list = list()
for data in datalist:
    car_dict = dict()
    specid = data.get('specid')
    car_dict["specid"] = specid
    specname = data.get('specname')
    car_dict["specname"] = specname
    specstatus = data.get('specstatus')
    car_dict["specstatus"] = specstatus
    year = data.get('year')
    car_dict["year"] = year
    minprice = data.get('minprice')
    car_dict["minprice"] = minprice
    dealerprice = data.get('dealerprice')
    car_dict["dealerprice"] = dealerprice
    condition = data.get('condition')
    car_list.append(car_dict)
    paramconflist = data.get('paramconflist')
    model_final_dict = dict()
    model_final_big_list = list()
    model_final_list = list()
    nn_list = list()
    for paramconf in paramconflist:
        nn_dict = dict()
        titleid = paramconf.get('titleid')
        itemname = paramconf.get('itemname')
        nn_dict['titleid'] = itemname
        new_list.append(nn_dict)

    for i in range(0, len(car_title_list)):
        for key, car_list in car_title_list[i].items():
            print(key)
            for car in car_list:
                print(car)

                # model_final_dict[key] = model_final_list
                # model_final_big_list.append(model_final_dict)
            # model_final_dict['发动机'] = model_final_list
    # model_final_dict['发动机'] = model_final_list
    # model_final_big_list.append(model_final_dict)
    # print(model_final_big_list)


