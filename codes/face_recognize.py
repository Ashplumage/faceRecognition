#-*- coding:utf-8 -*-
import cv2
from trainByKeras import Model

CAMERA_ID=0

if __name__ == '__main__':
    model=Model()
    model.load_model(file_path='./face.model.h5')

    color = (0,255,0)
    cap=cv2.VideoCapture(CAMERA_ID)

    cassade_path='/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml'

    while True:
        ok,frame=cap.read()

        frame_grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cassade=cv2.CascadeClassifier(cassade_path)

        faceRects=cassade.detectMultiScale(frame_grey,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
        if len(faceRects)>0:
            for faceRect in faceRects:
                x,y,w,h=faceRect
                image=frame[y:y+h,x:x+w]
                faceId=model.face_predict(image)

                if faceId==0:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

                    cv2.putText(frame,'your grace',
                                (x+30,y+30),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (255,0,255),
                                2)
                else:
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    #
                    # cv2.putText(frame, '',
                    #             (x + 30, y + 30),
                    #             cv2.FONT_HERSHEY_SIMPLEX,
                    #             1,
                    #             (255, 0, 255),
                    #             2)

                    pass

        cv2.imshow('识别朕',frame)
        k=cv2.waitKey(10)
        if k& 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()