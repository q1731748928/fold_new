import json
from itertools import chain

import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="car_info")
cursor = db.cursor()  # 使用cursor（）方法获取游标


def query1(sql):
    """
    不带参数查询
    :param sql:
    :return:
    """
    cursor.execute(sql)  # 执行sql查询语句
    result = cursor.fetchall()  # 记录查询结果
    return list(chain.from_iterable(result))  # 返回查询结果


# sql = 'SELECT car_model_configuration from car_model WHERE car_model_name like "%比亚迪%";'
sql = 'SELECT car_model_configuration from car_model;'
result = query1(sql)
for res1 in result:
    json_dic = json.loads(res1)
    bread = json_dic.get('bread')
    brandname = bread.get('brandname')
    seriesid = bread.get('seriesid')
    seriesname = bread.get('seriesname')
    specid = bread.get('specid')
    specname = bread.get('specname')
    seriesstate = bread.get('seriesstate')
    brandid = bread.get('brandid')
    brandname = bread.get('brandname')
    titlelist = json_dic.get('titlelist')
    datalist = json_dic.get('datalist')
    for data in datalist:
        specid = data.get('specid')
        specname = data.get('specname')
        specstatus = data.get('specstatus')
        year = data.get('year')
        minprice = data.get('minprice')
        dealerprice = data.get('dealerprice')
        condition = data.get('condition')
        paramconflist = data.get('paramconflist')
        try:
            for paramconf in paramconflist:
                titleid = paramconf.get('titleid')
                itemname = paramconf.get('itemname')
                sql = "INSERT INTO car_model_detail values (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (0,brandid, brandname,seriesid,seriesname,specid,specname, seriesstate,specstatus, year,minprice,dealerprice,str(condition),titleid,"",itemname,"")
                cursor.execute(sql, val)
                db.commit()
        except Exception as e:
            print(e)

    # 开始更新数据
    for title in titlelist:
        itemtype = title.get('itemtype')
        # print(itemtype)
        items = title.get('items')
        for item in items:
            titleid = item.get('titleid')
            itemname = item.get('itemname')
            # TODO update需要加条件了
            cursor.execute('UPDATE car_model_detail SET titleinfo = %s WHERE titleid = %s', (itemname, titleid))
            cursor.execute('UPDATE car_model_detail SET maingroup = %s WHERE titleid = %s', (itemtype, titleid))
            db.commit()


db.close()

