# 选项数据
options = [
    {'oid': 228475700, 'title': '对', 'param': '[]'},
    {'oid': 228475701, 'title': '错', 'param': '[]'}
]

# 正确答案的 oid 列表
rightoids = [228475700]  # 假设 228475700 是正确答案

# 打印题目选项，并为每个选项分配字母 A, B, C...
print("题目是: 请从以下选项中选择正确答案：")
for index, option in enumerate(options):
    option_label = chr(65 + index)  # 65 是字母 'A' 的 ASCII 码
    print(f'{option_label}. {option["title"]}')

# 查找并输出正确答案
for index, option in enumerate(options):
    oid = option['oid']
    title = option['title']
    if oid in rightoids:  # 如果当前 oid 是正确答案之一
        option_label = chr(65 + index)  # 获取对应的字母
        print(f"正确答案是: {option_label}. {title}")
