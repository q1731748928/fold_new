import json
import csv
import requests
import random
import time
class Luyahu(object):

    def __init__(self):
        self.url = 'https://shopsearch.taobao.com/search?'
        self.hearders = {
            "cookie": "t=e7ee30e05032ce5cbf574f26628217b4; cookie2=1befc75c1718e129e2181b1f3bf37509; _tb_token_=34ef853a131ee; _samesite_flag_=true; thw=cn; sgcookie=E100l15W6YCZDAdnPj9uTYYsYozrGPQxhz%2FwyaWVpxsIGSWFziQmy%2FyQPCnqFa4c0%2BRT55hkrr9vEl7VQeOvsSTZpPNCQ1mz7xzKHBVlkWgAruk%3D; _m_h5_tk=102c748e4d11158cdde549fbc00d7c00_1677643604998; _m_h5_tk_enc=e107e2a21d36f4ee9766e62d992d5b9b; _utk=VocP@qJyn^AtWdm; xlly_s=1; mt=ci=0_0; tracknick=; cna=mByVGUv7fB8CAXQYWRJi2IH0; JSESSIONID=ED7D54624FB9625B2C674E3EE100901D; l=fBOFc8qrLXOlf6KFBO5Clurza77TidOfCoVzaNbMiIEGC6DF6Xv9ZqtQ2uotdpKRR8XPiDTB45k_ZipT5eV88yDj3RRmI3YHifO2CeTIK7Nk_; isg=BG5uswaShlvRR_S1WfdYwdEWv8QwbzJpc2DSwpg613ONewvVAP6EeLY9M-eXpyqB; tfstk=cWsABRcAS7VDZBPM4nUo7yp6Av_ACGavs7AEXMlemUUucVQNSg1mWMjd84okpBRYe",
            "pragma": "no-cache",
            "referer": "https://shopsearch.taobao.com/search?q=%E5%8D%A4%E9%B8%AD%E8%B4%A7&js=1&initiative_id=staobaoz_20230303&ie=utf8&s=20",
            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

    def get_data(self,params):
        response = requests.get(url=self.url,params=params,headers=self.hearders)

        print(response.json())
        return response.json()
    def paras_data(self,response):
        # with open('淘宝卤鸭货.csv', 'a', encoding='utf-8', newline='') as f:
        #     file_name = ['店铺名称', '好评率', '荣誉等级', '动态评分_描述相符', '动态评分_描述相符同行业相比',
        #                  '动态评分_服务态度', '动态评分_服务态度同行业相比', '动态评分_物流服务',
        #                  '动态评分_物流服务同行业相比']
        #     writer = csv.DictWriter(f,file_name)
        #     # writer.writeheader()

            data_list = response['mods']['shoplist']['data']['shopItems']
            for i in data_list:
                item = {}
                item['店铺名称'] = i['title']
                if 'goodratePercent' in i:
                    item['好评率'] = i['goodratePercent']
                else:
                    item['好评率'] = '无'
                item['荣誉等级'] = i['shopIcon']['iconClass'].split('-')[2]
                Dynamic_scoring_dict = json.loads(i['dsrInfo']['dsrStr'])
                item['动态评分_描述相符'] =Dynamic_scoring_dict['mas']
                if float(Dynamic_scoring_dict['mg'].strip('%'))/100>=0:

                    item['动态评分_描述相符同行业相比'] = '高于'+ Dynamic_scoring_dict['mg']
                else:
                    item['动态评分_描述相符同行业相比'] = '低于' + Dynamic_scoring_dict['mg']
                item['动态评分_服务态度'] =Dynamic_scoring_dict['sas']
                if float(Dynamic_scoring_dict['cas'].strip('%'))/100 >=0:
                    item['动态评分_服务态度同行业相比'] = '高于'+Dynamic_scoring_dict['cas']
                else:
                    item['动态评分_服务态度同行业相比'] = '低于' + Dynamic_scoring_dict['cas']
                item['动态评分_物流服务'] =Dynamic_scoring_dict['mas']
                if float(Dynamic_scoring_dict['cg'].strip('%'))/100 >=0:
                    item['动态评分_物流服务同行业相比'] = '高于'+Dynamic_scoring_dict['cg']
                else:
                    item['动态评分_物流服务同行业相比'] = '低于' + Dynamic_scoring_dict['cg']
                #print(Dynamic_scoring_dict)
                print(item)

                yield item

    def get_totalPage(self):
        params = {
            "data-key": "s",
            "data-value": 0,
            "ajax": "true",
            "_ksTS": "1677832873316_506",
            # "callback": "jsonp507",
            "q": "卤鸭货",
            "js": "1",
            "initiative_id": "staobaoz_20230304",
            "ie": "utf8",
            "s": 0
        }
        res = requests.get(url=self.url, params=params, headers=self.hearders).json()
        totalPage = res['mods']['pager']['data']['totalPage']
        return totalPage

    def main(self):
        page = int(self.get_totalPage())
        with open('淘宝卤鸭货.csv', 'a', encoding='utf-8', newline='') as f:
            file_name = ['店铺名称', '好评率', '荣誉等级', '动态评分_描述相符', '动态评分_描述相符同行业相比',
                         '动态评分_服务态度', '动态评分_服务态度同行业相比', '动态评分_物流服务',
                         '动态评分_物流服务同行业相比']
            writer = csv.DictWriter(f, fieldnames=file_name)
            writer.writeheader()

            for i in range(0,page):
                params = {
                    "data-key": "s",
                    "data-value": i*20,
                    "ajax": "true",
                    "_ksTS": "1677832873316_506",
                    #"callback": "jsonp507",
                    "q": "卤鸭货",
                    "js": "1",
                    "initiative_id": "staobaoz_20230304",
                    "ie": "utf8",
                    "s":i*20
                }
                print('正在抓取第{}页数据'.format(i))
                response = self.get_data(params)
                res = self.paras_data(response)
                writer.writerows(res)
                time.sleep(round(random.uniform(2, 5), 3))
            print('数据抓取已完成')

if __name__ == '__main__':
    l = Luyahu()
    #l.get_totalPage()
    l.main()
