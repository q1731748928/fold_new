import ast
import json
import re

import pandas as pd
import pymysql
from lxml import etree

import requests

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="part_time_job")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://gleami.apps.fao.org/scenarios",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
cookies = {
    "csrftoken": "wzxckJwgjbFAX0yqKTay9f39EF3KeXtSgittW4Ye1CnwqrV2NJ42Lvcu5i4wyvDm",
    "sessionid": "a73i21ci6s8oodal0343j86emcdtppj9",
    "_ga": "GA1.1.1741455245.1747800973",
    "_ga_D1DDJEPMCW": "GS2.1.s1747803804$o2$g1$t1747803921$j0$l0$h0"
}
url = "https://gleami.apps.fao.org/input"
response = requests.get(url, headers=headers, cookies=cookies)
tree = etree.HTML(response.text)
country = tree.xpath('//div[@class="col-lg-3 text-right"]/text()')[0]
country = re.sub(r'[\n\s]+', '', country)
script_data = tree.xpath("//script[contains(., 'var allinput_data =')]/text()")[0]
if script_data:
        # Use regex to extract the JSON part
    json_match = re.search(r"var allinput_data = (\[.*?\]);", str(script_data), re.S)
    if json_match:
        json_string = json_match.group(1)
        obj = json.dumps(json_string)
        aa = json.loads(obj)
        data_dict = ast.literal_eval(aa)
region_selection = "1"
country_selection = "42"
country = "China, mainland"
data = []
# 输出结果
for d in data_dict:
    id = d.get('id')
    scenario = d.get('scenario')
    parameter = d.get('parameter')
    str_value = d.get('str_value')
    code = d.get('code')
    name = d.get('name')
    order = d.get('order')
    type = d.get('type')
    unit = d.get('unit')
    category_id = d.get('category_id')
    category = d.get('category')
    module = d.get('module')
    feedgroup_id = d.get('feedgroup_id')
    feedgroup = d.get('feedgroup')
    feedstuff = d.get('feedstuff')
    manuremanagement_id = d.get('manuremanagement_id')
    manuremanagement = d.get('manuremanagement')
    specie = d.get('specie')
    production_system_id = d.get('production_system_id')
    production_system = d.get('production_system')
    orientation_id = d.get('orientation_id')
    orientation = d.get('orientation')
    try:
        sql = "INSERT INTO gleami (country ,id	 ,scenario ,parameter ,str_value ,code ,name ,`order` ,type ,unit ,category ,category_id ,module ,feedgroup_id ,feedgroup ,feedstuff ,manuremanagement_id	,manuremanagement	,specie ,production_system_id,production_system	,orientation_id ,orientation ,region_selection	,country_selection	) VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
        country, id, scenario, parameter, str_value, code, name, order, type, unit, category, category_id, module,
        feedgroup_id, feedgroup, feedstuff, manuremanagement_id, manuremanagement, specie, production_system_id,
        production_system, orientation_id, orientation, region_selection, country_selection)
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
    # print(id, scenario, parameter, str_value, code, name, order, type, unit, category_id, category, module, feedgroup_id, feedgroup, feedstuff, manuremanagement_id, manuremanagement, specie, production_system_id, production_system, orientation_id, orientation)
    # print(f'id:{id}, scenario:{scenario}, parameter:{parameter}, str_value:{str_value}, code:{code}, name:{name}, order:{order}, type:{type}, unit:{unit}, category_id:{category_id}, category:{category}, module:{module}, feedgroup_id:{feedgroup_id}, feedgroup:{feedgroup}, feedstuff:{feedstuff}, manuremanagement_id:{manuremanagement_id}, manuremanagement:{manuremanagement}, specie:{specie}, production_system_id:{production_system_id}, production_system:{production_system}, orientation_id:{orientation_id}, orientation:{orientation}')
    obj = {
        'country': country,
        'id': id,
        'scenario': scenario,
        'parameter': parameter,
        'str_value': str_value,
        'code': code,
        'name': name,
        'order': order,
        'type': type,
        'unit': unit,
        'category_id': category_id,
        'category': category,
        'module': module,
        'feedgroup_id': feedgroup_id,
        'feedgroup': feedgroup,
        'feedstuff': feedstuff,
        'manuremanagement_id': manuremanagement_id,
        'manuremanagement': manuremanagement,
        'specie': specie,
        'production_system_id': production_system_id,
        'production_system': production_system,
        'orientation_id': orientation_id,
        'orientation': orientation
    }
    data.append(obj)

    # 创建 DataFrame
df = pd.DataFrame(data)
# 指定列头
columns = ['country', 'id', 'scenario', 'parameter', 'str_value', 'code', 'name', 'order', 'type', 'unit',
           'category', 'category_id', 'module', 'feedgroup_id', 'feedgroup', 'feedstuff', 'manuremanagement_id',
           'manuremanagement', 'specie', 'production_system_id', 'production_system', 'orientation_id',
           'orientation']
# 将 DataFrame 写入 Excel，指定列头
df.to_excel(f'{country}.xlsx', index=False, columns=columns, engine='openpyxl')
result = f"数据已成功写入到{country}.xlsx 文件！"
