from docx import Document

# 加载文档
doc = Document("项目名称.docx")

# 提取文档中的文本
text = []
for para in doc.paragraphs:
    text.append(para.text)

# 将提取的文本合并成一个字符串
document_text = "\n".join(text)

# 打印或保存提取的文本
string = document_text
str = string.split("\n\n")
for s in str:
    s = s.replace("\n","").replace("请上传完整版伦理审批文件。 ","").strip()
    print(s)