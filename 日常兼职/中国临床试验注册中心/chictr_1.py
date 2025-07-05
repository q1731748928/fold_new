import re
import execjs
import pymysql
import requests


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="part_time_job")
cursor = db.cursor()
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
headers = {
    "Host": "www.chictr.org.cn",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

js = execjs.compile(open('chictr.js', encoding='utf-8').read())
url = "https://www.chictr.org.cn/searchproj.html"
response = requests.get(url, headers=headers)

arg1 = re.findall("var arg1='(.*?)';", response.text)[0]
cookie = js.call('get_cookie', arg1)
cookies = {
    'acw_sc__v2': cookie
}
url = "https://www.chictr.org.cn/searchproj.html"
params = {
    "title": "天附咳喘胶囊治疗慢性阻塞性肺疾病并发肺动脉高压的随机对照临床研究",
    "officialname": "",
    "subjectid": "",
    "regstatus": "",
    "regno": "",
    "secondaryid": "",
    "applier": "",
    "studyleader": "",
    "createyear": "",
    "sponsor": "",
    "secsponsor": "",
    "sourceofspends": "",
    "studyailment": "",
    "studyailmentcode": "",
    "studytype": "",
    "studystage": "",
    "studydesign": "",
    "recruitmentstatus": "",
    "gender": "",
    "agreetosign": "",
    "measure": "",
    "country": "",
    "province": "",
    "city": "",
    "institution": "",
    "institutionlevel": "",
    "intercode": "",
    "ethicalcommitteesanction": "",
    "whetherpublic": "",
    "minstudyexecutetime": "",
    "maxstudyexecutetime": "",
    "btngo": "btn"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
from lxml import etree
tree = etree.HTML(response.text)
hrefs = tree.xpath('//td//a//@href')
for href in hrefs:
    if str(href).__contains__("showproj"):
        detail_url = "https://www.chictr.org.cn/" + href
        print(detail_url)
        res = requests.get(detail_url, headers=headers, cookies=cookies)
        tree = etree.HTML(res.text)
        registration_number = ""
        date_of_last_refreshed_on = ""
        registration_status = ""
        public_title = ""
        applicant = ""
        study_leader = ""
        applicant_telephone = ""
        applicant_e_mail = ""
        applicant_website_voluntary_supply = ""
        applicant_address = ""
        approved_by_ethic_committee = ""
        name_of_the_ethic_committee = ""
        applicant_s_institution = ""
        approved_by_ethic_committee = ""
        primary_sponsor = ""
        secondary_sponsor = ""
        source_of_funding = ""
        target_disease = ""
        study_type = ""
        study_phase = ""
        study_design = ""
        objectives_of_study = ""
        inclusion_criteria = ""
        exclusion_criteria = ""
        study_execute_time = ""
        recruiting_time = ""
        interventions= ""
        countries_of_recruitment_and_research_settings = ""
        outcomes = ""
        collecting_sample = ""
        participant_age = ""
        date_of_approved_by_ethic_committee = ""
        sex = ""
        randomization_procedure = ""
        calculated_results_after_the_study_completed_public_access =""
        ipd_sharing = ""
        data_collection_and_management = ""
        data_and_safety_monitoring_committee = ""

        #
        # study_
        # phase
        # study_design
        # objectives_of_study
        # inclusion_criteria
        # exclusion_criteria
        # study_execute_time
        # recruiting_time
        # varbinary
        # 255
        # false
        # false
        # false
        # interventions
        # 研究实施地点：
        # countries_of_recruitment_and_research_settings
        # outcomes
        # collecting_sample
        # participant_age
        # sex
        # randomization_procedure
        # calculated_results_after_the_study_completed_public_access
        # blinding
        # ipd_sharing
        # data_collection_and_management
        # data_and_safety_monitoring_committee
        # texts = tree.xpath('//div[@class="project-ms"]/table/tbody/tr//td/following-sibling::td//text()')
        # title = str(href).split("/")[-1]
        # for i in range(len(texts)):
        #     # 获取当前的文本
        #     text = texts[i]
        #     # 使用正则表达式替换 \r\n 和空格
        #     ss = re.sub(r'(\r\n| +)+', '', text)
        #     # 处理原文本并排除空字符串
        #     if str(ss).__eq__(""):
        #         continue
        #     else:
        #         print(ss)
        #         with open(f'./{title}.txt', 'a+') as f:
        #             f.write(ss+ "\n")
        #         # for a in range(len(aa)):
        #         #     print(aa[a])
        #         # for j in range(len(aa)):
        #         #     print(f"{j}", f"{aa[j]}")
