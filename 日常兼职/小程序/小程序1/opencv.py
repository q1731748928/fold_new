import cv2

video = cv2.VideoCapture("题库2/2.mp4")  # 获取一个视频来打开
isOpened = video.isOpened  # 判断这个视频是否可以正常打开
print(isOpened)

fps = video.get(cv2.CAP_PROP_FPS)  # 读取这个视频的帧率
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频的宽度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频的高度

print(fps, width, height)  # 查看帧率 宽高

i = 0

while isOpened:
    if i == 10:
        break
    else:
        i += 1

    (flag, frame) = video.read()  # 读取每一张图片  flag 表明是否都区成功， frame表示图片的内容
    fileName = "image" + str(i) + ".jpg"
    print(fileName)

    if flag == True:
        print("./pic/" + fileName)
        cv2.imwrite("D:\\pythonProject\\turing_exec\\日常兼职\\小程序\\题库2\\pic" + fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

print("end!")



