import cv2 

#Get cascadeClassifier.
face_cascade=cv2.CascadeClassifier("/home/odiwuor/Documents/opencv4.0.5/new/customized/path/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")
#Capture frame from wencam.
cap=cv2.VideoCapture(0)

#Continously capture  more than one frame.
while True:
    check,frame=cap.read()
    if check==True:
        frame=cv2.resize(frame,(800,600))
        
        #Convert frame into grayScale image.
        grayImage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        detect_faces=face_cascade.detectMultiScale(image=grayImage,scaleFactor=1.2,minNeighbors=4)
        for (x,y,w,h) in detect_faces:
            print("x",x)
            print("y",y)
            print("width",w)
            print("height",h)
            cv2.imshow("FaceDetection",frame)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break

cap.release()
cap.destroyAllWindows()

        