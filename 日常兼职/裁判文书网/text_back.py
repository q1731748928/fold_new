# coding=utf-8
import pymysql
from lxml import etree
import re
db_connection = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="part_time_job"
    )
cursor = db_connection.cursor()
query = "SELECT doc_id, detail FROM cpws limit 10"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    doc_id = row[0]
    qw_content = row[1]

# 我目前是需要中国裁判文书网，陕西省西安市2024年盗窃犯罪的一审刑事判决书，要提取案发时间（日期），地点，犯罪人年龄，就业情况，籍贯，受教育水平，家庭情况
    tree = etree.HTML(qw_content)
    qwContents = tree.xpath('//div')
    for qwContent in qwContents:
        text = qwContent.text
        # print(text)
        ts = text.split('\n')
        for t in ts:
            if str(t).startswith("被告人"):
                # print(t)
                birth_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日)', t)
                # 案发时间（日期）
                case_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日因)', t)
                # 户籍地
                residence_registration = re.search(r"户籍地([^\，]+)", t)
                # 受教育水平
                edu_ = re.search(r"([^\，]+文化|文盲[^\，]+肄业)", t)
                location = ""
                if birth_date:
                    birth_date = str(birth_date.group(0))
                    # print(f"提取的出生日期是: {birth_date.group(0)}")
                if case_date:
                    case_date = str(case_date.group(0))
                    # print(f"提取的案发时间是: {case_date.group(0)}")
                if residence_registration:
                    residence_registration = str(residence_registration.group(0))
                    # print(f"提取的户籍地是: {residence_registration.group(0)}")
                if edu_:
                    edu_ = str(edu_.group(0))
                    # print(f"提取的受教育水平是: {edu_.group(0)}")
                sql = """
                                    UPDATE cpws
                                    SET birthday = %s, case_date = %s, residence_registration = %s, edu = %s, case_place = %s, location = %s
                                    WHERE doc_id = %s
                                """
                try:
                    cursor.execute(sql,
                                   (birth_date, case_date, residence_registration, edu_, location, location, doc_id))
                    db_connection.commit()
                except Exception as e:
                    print(f"Error updating row: {e.args}")
            # if str(t).__contains__("来到"):
            #     location = re.search(r'来到(.*?)，', t)
            #     if location:
            #         location = str(location.group(0))
            #         # print(f"提取的作案地点: {location.group(0)}")

            break
    print("\n")
    #     match = re.search(r'被告人.*', text)
    #     if match:
    #         print(f"提取的有用内容是: {match.group(0)}")
    # print("\n")
    #     # 使用正则表达式提取出生日期
    #     birth_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日)出生', text)
    #
    #     if birth_date:
    #         print(f"提取的出生日期是: {birth_date.group(0)}")
    # print("\n")