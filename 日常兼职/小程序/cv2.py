# -*- coding:UTF-8 -*-

import cv2
import numpy as np
import random
import os


# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


# 读取视频文件

j = 0
videoCapture = cv2.VideoCapture("/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/小程序/题库2/2.mp4")
# videoCapture=cv2.VideoCapture(1)
# 读帧
success, frame = videoCapture.read()

timeF = 360  # 按需更改
i = 0
while success:
    i = i + 1
    if (i % timeF == 0):
        s = 10000
        j = j + 1
        s += j
        save_image(frame, '/Users/hejie/PycharmProjects/turing_exec/日常兼职/小程序/小程序/题库2/cv2img', s)
        # print('save image:',i)
    success, frame = videoCapture.read()
