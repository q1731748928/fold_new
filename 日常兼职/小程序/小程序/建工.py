import pytesseract
from PIL import Image
import os

# 图片文件夹路径
image_folder = '/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/小程序/题库2/cv2img'

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 遍历每一张图片
for image_file in image_files:
    # 读取图像
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)

    # 图片中文本识别
    text = pytesseract.image_to_string(image, lang='chi_sim')

    # 创建保存文本的文件名
    text_filename = os.path.splitext(image_file)[0] + '.txt'

    # 保存文本到txt文件
    with open(f'./题库2/图片文本/{text_filename}', 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'{image_file} 的文本已保存到 {text_filename}')
