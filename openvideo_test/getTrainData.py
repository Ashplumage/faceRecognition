#-*- coding: utf-8 -*-
import cv2

def getTrainData(windowname,camera_id,path_name,max_num):
    cv2.namedWindow(windowname)#path_name即为指定目录，max_num为你需要捕捉的图片数量

    cap=cv2.VideoCapture(camera_id)#这里的代码都很熟悉，打开摄像头，加载分类器等等

    classifier=cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')

    color=(0,255,0)

    num=0#记录图片数量

    while cap.isOpened():
        ok,frame=cap.read()
        if not ok:
            break

        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#灰度化

        faceRects = classifier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

        if len(faceRects)>0:
            for faceRect in faceRects:
                x,y,w,h=faceRect
                image_name='%s%d.jpg' % (path_name,num)#这里为每个捕捉到的图片进行命名，每个图片按数字递增命名。
                image=frame[y:y+h,x:x+w]#将当前帧含人脸部分保存为图片
                cv2.imwrite(image_name,image)

                num+=1
                if num>max_num:#如果超过指定最大保存数量退出循环
                    break

                cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)#画出矩形框
                font=cv2.FONT_HERSHEY_SIMPLEX#获取内置字体
                cv2.putText(frame,('%d'%num),(x+30,y+30),font,1,(255,0,255),4)#调用函数，对人脸坐标位置，添加一个(x+30,y+30）的矩形框用于显示当前捕捉到了多少人脸图片

        if num>max_num:
            break

        cv2.imshow(windowname,frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    cap.release()#释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()

#主函数
if __name__ =='__main__':
    print ('catching your face and writting into disk...')
    getTrainData('getTrainData',0,'../traindata/',1000)
