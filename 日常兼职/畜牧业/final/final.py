import ast
import json
import re
import time

import pandas as pd
import pymysql
from lxml import etree
import requests
session = requests.session()
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="part_time_job")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
class Gleami:
    def __init__(self):
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
        }
    def get_cookie(self):
        url = "https://gleami.apps.fao.org/"
        response = session.get(url, headers=self.headers)
        return response.headers
    def get_country(self, cookie_headers, region_selection, country_selection):
        sessionid = re.search(r"sessionid=(.*?);", str(cookie_headers)).group(1)
        csrftoken = re.search(r"csrftoken=(.*?);", str(cookie_headers)).group(1)
        self.cookies = {
            "csrftoken": csrftoken,
            "sessionid": sessionid,
            "_ga": "GA1.1.1163173444.1747796148",
            "_ga_D1DDJEPMCW": "GS2.1.s1747796148$o1$g1$t1747796305$j0$l0$h0"
        }
        url = "https://gleami.apps.fao.org/"
        # China
        data = {
            "region_selection": region_selection,
            "country_selection": country_selection,
            "csrfmiddlewaretoken": csrftoken
        }
        response = session.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.headers
    def get_animal(self, csrftoken):
        url = "https://gleami.apps.fao.org/animals_selection"
        data = {
            'productionsys': ['1_1', '1_2', '2_3', '2_4', '3_5', '3_6', '4_7', '4_8', '5_9', '5_10', '5_11', '6_12',
                              '6_13', '6_14'],
            'animalproductionsysproduct': [
                '1_1_1', '1_1_2', '1_2_1', '1_2_2', '2_3_1', '2_3_2', '2_4_1', '2_4_2',
                '3_5_1', '3_5_2', '3_6_1', '3_6_2', '4_7_1', '4_7_2', '4_8_1', '4_8_2',
                '5_9_3', '5_10_1', '5_11_3', '6_12_1', '6_13_1', '6_14_1'
            ],
            'csrfmiddlewaretoken': csrftoken
        }
        response =  session.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.headers

    def get_module(self, csrftoken):
        url = "https://gleami.apps.fao.org/modules_selection"
        data = {
            'moduleparameters': [
                '1_1', '1_2', '1_3', '1_9', '1_11',
                '2_1', '2_2', '2_3', '2_4', '2_5', '2_6',
                '3_6'
            ],
            'csrfmiddlewaretoken': csrftoken
        }
        response = session.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.headers

    def get_base(self, csrftoken):
        url = "https://gleami.apps.fao.org/baseline_selection"
        data = {
            "csrfmiddlewaretoken": csrftoken,
            "baseline_selection": "",
            "skip_btn": "skip"
        }
        response = session.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.headers

    def get_scenarios(self, csrftoken):
        url = "https://gleami.apps.fao.org/scenarios"
        data = {
            "csrfmiddlewaretoken": csrftoken,
            "scenario": ""
        }
        response = session.post(url, headers=self.headers, cookies=self.cookies, data=data)
        return response.headers

    def get_input(self, csrftoken):
        self.cookies['csrftoken'] = csrftoken
        url = "https://gleami.apps.fao.org/input"
        response = session.get(url, headers=self.headers, cookies=self.cookies)
        return response.text



    def get_headers(self, cookie):
        csrftoken = re.search(r"csrftoken=(.*?);", str(cookie))
        csrftoken = csrftoken.group(1)
        return csrftoken

    def clean_str(self, input_html, country, region_selection, country_selection):
        data_dict = ast.literal_eval(input_html)
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
                val = (country, id, scenario, parameter, str_value, code, name, order, type, unit, category, category_id, module, feedgroup_id, feedgroup, feedstuff, manuremanagement_id, manuremanagement, specie, production_system_id, production_system, orientation_id, orientation, region_selection, country_selection)
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
                'orientation': orientation,
                'region_selection': region_selection,
                'country_selection': country_selection
            }
            data.append(obj)

            # 创建 DataFrame
        df = pd.DataFrame(data)
        # 指定列头
        columns = ['country', 'id', 'scenario', 'parameter', 'str_value', 'code', 'name', 'order', 'type', 'unit',
                   'category', 'category_id', 'module', 'feedgroup_id', 'feedgroup', 'feedstuff', 'manuremanagement_id',
                   'manuremanagement', 'specie', 'production_system_id', 'production_system', 'orientation_id',
                   'orientation', 'region_selection', 'country_selection']
        # 将 DataFrame 写入 Excel，指定列头
        df.to_excel(f'./{country}.xlsx', index=False, columns=columns, engine='openpyxl')
        result = f"数据已成功写入到{country}.xlsx 文件！"
        return result


if __name__ == '__main__':
    gleami = Gleami()
    cookie_headers = gleami.get_cookie()
    with open('/Users/hejie/PycharmProjects/turing_exec/日常兼职/畜牧业/final/country_code.txt', 'r') as f:
        country_str = f.read()
    pattern = r"countries_by_regions\['(\d+)'\] = \[\['', '-------'\],(.*?)\];"
    matches = re.findall(pattern, country_str, re.DOTALL)
    result = []
    for region_selection, country_selection in matches:
        country_pattern = r'\[(\d+), \'(.*?)\'\]'
        country_matches = re.findall(country_pattern, country_selection)
        for num, country in country_matches:
            print(f'{region_selection} {num} {country}')
            country_headers = gleami.get_country(cookie_headers, str(region_selection), str(num))
            country_csrftoken = gleami.get_headers(country_headers)
            animal_headers = gleami.get_animal(country_csrftoken)
            animal_csrftoken = gleami.get_headers(animal_headers)
            module_headers = gleami.get_module(animal_csrftoken)
            # time.sleep(180)
            module_csrftoken = gleami.get_headers(module_headers)
            base_headers = gleami.get_base(module_csrftoken)
            base_csrftoken = gleami.get_headers(base_headers)
            scenarios_headers = gleami.get_scenarios(base_csrftoken)
            scenarios_csrftoken = gleami.get_headers(scenarios_headers)
            input_html = gleami.get_input(scenarios_csrftoken)
            tree = etree.HTML(input_html)
            script_data = tree.xpath("//script[contains(., 'var allinput_data =')]/text()")[0]
            if script_data:
                # Use regex to extract the JSON part
                json_match = re.search(r"var allinput_data = (\[.*?\]);", str(script_data), re.S)
                if json_match:
                    json_string = json_match.group(1)
                    obj = json.dumps(json_string)
                    aa = json.loads(obj)
                    result = gleami.clean_str(aa, country, region_selection, str(num))
            print(result)






