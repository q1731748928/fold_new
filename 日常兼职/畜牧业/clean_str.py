import ast
import json
import re

import pandas as pd

with open('/Users/hejie/PycharmProjects/turing_exec/日常兼职/畜牧业/China.txt', 'r') as f:
    r1 = f.read()
# ids = re.findall(r"'id': (.*?),", r1)
# scenarios = re.findall(r"'scenario': (.*?),", r1)
#
# # 转换为整数列表
# ds = [int(id) for id in ids]
# for d in ds:
#     print(d)

data_dict = ast.literal_eval(r1)
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
    # print(id, scenario, parameter, str_value, code, name, order, type, unit, category_id, category, module, feedgroup_id, feedgroup, feedstuff, manuremanagement_id, manuremanagement, specie, production_system_id, production_system, orientation_id, orientation)
    # print(f'id:{id}, scenario:{scenario}, parameter:{parameter}, str_value:{str_value}, code:{code}, name:{name}, order:{order}, type:{type}, unit:{unit}, category_id:{category_id}, category:{category}, module:{module}, feedgroup_id:{feedgroup_id}, feedgroup:{feedgroup}, feedstuff:{feedstuff}, manuremanagement_id:{manuremanagement_id}, manuremanagement:{manuremanagement}, specie:{specie}, production_system_id:{production_system_id}, production_system:{production_system}, orientation_id:{orientation_id}, orientation:{orientation}')
    obj = {
        'country': 'China',
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
columns = ['country', 'id', 'scenario', 'parameter', 'str_value', 'code', 'name', 'order', 'type', 'unit', 'category', 'category_id', 'module', 'feedgroup_id', 'feedgroup', 'feedstuff', 'manuremanagement_id', 'manuremanagement', 'specie', 'production_system_id', 'production_system', 'orientation_id', 'orientation']
# 将 DataFrame 写入 Excel，指定列头
df.to_excel('China.xlsx', index=False, columns=columns, engine='openpyxl')
print("数据已成功写入到 China.xlsx 文件！")

