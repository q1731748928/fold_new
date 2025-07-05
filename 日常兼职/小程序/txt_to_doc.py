import os
import re
from docx import Document

# 初始化Word文档
document = Document()

# 设定路径和文件名排序逻辑
path = '/日常兼职/小程序/小程序/题库2/图片文本'

# 获取文件夹中所有的 .txt 文件
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]

# 自定义排序函数，提取文件名中的数字进行排序
def extract_number(filename):
    match = re.search(r'(\d+)', filename)  # 提取文件名中的数字部分
    return int(match.group(1)) if match else float('inf')  # 如果没有找到数字，则将其视为最大值

# 按照文件名中的数字进行排序
txt_files_sorted = sorted(txt_files, key=extract_number)

NUM_MIN = 0  # 自定义最小值
NUM_MAX = 100  # 自定义最大值

# 遍历排序后的txt文件列表
for txt_file in txt_files_sorted:
    # 构建完整的文件路径
    txt_file_path = os.path.join(path, txt_file)

    # 打开并读取每个.txt文件
    with open(txt_file_path, 'r', encoding='utf-8') as rf:
        num, add = 0, 0
        for line in rf:
            num += 1
            line = line.strip()
            # 如果行号在指定范围内，添加到Word文档中
            if NUM_MIN < num <= NUM_MAX:
                add += 1
                document.add_paragraph(line)
            # 如果行号超出最大值，跳出循环
            elif num > NUM_MAX:
                break

# 保存最终的Word文档
output_file = os.path.join(path, str(NUM_MAX) + "_图片文本题库2.docx")
document.save(output_file)

print(f"Word文档已保存为: {output_file}")
