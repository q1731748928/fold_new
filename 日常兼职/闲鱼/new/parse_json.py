import ast
import json
import re

import pymysql

def extract_brands(title):
    # 定义常见电子产品品牌列表
    brands = [
        "夏普", "sharp",
        "东芝", "toshiba",
        "酷派","coolpad",
        "索爱","SOAIY",
        "松下","Panasonic",
        "西门子","Siemens",
        "纽曼","Newman",
        "黑莓","blackberry",
        "爱立信","Ericsson",
        "东信","Donson Network",
        "波导","Bird Company",
        "海信","Hisense",
        "海尔","haier",
        "长虹","Changhong", "CHiQ",
        "酷比魔方","cube",
 "摩托罗拉", "Motorola",
 "红米", "redmi",
 "金立", "Gionee",
 "海康威视", "hikvision",
"华为", "Huawei",
"小米", "Xiaomi",
"联想", "Lenovo",
"中兴", "ZTE",
"OPPO", "OPPO",
"vivo", "vivo",
"一加", "OnePlus",
"魅族", "Meizu",
"锤子", "Smartisan",
"诺基亚", "Nokia",
"TCL", "TCL",
"海信", "Hisense",
"创维", "Skyworth",
"海尔", "Haier",
"紫米", "ZMI",
"步步高", "BBK",
"大疆", "DJI",
"360", "360",
"黑鲨", "Black Shark",
"坚果", "Smartisan",
"乐视", "LeEco",
"科大讯飞", "iFlytek",
"华硕", "ASUS",
"苹果", "Apple", "iPhone",
"三星", "Samsung",
"索尼", "Sony",
"戴尔", "Dell",
"惠普", "HP",
"微软", "Microsoft",
"英特尔", "Intel",
"尼康", "Nikon",
"佳能", "Canon",
"LG", "LG",
"雷蛇", "Razer",
"HTC", "HTC",
"飞利浦", "Philips",
"博世", "Bosch",
"西部数据", "Western Digital",
"赛米控", "Siemens",
"特斯拉", "Tesla",
"亚马逊", "Amazon",
"富士", "Fujifilm",
"松下", "Panasonic",
"摩托罗拉", "Motorola",
"高通", "Qualcomm",
"雷神", "Thunderobot",
"AMD", "AMD",
"英伟达", "NVIDIA"
]
    # 构建正则表达式模式
    # 使用 re.escape 确保品牌名称中有特殊字符时不会被错误匹配
    pattern = r'|'.join(re.escape(brand) for brand in brands)
    # 假设 title 是待搜索的字符串
    # 使用 re.IGNORECASE 来忽略大小写
    matches = re.findall(pattern, title, flags=re.IGNORECASE)
    return matches


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
query = "SELECT id, result_list, keyword FROM xy"  # 替换 your_table 为你的表名
cursor.execute(query)

# 二手电子产品(手机、平板、电脑)，特征爬价格，成色，品牌，内存，颜色，保修状态，卖家信用，几人想要，地区
# 获取所有查询结果
results = cursor.fetchall()

# 打印每一行的 id 和 result_list
for row in results:
    id_value = row[0]
    result_list = row[1]
    keyword = row[2]
    dict_obj = ast.literal_eval(result_list)
    # 标题
    title = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('detailParams', {}).get('title', None)
    itemId = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('detailParams', {}).get('itemId', None)
    # 价格
    price = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('clickParam', {}).get('args', {}).get('price',None)
    # 地区
    area = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('area', None)
    tagLists_r2 = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('fishTags', {}).get('r2', {}).get('tagList', None)
    tagLists_r3 = dict_obj.get('data', {}).get('item', {}).get('main', {}).get('exContent', {}).get('fishTags', {}).get('r3', {}).get('tagList', None)
    # 成色
    fineness = ""
    # 品牌
    brand = ""
    # 保修状态
    repair_status = ""
    # 卖家信用
    credit = "卖家信用极好"
    # 内存
    storage = ''
    # 颜色
    color = ''
    # 多少人想要
    wanted = ''
    if tagLists_r3 != None:
        for tagList in tagLists_r3:
            labelId = tagList['data']['labelId']
            # 9:想要的人数
            if labelId == '9':
                wanted = tagList['data']['content']
    if tagLists_r2 != None:
        for tagList in tagLists_r2:
            labelId = tagList['data']['labelId']
            # 34:内存
            if labelId == '34':
                storage = tagList['data']['content']
            # 35:保修状态
            if labelId == '35':
                repair_status = tagList['data']['content']
            # 36:成色
            elif labelId == '36':
                fineness = tagList['data']['content']
            # 38:品牌
            elif labelId == '38':
                brand = tagList['data']['content']
    if brand == '':
        new_brand = extract_brands(title)
        if len(new_brand) > 0:
            brand = new_brand[0]
    # print(itemId, title, wanted, storage, fineness, brand, repair_status)
    # 二手电子产品(手机、平板、电脑)，特征爬价格，成色，品牌，内存，颜色，保修状态，卖家信用，几人想要，地区
    try:
        sql = "INSERT INTO xy_detail_test (item_id, keyword, title, price, fineness, brand, storage, color, repair_status, credit, wanted, area) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (itemId, keyword, title, price, fineness, brand, storage, color, repair_status, credit, wanted, area)
        cursor.execute(sql, val)
        db_connection.commit()
    except Exception as e:
        print(e.args)

# 关闭游标和数据库连接

