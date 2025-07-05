import cv2
import os

def apart(video_path, video_name, image_path, frameFrequency=15):
    """
    功能：将视频拆分成图片
    参数：
        video_path：要拆分的视频路径
        video_name：要拆分的视频名字（不带后缀）
        image_path：拆分后图片的存放路径
        frameFrequency：提取图片的频率（默认每36000帧提取一次）
    """

    # 在这里把后缀接上
    video = os.path.join(video_path, video_name + '.mp4')

    if not os.path.exists(image_path):
        # 如果文件目录不存在则创建目录
        os.makedirs(image_path)

    # 获取视频
    use_video = cv2.VideoCapture(video)

    # 初始化计数器
    count = 0

    # 开始循环抽取图片
    print('Start extracting images!')
    while True:
        res, image = use_video.read()
        count += 1

        # 如果提取完图片，则退出循环
        if not res:
            print('No more frames to extract.')
            break

        # 只在指定频率的帧上提取图片
        if count % frameFrequency == 0:
            # 将图片写入文件夹中
            cv2.imwrite(image_path + str(count) + '.jpg', image)
            print(f"Extracted frame {count}: {image_path + str(count) + '.jpg'}")

    print('End of image extraction!')
    use_video.release()

if __name__ == '__main__':
    video_path = '/日常兼职/小程序/小程序/题库2'
    video_name = '2'
    image_path = '/日常兼职/小程序/小程序/题库2/cv2img/'
    apart(video_path, video_name, image_path, frameFrequency=15)
