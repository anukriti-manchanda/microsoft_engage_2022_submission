#CAP_DSHOW is required as an argument in cv2.VideoCapture if you are using windows
from cv2 import CAP_DSHOW
from django.shortcuts import redirect, render
import cv2
import dlib
import numpy as np
from imutils import face_utils
import winsound
import geocoder
from datetime import datetime
from django.shortcuts import render
from .models import *
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
           

# Create your views here.

#View for login.html
def login(request):
    if request.method=='POST':
        carNumber=request.POST['carNumber']  
        phoneNumber=str(request.POST['phoneNumber'])
        ins=loginDetails(carNumber=carNumber, phoneNumber=phoneNumber)
        ins.save()
        print("The data has been writen to the database")
        return redirect('getStarted')
    return render(request,'login.html')

#View for about.html
def about(request):
    return render(request,'about.html')

#View for creator.html
def creator(request):
    return render(request,'creator.html')

#View for index.html
def index(request):
    return render(request,'index.html')


#View for /getStarted-main drowsiness detection code
global cam
global latlang
global city
global state
global country
global time
@gzip.gzip_page
def getStarted(request):
    class VideoCamera(object):
        def __init__(self):
            self.video = cv2.VideoCapture(0,CAP_DSHOW)
            (self.grabbed, self.frame) = self.video.read()
            threading.Thread(target=self.update, args=()).start()

        def delete(self):
            self.video.release()

        def get_frame(self):
            image = self.frame
            return image

        def update(self):
            while True:
                (self.grabbed, self.frame) = self.video.read()

    #Storing Face detector in detector
    detector=dlib.get_frontal_face_detector()

    #predictor that will help up detect our face and locate the 68 landmarks on our face 
    predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    #Numpy's linear algebra model calculates the euclidean distance between two points. If (x1,y1) and (x2,y2) are two points
    #euclidean distance ie equal to [(x2-x1)^2+(y2-y1)^2]^1/2
    def compute(ptA,ptB):
        dist=np.linalg.norm(ptA-ptB)
        return dist

    #Function that detects blinking of the eye

    #6 points are detected on each eye out of 68 points and after computing the distances between them when the eyes are open(up)
    #and when the eyes are closed(down), a ratio is calculated. 
    def blinked(a,b,c,d,e,f):
        up=compute(b,d)+compute(c,e)
        down=compute(a,f)
        ratio=up/(2.0*down)

        #comparing ratio to 0.25(ratio>0.25->eye always open) for drowsiness because this value of the ratio is chosen according 
        #to researches 
        if ratio>0.25:
            return 2
        elif(ratio>0.21 and ratio==0.25):
            return 1
        else:
            return 0
    def gen(camera):
        global sleep
        sleep=0
        global drowsy
        drowsy=0
        global active
        active=0
        global status
        status=''
        global color
        color=(0,0,0)
        flag = False
        while not flag:

            #live feed is captured in frames
            frame = camera.get_frame()

            #Color conversion that shows a colored live feed and not black and white(gray)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #faces->for each instance our detector generates multiple rectangles around our face so we put a loop for each rectangle
            faces = detector(gray)

            #detected face in faces array
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()

                landmarks = predictor(gray, face)

                #shaping our result stored in landmarks into numpy array
                landmarks = face_utils.shape_to_np(landmarks)

                #The numbers are actually the landmarks which will show eye
                #The points were picked from the image of 68 landmark detection(image in the folder)
                left_blink = blinked(landmarks[36],landmarks[37], 
                    landmarks[38], landmarks[41], landmarks[40], landmarks[39])
                right_blink = blinked(landmarks[42],landmarks[43], 
                    landmarks[44], landmarks[47], landmarks[46], landmarks[45])

                #Now judge what to do for the eye blinks

                #our counters for sleep, drowsy, active keep increasing by 1 which implies that it neglects
                #normal blinking and does not continuously keep flickering with every new frame

                #if our expression remains constant for more than 6 frames only then will it show a result on the frame on web page
                if(left_blink==0 or right_blink==0):
                    sleep=sleep+1
                    drowsy=0
                    active=0
                    if(sleep>6):
                        status="Drowsy!"
                        color = (255,0,0)

                elif(left_blink==1 or right_blink==1):
                    sleep=0
                    active=0
                    drowsy=drowsy+1
                    if(drowsy>6):
                        status="Little Drowsy!"
                        color = (0,0,255)

                else:
                    drowsy=0
                    sleep=0
                    active=active+1
                    if(active>6):
                        status="Active :)"
                        color = (0,255,0)

                #Putting text on the frame
                cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

                #if status is drowsy get location from the ip address and time from datetime module and breaks the loop
                if status=='Drowsy!':
                    g=geocoder.ip('me')
                    latlong=str(g.latlng)
                    city=str(g.city)
                    state=str(g.state)
                    country=str(g.country)
                    time=str(datetime.now().time())
                    flag = True
                    break

            #After the loop breaks give a beep sound and stop the webcam
            #store the data in the database
            if flag==True:
                frequency=2500
                duration=1000
                winsound.Beep(frequency,duration)
                VideoCamera.delete(camera)
                data=location(latlong=latlong,city=city, state=state, country=country,time=time)
                data.save()
                return redirect('dashboard')

            #livestreaming our webcam footage on the server
            else:   

                _, jpeg = cv2.imencode('.jpg', frame)
                frame=jpeg.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass


#View for dashboard.html
def dashboard(request):
    locationdata = location.objects.all() 
    return render(request,"dashboard.html",{'location':locationdata})

        



