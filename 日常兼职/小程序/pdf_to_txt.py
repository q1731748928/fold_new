from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# 设置 Tesseract 的路径，如果你使用的是 Windows 系统，可能需要手动设置 tesseract 路径
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# PDF 文件路径
pdf_file = "/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/2.pdf"

# 将 PDF 转换为图片
images = convert_from_path(pdf_file)

# 遍历每一页的图像，使用 OCR 提取文字
for page_num, image in enumerate(images):
    # 进行 OCR 识别
    text = pytesseract.image_to_string(image, lang='chi_sim')
    # 将提取的文本写入到 txt 文件
    with open("output.txt", "a", encoding="utf-8") as txt_file:
        txt_file.write(text)
