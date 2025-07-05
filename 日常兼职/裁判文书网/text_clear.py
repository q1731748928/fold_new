# coding=utf-8
import pymysql
from lxml import etree
import re



def update_batch_data(db_connection, batch_data):
    cursor = db_connection.cursor()
    sql = """
            UPDATE cpws
            SET birthday = %s, case_date = %s, residence_registration = %s, edu = %s, location = %s
            WHERE doc_id = %s
    """
    try:
        cursor.executemany(sql, batch_data)
        db_connection.commit()
        print(f"更新 {len(batch_data)} 行数据。")
    except Exception as e:
        print(f"更新批次数据时出错: {e.args}")
        db_connection.rollback()
    finally:
        cursor.close()

db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="part_time_job"
)
cursor = db_connection.cursor()
query = "SELECT doc_id, detail FROM cpws"
cursor.execute(query)
results = cursor.fetchall()

batch_data = []
for row in results:
    doc_id = row[0]
    qw_content = row[1]
    # 我目前是需要中国裁判文书网，陕西省西安市2024年盗窃犯罪的一审刑事判决书，要提取案发时间（日期），地点，犯罪人年龄，就业情况，籍贯，受教育水平，家庭情况
    tree = etree.HTML(qw_content)
    qwContents = tree.xpath('//div')
    for qwContent in qwContents:
        text = qwContent.text
        print(text)
        job_status = re.search(r"([^\，]+业)",text)
        if job_status:
            print(f"extracted job status: {job_status.group(0)}")
            job_status = str(job_status.group(0))
            sql = """
                                               UPDATE cpws
                                               SET job_status = %s
                                               WHERE doc_id = %s
                                          """
            cursor.execute(sql, (str(job_status), doc_id))
            db_connection.commit()
        # 案发时间（日期）
        # case_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日因)', text)
        # if case_date:
        #     # print(f"提取的案发时间是: {case_date.group(0)}")
        #     case_date = str(case_date.group(0))
        #     sql = """
        #                            UPDATE cpws
        #                            SET case_date = %s
        #                            WHERE doc_id = %s
        #                       """
        #     cursor.execute(sql, (str(case_date), doc_id))
        #     db_connection.commit()
        #     break
        # print(text)
        # # 案发时间（日期）
        case_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日因)', text)
        # if case_date:
        #     case_date = str(case_date.group(0))
        #     sql = """
        #                            UPDATE cpws
        #                            SET location = %s
        #                            WHERE doc_id = %s
        #     """
        #     cursor.execute(sql, (str(case_date), doc_id))
        #     db_connection.commit()
            # print(f"提取的案发时间是: {case_date.group(0)}")
        # location = re.search(r'到(.*?)，', text)
        # if location:
        #     print(f"提取的作案地点: {location.group(0)}")
        #     location = str(location.group(0))
        #     sql = """
        #                UPDATE cpws
        #                SET location = %s
        #                WHERE doc_id = %s
        #           """
        #     cursor.execute(sql, (str(location), doc_id))
        #     db_connection.commit()
        #     break
        # birth_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日出生)', text)
        # birthday = ""
        # residence_registration = ""
        # edu_ = ""
        # if birth_date:
        #     print(f"提取的出生日期是: {birth_date.group(0)}")
        #     birthday = str(birth_date.group(0))
        #     sql = """
        #             UPDATE cpws
        #             SET birthday = %s
        #             WHERE doc_id = %s
        #             """
        #     cursor.execute(sql,(birthday,doc_id))
        #     db_connection.commit()
        # residence_registration = re.search(r"户籍地([^\，]+)", text)
        # if residence_registration:
        #     print(f"提取的户籍地是: {residence_registration.group(0)}")
        #     residence_registration = str(residence_registration.group(0))
        #     sql = """
        #                         UPDATE cpws
        #                         SET residence_registration = %s
        #                         WHERE doc_id = %s
        #                         """
        #     cursor.execute(sql, (residence_registration, doc_id))
        #     db_connection.commit()
#             # # 受教育水平
#         edu_ = re.search(r"([^\，]+文化|文盲[^\，]+肄业)", text)
#         if edu_:
#             print(f"提取的受教育水平是: {edu_.group(0)}")
#             edu_ = str(edu_.group(0))
#             sql = """
#                                             UPDATE cpws
#                                             SET edu = %s
#                                             WHERE doc_id = %s
#                                             """
#             cursor.execute(sql, (edu_, doc_id))
#             db_connection.commit()
#     batch_data.append((birthday, str(list), residence_registration, edu_, str(location_list), doc_id))
# update_batch_data(db_connection, batch_data)
        # sql = """
        #         UPDATE cpws
        #         SET birthday = %s, case_date = %s, residence_registration = %s, edu = %s, location = %s
        #         WHERE doc_id = %s
        #         """
        # try:
        #     cursor.execute(sql,
        #                    (birth_date, str(list), residence_registration, edu_, str(location_list), doc_id))
        #     db_connection.commit()
    #     except Exception as e:
    #         print(f"Error updating row: {e.args}")
    # print('\n')
        # # 案发时间（日期）
        # case_date = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日因)', text)
        # # 户籍地
        # residence_registration = re.search(r"户籍地([^\，]+)", text)
        # # 受教育水平
        # edu_ = re.search(r"([^\，]+文化|文盲[^\，]+肄业)", text)
        # location = ""
        # if birth_date:
        #     print(f"提取的出生日期是: {birth_date.group(0)}")
        #     birth_date = str(birth_date.group(0))
        # if case_date:
        #     case_date = str(case_date.group(0))
        #     # print(f"提取的案发时间是: {case_date.group(0)}")
        # if residence_registration:
        #     residence_registration = str(residence_registration.group(0))
        #     # print(f"提取的户籍地是: {residence_registration.group(0)}")
        # if edu_:
        #     edu_ = str(edu_.group(0))
        #     # print(f"提取的受教育水平是: {edu_.group(0)}")
        # sql = """
        #         UPDATE cpws
        #         SET birthday = %s, case_date = %s, residence_registration = %s, edu = %s, case_place = %s, location = %s
        #         WHERE doc_id = %s
        #                         """
        # try:
        #     cursor.execute(sql,
        #                    (birth_date, case_date, residence_registration, edu_, location, location, doc_id))
        #     db_connection.commit()
        # except Exception as e:
        #     print(f"Error updating row: {e.args}")
    # if str(t).__contains__("来到"):
    #     location = re.search(r'来到(.*?)，', t)
    #     if location:
    #         location = str(location.group(0))
    #         # print(f"提取的作案地点: {location.group(0)}")
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
