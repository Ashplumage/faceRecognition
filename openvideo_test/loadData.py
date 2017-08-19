# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2

IMAGE_SIZE = 64


# 按照指定图像大小调整尺寸
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)

    # 获取图像尺寸
    h, w, _ = image.shape

    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)

    # 计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass

        # RGB颜色
    BLACK = [0, 0, 0]

    # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

    # 调整图像大小并返回
    return cv2.resize(constant, (height, width))


# 读取训练数据i
images = []
labels = []

def file_exit(path_name,son_path_name):#判断path_name文件夹下是否有file_name
    lists = os.listdir(path_name)#该目录下的所有文件夹
    for list in lists:#遍历所有文件，如果存在与son_path_name同名的文件夹，返回1即找到测试集文件
        if list == son_path_name:
            print ('file exits')
            return 1
    return 0


def read_path(path_name,son_path_name):#读取路径下的数据集，并为每张图片添加一个类别标签
    parent_path = os.path.abspath(os.path.join(path_name, '..'))
    exit_code=file_exit(parent_path,son_path_name)#判断该路径下是否有测试集目录

    if exit_code == 1:#如果有，则全路径是当前路径上一级＋测试集文件夹名
        fullpath = parent_path +'/'+ son_path_name

        for dir_item in os.listdir(fullpath):#遍历所有的图片

            if dir_item.endswith('.jpg'):#如果格式是图片，则进行大小处理
                image = cv2.imread(fullpath+'/'+dir_item)
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)

                # cv2.imwrite('test.jpg', image)

                images.append(image)
                labels.append(son_path_name)
    print labels
    return images, labels


# 从指定路径读取训练数据，path_name是当前文件所在路径，son_path_name是需要寻找的存放测试数据的子目录名
def load_dataset(path_name,son_path_name):
    images, labels = read_path(path_name,son_path_name)#读取子目录下的所有测试数据集

    # 将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3)
    # IMAGE_SIZE为64，故对我来说尺寸为1200 * 64 * 64 * 3
    # 图片为64 * 64像素,一个像素3个颜色值(RGB)
    images = np.array(images)
    print(images.shape)

    # 标注数据，'traindata'文件夹下都是训练集的脸部图像，全部指定为0，另外一个文件夹下是测试集的，全部指定为1
    labels = np.array([0 if label==('traindata') else 1 for label in labels])
    print labels
    return images, labels


if __name__ == '__main__':
    path_name=os.getcwd()#getcwd()获取当前.py文件所在目录，加载与此目录所在路径上一级的traindata文件夹下的所有训练文件
    images, labels = load_dataset(path_name,'testdata')
    print images,labels
