from datetime import datetime

# 输入日期字符串
date_str = '2016-7-30'

# 将字符串转换为 datetime 对象
date_obj = datetime.strptime(date_str, '%Y-%m-%d')

# 将 datetime 对象格式化为带零填充的字符串
formatted_date = date_obj.strftime('%Y-%m-%d')

print(formatted_date)  # 输出：2016-07-30