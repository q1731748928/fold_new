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
        for i in range(1, 6):
            tr1 = tree.xpath(f'//div[@class="project-ms"][1]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 注册号
                registration_number = tr1
                print(registration_number)
            if i == 2:
                # 最近更新日期:
                date_of_last_refreshed_on = tr1
                print(date_of_last_refreshed_on)
            if i == 4:
                # 注册号状态
                registration_status = tr1
            if i == 6:
                # 注册题目
                public_title = tr1
        for i in range(1, 10):
            tr2 = tree.xpath(f'//div[@class="project-ms"][2]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 申请注册联系人 研究负责人
                applicant = tr2
                study_leader = tr2
                print(applicant)
            if i == 3:
                # 申请注册联系人电话
                applicant_telephone = tr1
            if i == 5:
                # 申请注册联系人电子邮件
                applicant_e_mail = tr1
            if i == 6:
                # 申请单位网址(自愿提供)
                applicant_website_voluntary_supply = tr1
            if i == 7:
                # 申请注册联系人通讯地址
                applicant_address = tr1
            if i == 8:
                # 申请人所在单位
                applicant_s_institution = tr1
        for i in range(1, 5):
            tr3 = tree.xpath(f'//div[@class="project-ms"][3]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 是否获伦理委员会批准
                approved_by_ethic_committee = tr3
            if i == 2:
                # 批准本研究的伦理委员会名称
                name_of_the_ethic_committee = tr3
            if i == 4:
                # 伦理委员会批准日期
                date_of_approved_by_ethic_committee = tr3
        for i in range(1, 24):
            tr4 = tree.xpath(f'//div[@class="project-ms"][4]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 研究实施负责（组长）单位
                primary_sponsor = tr4
            if i == 5:
                # 试验主办单位
                secondary_sponsor = tr4
            if i == 6:
                # 经费或物资来源
                source_of_funding = tr4
            if i == 8:
                # 研究疾病
                target_disease = tr4
            if i == 12:
                # 研究类型
                study_type = tr4
            if i == 13:
                # 研究所处阶段
                study_phase = tr4
            if i == 14:
                # 研究设计
                study_design = tr4
            if i == 18:
                # 研究目的
                objectives_of_study = tr4
            if i == 22:
                # 纳入标准：
                inclusion_criteria = tr4
            if i == 24:
                # 排除标准
                exclusion_criteria = tr4
        # for i in range(1, 2):
        #     tr4_ = tree.xpath(f'//div[@class="project-ms"][4]/table[2]/tbody/tr[position()={i}]/td[2]/text()')[0]
        #     if i == 1:
        #         tr4__ = tree.xpath(f'//div[@class="project-ms"][4]/table[2]/tbody/tr[position()={i}]/td[4]/text()')[0]
        #         # 研究实施时间
        #         study_execute_time = tr4__
        #     if i == 2:
        #         # 征募观察对象时间
        #         recruiting_time = tr4__
        for i in range(1, 2):
            tr5 = tree.xpath(f'//div[@class="project-ms"][5]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 干预措施
                interventions = tr5
        for i in range(1, 2):
            tr6 = tree.xpath(f'//div[@class="project-ms"][6]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 研究实施地点
                countries_of_recruitment_and_research_settings = tr6
        for i in range(1, 2):
            tr7 = tree.xpath(f'//div[@class="project-ms"][7]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 测量指标
                outcomes = tr7
        for i in range(1, 2):
            tr8 = tree.xpath(f'//div[@class="project-ms"][8]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 采集人体标本
                collecting_sample = tr8
                # # 年龄范围
                # tr8_ = tree.xpath(f'//div[@class="project-ms"][8]/table/tbody/tr[position()={i}]/td[3]/text()')[0]
                # participant_age = tr8_
            if i == 2:
                # 性别
                sex = tr8
            if i == 3:
                # 随机方法
                randomization_procedure = tr8
        for i in range(1, 5):
            tr10 = tree.xpath(f'//div[@class="project-ms"][10]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 是否公开试验完成后的统计结果
                calculated_results_after_the_study_completed_public_access = tr10
        for i in range(1, 2):
            tr11 = tree.xpath(f'//div[@class="project-ms"][11]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            if i == 1:
                # 是否共享原始数据
                ipd_sharing = tr11
            if i == 2:
                # 盲法
                blinding = tr11
        for i in range(1, 2):
                # 数据采集和管理
                tr12 = tree.xpath(f'//div[@class="project-ms"][12]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
                data_collection_and_management = tr12
        for i in range(1, 6):
            tr13 = tree.xpath(f'//div[@class="project-ms"][13]/table/tbody/tr[position()={i}]/td[2]/text()')[0]
            # 数据与安全监察委员会
            if i == 4:
                # 数据与安全监察委员会
                data_collection_and_management = tr13
            if i == 6:
                # 数据与安全监察委员会
                data_and_safety_monitoring_committee = tr13
        sql = "INSERT INTO chictr (registration_number,date_of_last_refreshed_on,registration_status,registration_status,public_title,applicant,study_leader,applicant_telephone,applicant_e_mail,applicant_website_voluntary_supply,applicant_address,applicant_s_institution,approved_by_ethic_committee,name_of_the_ethic_committee,date_of_approved_by_ethic_committee,primary_sponsor,secondary_sponsor,source_of_funding,target_disease,study_type,study_phase,study_design,objectives_of_study,inclusion_criteria,exclusion_criteria,study_execute_time,recruiting_time,interventions,countries_of_recruitment_and_research_settings,outcomes,collecting_sample,participant_age,sex,randomization_procedure,calculated_results_after_the_study_completed_public_access,blinding,ipd_sharing,data_collection_and_management,data_and_safety_monitoring_committee) " \
              "VALUES " \
              "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
        val = (registration_number,date_of_last_refreshed_on,registration_status,registration_status,public_title,applicant,study_leader,applicant_telephone,applicant_e_mail,applicant_website_voluntary_supply,applicant_address,applicant_s_institution,approved_by_ethic_committee,name_of_the_ethic_committee,date_of_approved_by_ethic_committee,primary_sponsor,secondary_sponsor,source_of_funding,target_disease,study_type,study_phase,study_design,objectives_of_study,inclusion_criteria,exclusion_criteria,study_execute_time,recruiting_time,interventions,countries_of_recruitment_and_research_settings,outcomes,collecting_sample,participant_age,sex,randomization_procedure,calculated_results_after_the_study_completed_public_access,blinding,ipd_sharing,data_collection_and_management,data_and_safety_monitoring_committee)
        cursor.execute(sql, val)
        db.commit()
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
