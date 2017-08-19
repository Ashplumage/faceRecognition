#-*-coding:utf-8 -*-
import  cv2

def facedetect(windowname,camera_id):
#命名和打开摄像头，详情见上一篇
    cv2.namedWindow(windowname)

    cap=cv2.VideoCapture(camera_id)

    classfier=cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')#加载分类器，分类器位置可以自行更改


    color=(0,225,0)#人脸框的颜色，采用rgb模型，这里表示g取255，为绿色框

    while cap.isOpened():
        ok,frame=cap.read()
        if not ok:
            break

        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#图像灰度化

        faceRects=classfier.detectMultiScale(grey,scaleFactor=1.2,minNeighbors=3,minSize=(30,30))#利用分类器检测灰度图像中的人脸矩阵数，1.2和2分别为图片缩放比例和需要检测的有效点数

        if len(faceRects)>0:#大于0则检测到人脸
            for faceRect in faceRects:#单独框出每一张人脸
                x,y,w,h=faceRect#获取框的左上的坐标，框的长宽

                cv2.rectangle(frame,(x-10,y-10),(x+w-10,y+h-10),color,2)

        cv2.imshow(windowname,frame)#显示图像

        c=cv2.waitKey(10)
        if c&0xFF==ord('q'):#退出条件
            break

    cap.release()#释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':#主程序
    print ('face detecting... ')
    facedetect('facedetect',0)