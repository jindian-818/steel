# 对图片进行base64编码，解码，解码为numpy，opencv，matplot照片
# USAGE
# python base64_2_jpg.py

import base64

import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt


# 将字符串写入文字
#  name 图片名
#  base64_data 图片二进制编码后string流
def write2txt(name, base64_data):
    # 写入_base64.txt
    print(name)
    print(name,len(base64_data))
    basef = open('./img/'+name + '_base64.txt', 'w')
    data = 'data:image/jpg;base64,%s' % base64_data
    # print(data)
    basef.write(base64_data)
    basef.close()


# 编码图像为base64字符串
def encode_base64(file):
    with open(file, 'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        print(type(base64_data))
        # print(base64_data)
        # 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64,
        base64_str = str(base64_data, 'utf-8')
        # print(base64_str)
        print(len(base64_data))
        #write2txt(file.replace(".jpg", ""), base64_str)
        return base64_data


# 解码base64字符串为图像，并保存
def decode_base64(base64_data):
    with open('./img/base64.jpg', 'wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)
    return './img/base64.jpg'


# 解码base64字符串为numpy图像、opencv、matplot图像

# 解码base64字符串为numpy图像
def decode_base64_np_img(base64_data):
    img = base64.b64decode(base64_data)
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    print('numpy: ', img_array.shape)
    cv2.imshow("img", img_array)
    cv2.waitKey(0)


# 解码base64字符串为opencv图像
def decode_base64_cv_img(base64_data):
    img = base64.b64decode(base64_data)
    write2txt("reseive", str(img))
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    img_raw = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式BGR
    #img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)  # 转换灰度图

    print('opencv bgr: ', img_raw.shape)
    #print('opencv gray: ', img_gray.shape)

    cv2.imshow("img bgr", img_raw)
    #cv2.imshow("img gray", img_gray)
    cv2.waitKey(0)
    


# 解码base64字符串为matplot图像
def decode_base64_matplot_img(base64_data):
    img = base64.b64decode(base64_data)
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    img_raw = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式BGR
    img_matplot = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)  # BGR转RGB

    img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)  # 转换灰度图
    imggray_matplot = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)  # 灰度图转RGB
    plt.figure()
    plt.title("Matplot RGB Origin Image")
    plt.axis("off")
    plt.imshow(img_matplot)

    plt.figure()
    plt.title("Matplot Gray Origin Image")
    plt.axis("off")
    plt.imshow(imggray_matplot)
    plt.show()

def pic_compress(base64_data, out_path, target_size=199, quality=90, step=5, pic_type='.jpg'):
    pic_byte = base64.b64decode(base64_data)
    img_np = np.fromstring(pic_byte, np.uint8)  # 转换np序列
    img_cv = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    print(img_cv.shape)
    if (img_cv.shape[1] > 1000):
        img_cv = imutils.resize(img_cv, width=1000)
    print(img_cv.shape)

    current_size = len(pic_byte) / 1024
    print("图片压缩前的大小为(KB)：", current_size)
    while current_size > target_size:
        retval, pic_byte = cv2.imencode(pic_type, img_cv, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        # retval, buffer = cv2.imencode('.jpg', pic_img)
        pic_str = base64.b64encode(pic_byte)
        pic_str = pic_str.decode()
        if quality - step < 0:
            break
        quality -= step
        current_size = len(pic_byte) / 1024

    # 保存图片
    # with open(out_path, 'wb') as f:
    #     f.write(BytesIO(pic_byte).getvalue())

    print(len(pic_byte) / 1024)
    # print(pic_str)
    # return pic_byte
    return (len(pic_byte) / 1024, pic_str)

if __name__ == '__main__':
    img_path = './images/1622175322109_0.025711.jpg'
    base64_data = encode_base64(img_path)
    decode_base64(base64_data)

    decode_base64_np_img(base64_data)
    decode_base64_cv_img(base64_data)
    decode_base64_matplot_img(base64_data)

    (pic_size, pic) = pic_compress(base64_data, 'new_test.jpg', target_size=100)
    print("图片压缩后的大小为(KB)：", pic_size)
    print(pic)
