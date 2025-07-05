import os
import re
from docx import Document

def replace_text_in_docx(file_path):
    # 打开文档
    doc = Document(file_path)

    # 定义正则表达式，匹配类似 "考生答案 D X 正确答案 B 分数 0/1分" 的文本
    pattern = re.compile(r'考生答案\s+正确答案\s+分数')

    # 遍历文档中的每一段
    for para in doc.paragraphs:
        # 遍历段落中的每一个run（即文本片段）
        for run in para.runs:
            # 使用正则表达式查找并替换符合模式的文本
            print(f'修改前的文字:{run.text}')
            run.text = pattern.sub("", run.text)
            print(f'修改后的文字:{run.text}')

    # 获取文件路径
    folder_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # 设置保存路径
    new_file_path = os.path.join(folder_path, 'modified_' + file_name)

    # 保存修改后的文档
    # doc.save(new_file_path)
    # print(f"文件已保存为: {new_file_path}")

# 调用函数，传入文档路径
replace_text_in_docx('/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/设备安装施工员 - 建工学堂.docx')
