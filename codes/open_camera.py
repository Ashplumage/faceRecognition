#-*- coding:utf-8 -*-

import cv2    #引入cv2，也就是引入opencv的一些包和处理类，不然下面的一些操作都无法完成

#打开摄像头的方法，window_name为显示窗口名，video_id为你设备摄像头的id，默认为0，如果引用usb可能会改变为1，等
def openvideo(window_name ,video_id):
    cv2.namedWindow(window_name)

    cap=cv2.VideoCapture(video_id)#获取摄像头
    while cap.isOpened():
        ok,frame=cap.read()#ok表示摄像头读取状态，frame表示摄像头读取的图像矩阵mat类型
        if not ok :
            break

        cv2.imshow(window_name,frame)#将图像矩阵显示在一个窗口中
        c=cv2.waitKey(10)#10ms一帧
        if c & 0xFF==ord('q'):#按键q退出
            break

#释放资源
    cap.release()
    cv2.destroyWindow(window_name)

#主程序调用方法运行
if __name__ == '__main__':
    print ('open camera...')
    openvideo('openvideo' ,0)