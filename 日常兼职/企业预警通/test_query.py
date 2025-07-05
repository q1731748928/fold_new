import pymysql

# 连接到 MySQL 数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='qyyjt')

# 创建游标对象
cursor = conn.cursor()
def query(company_name):
    # 查询特定字段
    cursor.execute("SELECT main_rating,all_creditors_right,continuous_creditors_right FROM qyyjt WHERE company_name = %s", (company_name,))

    # 获取查询结果
    result = cursor.fetchone()

    if result:
        print(f"查询结果: main_rating: {result[0]}, all_creditors_right: {result[1]}, continuous_creditors_right: {result[2]}")
        return result
    else:
        print("未找到匹配的记录。")
    # 关闭数据库连接
    conn.close()


print(query('abc'))