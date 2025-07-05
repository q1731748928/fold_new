import os
import re
from docx import Document


def open_docx(file_path):
    # 打开文档
    doc = Document(file_path)

    # 遍历文档中的每一段（每一行）
    for para in doc.paragraphs:
        # 打印每一段的文本内容
        print(para.text)
        with open("./doc.txt","a+") as f:
            f.write(str(para.text) + "\n")
        # 遍历段落中的每一个run（即文本片段）
        # 使用正则表达式查找并替换符合模式的文本
        # print(f'修改前的文本:{para.text}')
        # para.text = pattern.sub("", para.text)
        # print(f'修改后的文本:{para.text}')
        # for run in para.runs:
        #

    # 获取文件路径
    folder_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # 设置保存路径
    new_file_path = os.path.join(folder_path, 'modified_' + file_name)

    # 保存修改后的文档
    # doc.save(new_file_path)
    # print(f"文件已保存为: {new_file_path}")


open_docx('/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/设备安装施工员 - 建工学堂.docx')
