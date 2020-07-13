import tensorflow as tf
oldinit = tf.Session.__init__
def new_tfinit(session, target='', graph=None, config=None):
    print("Set config.gpu_options.allow_growth to True")
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    oldinit(session, target, graph, config)
tf.Session.__init__ = new_tfinit
import face_recognition
import cv2
from PIL import Image
import numpy as np
from io import BytesIO
import sys
import argparse
import cv2
import time
import os
# import ast
from collections import OrderedDict
from datetime import datetime, timedelta
# from faces import FaceDetector
# from data import FaceData
# from gabor import GaborBank
# from emotions import EmotionsDetector

# from http.server import BaseHTTPRequestHandler, HTTPServer

import threading
import queue
import random
from flask import Flask , jsonify,render_template
import pymysql
import base64
# import keyboard as kb
import traceback

import dlib

# from mtcnn import MTCNN
# detector = MTCNN(min_face_size=65)

import os
import sys
import cv2
# from time import time, sleep
from queue import Queue
from collections import namedtuple

sys.path.append('../godofeye/lib')
sys.path.append('../godofeye/lib/yoloface')

from blueeyes.face_recognition import FaceDetector, FaceRecognition
from blueeyes.utils import Camera

# cap = Camera(source='/home/huy/Downloads/AnhDuy.mp4', frameskip=5)
video = Camera(source='rtsp://admin:be123456@10.10.46.224:554/Streaming/Channels/101', frameskip=0)
# cap = Camera(source='rtsp://admin:be123456@10.10.46.224:554/Streaming/Channels/101', frameskip=5)

# video = cv2.VideoCapture('rtsp://admin:be123456@10.10.46.224:554/Streaming/Channels/101')

# cap = Camera(source=0, frameskip=15)
# cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
# cap = cv2.VideoCapture('/home/huy/Downloads/dataV13_group.avi')
# cap.set(cv2.CAP_PROP_FPS, 10)

video.start()

# Configurations
FRAME_COUNT_TO_DECIDE = 5

HOME = os.environ['HOME']
# detector = FaceDetector('mtcnn', min_face_size=60)
detector = FaceDetector('yolo', model_img_size=(416,416))
# detector = YOLO()
recog = FaceRecognition(
    # model_dir='/home/huy/code/godofeye/models', 
    model_dir=f'{HOME}/Downloads',
    vggface=False,
    use_knn=True
    # retrain=False
)

def process_id(result_id):
    name = result_id[0]
    print(result_id)

recog.on_final_decision(process_id)

execution_time = {}

# if not video.cap.isOpened():
#     print('Error in opening camera')

app = Flask(__name__)

database = pymysql.connect(host='localhost',
                           user='be',
                           password='blueeyes',
                           autocommit = True

                           )

print("Connecting to the Camera")
# Waiting for the camera to open
while True:
    __ret, __frame = video.read()
    if __ret == False:
        print('...............')
        video = Camera(source='rtsp://admin:be123456@10.10.46.224:554/Streaming/Channels/101', frameskip=0)
        time.sleep(1)
    else:
        break

#### NEW #####
FRAME_WIDTH = int(video.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_HEIGHT = int(video.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FPS = int(video.cap.get(cv2.CAP_PROP_FPS))
FPS = 25

#---------------------------------------------
def splitname(str_):
    str_1 = list(str_)
    result = str_1[0].upper()
    for i in range(1,len(str_1)):
        if str_1[i].isupper():

            result+=" "+str_1[i]
        else:
            result+=str_1[i]
    return result

# name = queue.Queue(maxsize=1)
name = ""

def main(argv,dem_nhac=0):
    global video
    global database
    def distance_cal(f,h,p):
        return f*h/p
    button = 0
    def button_():
        nonlocal button
        button = int(input("Would you like input (1/0) :"))
    
    """
    Main entry of this script.

    Parameters
    ------
    argv: list of str
        Arguments received from the command line.
    """
#    global name
    name = ""
    bien=0

    Q = []
    x = "image_css"
    allfiles = os.listdir(x) # doc folder image_css
    dem_x = 0
    list_image_css = []
    list_names = []
    for i in allfiles :
        dem_x += 1
    for i in range(dem_x) :
        n=0
        try:
            allfiles_1 = os.listdir ( x + '/' + allfiles[i] )
        except:
            traceback.print_exc()
            continue
        
        
        
        for j in allfiles_1:
            if os.path.exists('variable/'+allfiles[i]+j+'.txt'):
                #print(n)
                fileface = open('variable/'+allfiles[i]+j+'.txt','r+')
                a=fileface.read()
                a= a.replace('  ', ' ')
                a = a.replace('  ',' ')
                a = a.replace('  ',' ')
                a = a.replace(' ',',')
                a = a+'x'
                try:
                    b = eval(a.split("x")[0])
                    list_image_css.append(b)
                    fileface.close()
                    n+=1
                except:
                    traceback.print_exc()
                    pass
                

            elif not os.path.exists('variable/'+allfiles[i]+j+'.txt'):
                a=face_recognition.load_image_file(x+'/'+allfiles[i]+'/'+j)
                try:
                    faces = detector.detect_faces(a)
                    # faces = detector.detect(a)
                    boxes = [face['box'] for face in faces]
                    face_locations_1 = [(y1,x1+w,y1+h,x1) for (x1,y1,w,h) in boxes]
                    b=face_recognition.face_encodings(a,face_locations_1,num_jitters=10)[0]#known_face_locations=[[0,a.shape[1],a.shape[0],0]])[0]#,known_face_locations=[[0,a.shape(1),a.shape(0),0]])
                    fileface = open('variable/'+allfiles[i]+j+'.txt','w+')
                    fileface.write(str(b))
                    fileface.close()
                    list_image_css.append(b)
                    n+=1
                except:
                    traceback.print_exc()
                    pass

        for k in range(n):
            list_names.append(allfiles[i])
    #print(list_image_css)
    rutgon_ = []
    
    for i in list_names:
        if i not in rutgon_:
            rutgon_.append(i)
    read_rutgon_ = open('best/listsv.txt','w+')
    for i in rutgon_:
        read_rutgon_.write("\n"+i)
    read_rutgon_.close()

    read_chuyencan_ = open('best/chuyencan.txt','w+')
    for i in range(len(rutgon_)):
        read_chuyencan_.write("\n"+str(0))
    read_chuyencan_.close()

    sourceName = 'debug info'

    # Force HD resolution (if the video was not recorded in this resolution or
    # if the camera does not support it, the frames will be stretched to fit it)
    # The intention is just to standardize the input (and make the help window
    # work as intended)
    #video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Create the helper class
    # data = VideoData() #// camxuc

    # Text settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    thick = 1
    glow = 3 * thick

    # Color settings
    color = (255, 255, 255)

    paused = False
    frameNum = 0
    k=[]
    # Process the video input
    bien_=0
    #list_names = []
    thuongxuyen_ = 0
    hiendien = 0
    hiendien_ten = []
    vang_ = len(list_names)
    file_vang = []
    bien_dem = 0
    list_buon = [""]
    list_vang_vuaroi = []
    
    list_name_camxuc = []
   
    unknow_count=0
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        
        if not paused:
            start = datetime.now()  
        #if ret:
            #ret, frame = video.read()
        else:
            paused = True

        ret, frame = video.read()

        # small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25,interpolation = cv2.INTER_CUBIC)
        
        # rgb_small_frame = frame[:, :, ::-1]
        rgb_small_frame = frame
        toa_y = 100
        stt = 0
        for i in hiendien_ten:
            stt+=1
            toa_y += 40
        
       if int(str(len(rutgon_)-int(len(hiendien_ten)))) == 0 :
            #print("lop du")
            pass
            #cv2.putText(frame, " Class full " , (30,220), cv2.FONT_HERSHEY_SIMPLEX , 2, (150,50,240),5)
        name_linkfile = str(time.localtime(time.time()).tm_mon)+'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)
        vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'_vang'+'.txt','a+') #write ck
        vang_os.close()
        vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'_vang'+'.txt','r+') #write ck
        for i in rutgon_:
            if i in hiendien_ten:
                continue
            else:
                if i not in list(vang_os.read().split()):
                    file_vang.append(i)
        vang_os.close()

        for i in file_vang:
            try:
                vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'_vang'+'.txt','r+')
                zzz = list(vang_os.read().split())
                vang_os.close()
            except:
                traceback.print_exc()
                continue
            if i not in zzz and i not in hiendien_ten:
                vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'_vang'+'.txt','a+') #write ck
                #if time.localtime(time.time()).tm_min==40:
                    #if time.localtime(time.time()).tm_sec==50:
                vang_os.write("\n"+i)
                vang_os.close()
            else:
                vang_os.close()

        # letiennhat = open('best/ten.txt','w+')
        # letiennhat.write('DUTer')
        # letiennhat.close()
        letiennhat = open('hide_on_push/id.txt','w+')
        letiennhat.write('WELCOME TO')
        letiennhat.close()
        letiennhat = open('hide_on_push/name_id.txt','w+')
        letiennhat.write('WELCOME TO')
        letiennhat.close()
        letiennhat = open('hide_on_push/donvi.txt','w+')
        letiennhat.write('DUT')
        letiennhat.close()
        if os.path.exists('best/input_1.txt'):
            button = 1
        if button == 1:
            try:
                if not os.path.exists('best/input_1.txt'):
                    time.sleep(2)
                else:
                    open_fff = open('best/input_1.txt', 'r+')
                    val_input_2 = open_fff.read()
                    open_fff.close()
                    os.remove('best/input_1.txt')
                    text = val_input_2
            except:
                traceback.print_exc()
                pass

            if 1:
                dem_anh = 0
                while True:
                    while True:
                        if dem_anh > 50:
                            dem_nhac += 1
                            cv2.destroyAllWindows()
                            return main(argv, dem_nhac)  # return
                            break

                        # image_ = image_queue.get()
                        cv2.imshow('add_person', image_)

                        if cv2.waitKey(1) & 0xff == ord('a'):
                            try:
                                if not os.path.exists('image_css/' + text):
                                    os.mkdir('image_css/' + text)

                            except:
                                traceback.print_exc()
                                pass
                            faces = detector.detect_faces(image_)
                            print(faces)
                            
                            #boxes = [face['box'] for face in faces]
                            #face_locations_1 = [(y1,x1+w,y1+h,x1) for (x1,y1,w,h) in boxes]
                            if len(faces)==1 :
                                cv2.imwrite('image_css/' + str(text) + '/' + 'classe' + str(dem_anh) + '.jpg', image_)
                                list_image_css.append('image_css/' + str(text) + '/classe' + str(dem_anh) + '.jpg')
                                dem_anh = dem_anh + 1

                del (video)
        else:
            pass
        if process_this_frame:
            
            # Find all the faces and face encodings in the current frame of video
            # face_locations = face_recognition.face_locations(rgb_small_frame, 2)
            # print(face_locations)
            # print('Processing frame')

            # # using MTCNN Face Detection
            # faces = detector.detect_faces(rgb_small_frame)
            
            # boxes = [face['box'] for face in faces]
            # ### REMOVE ###
            # boxes = [(x,y,w,h) for (x,y,w,h) in boxes if w >= 80//2 and h >= 90//2]
            # bias = 0
            # face_locations = [(y-bias,x+w+bias,y+h+bias,x-bias) for (x,y,w,h) in boxes]
            
            
            
            # face_locations = detector.detect(rgb_small_frame)
            # using Dlib Hog FaceDetecion
            # face_locations = []
            # faceRects = hogFaceDetector(rgb_small_frame, 2)
            # for faceRect in faceRects:
            #     left = faceRect.left()
            #     top = faceRect.top()
            #     right = faceRect.right()
            #     bottom = faceRect.bottom()
            #     face_locations.append([top,right,bottom,left])
            
            # print('face_location: ', face_locations)
            # print(face_locations)
            
            # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations,num_jitters=10)
            # face_names = []
            #start = time.time()
            name_linkfile = str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)
            vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+
                           '.txt/'+name_linkfile+'_vang'+'.txt','a+') #write ck
            vang_os.close()
            vang_os = open('regular_review/hour' + str(time.localtime(time.time()).tm_hour)+
                               '.txt/'+name_linkfile+'_vang'+'.txt','r+') #write ck

                   
#             for face_encoding in face_encodings:
#                 threshold = 0.33828888888465666682982228299
#                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding, threshold)
#                 #elapsed = time.time() - start
#                 #print(elapsed)
#                 # problem : hoc nguoi !
                
#                 if bien_==0:
#                     open_f = open('best/input.txt','w+')
#                     val_input = open_f.write("HELLO MY FRIEND ")
#                     open_f.close()
#                 if True not in matches:
#                     bien_+=1
#                     if bien_>=2:
#                         # if bien_==15:
#                         #     bien_=0
                            
#                         open_f = open('best/input.txt','w+')
#                         val_input = open_f.write("Do you want Input new friend ")
#                         open_f.close()
                        
#                         #cv2.putText(frame,"Hold 'z' : Input your image",(850,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
#                         #if cv2.waitKey(1) & 0xff == ord('z'):
#                             #button=1
# #                        open_ff = open('best/input_1.txt','r+')
# #                        val_input_1 = open_ff.read()
# #                        open_ff.close()
#                         if os.path.exists('best/input_1.txt'):
#                             button=1
#                         if button == 1:
#                             try:
#                                 if not os.path.exists('best/input_1.txt'):
#                                     time.sleep(2)
#                                 else:
#                                     open_fff = open('best/input_1.txt','r+')
#                                     val_input_2 = open_fff.read()
#                                     open_fff.close()
#                                     os.remove('best/input_1.txt')
#                                     text = val_input_2
#                             except:
#                                 traceback.print_exc()
#                                 pass
                            
                            
#                             #text=input("Input(No sign and No space) :")
#                             #while not text.isalpha():
#                                 #print("False, input again")
#                                 #text=input("Input(No sign and No space) :")
#                             '''
#                             try:
#                                 if os.path.exists('image_css/'+text):
#                                     music("khongphaibanroi.mp3")
#                                     print("khong phai ban roi")
#                                     #sleep(1)
#                                     duyet = input('ban co chac rang ban khong quen toi : ( yes/no)')
#                                     if duyet == 'yes':
#                                         text = str(id(text))
#                                     else :
#                                         bien_=0
#                                         button =0
#                                         break
#                             except:
#                                 pass
#                             '''
#                             if 1:
#                                 dem_anh = 0
#                                 while True:
#                                     while True:
#                                         if dem_anh > 50:
#                                             dem_nhac += 1
#                                             cv2.destroyAllWindows()
#                                             return main(argv,dem_nhac) # return
#                                             break
                
#                                         image_ = image_queue.get()
#                                         cv2.imshow('add_person', image_)

#                                         if cv2.waitKey(1) & 0xff == ord('a'):
#                                             try:
#                                                 if not os.path.exists('image_css/'+text):
#                                                     os.mkdir('image_css/'+text)
                                            
#                                             except:
#                                                 traceback.print_exc()
#                                                 pass
#                                             cv2.imwrite('image_css/'+str(text)+'/'+'classe'+str(dem_anh)+'.jpg',image_)
#                                             list_image_css.append('image_css/'+str(text)+'/classe'+str(dem_anh)+'.jpg')
#                                             dem_anh = dem_anh +1
#                                 del(video)
#                         else:
#                             pass
                name = "Unknow"
                boxes = detector.detect(frame)
                labels = recog.recog(frame, boxes, threshold=0.4)
                recog.put_to_result_buffer(boxes,labels)

                # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]
                # face_names.append(name)
                #problem realtime : regular review
                name_linkfile = str(time.localtime(time.time()).tm_mon)+'_'+str(time.localtime(time.time()).tm_mday)+'_'+str(time.localtime(time.time()).tm_year)

                ### PUSH ID TO WEBAPP


                try:
                    if name.isdigit():
                        letiennhat = open('hide_on_push/id.txt','w+')
                        letiennhat.write(name)
                        letiennhat.close()
                    else:
                        letiennhat = open('hide_on_push/id.txt','w+')
                        letiennhat.write(name)
                        letiennhat.close()
                except:
                    traceback.print_exc()
                    if name != "Unknow":
                        letiennhat = open('hide_on_push/name_id.txt','w+')
                        letiennhat.write(splitname(name))
                        letiennhat.close()
                        letiennhat = open('hide_on_push/id.txt','w+')
                        letiennhat.write(name)
                        letiennhat.close()
                try:
                    LeTienNhat= open('hide_on_push/html3.html','w+')
                    LeTienNhat.write('<meta http-equiv="refresh" content="2"><img src="scv/'+str(name)+'.jpg" alt="Anh dai dien" width="100%" height="100%">')
                    LeTienNhat.close()
                except:
                    pass
                if name != "Unknow":
                    pass

                if len(face_locations_count)>=2:
                    letiennhat = open('best/ten.txt','w+')
                    letiennhat.write("EVERYONE")
                    letiennhat.close()
                    #time.sleep(0.25)

                if name != "Unknow":
                    unknow_count=0
                    name_file = 'regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt'
                    open_file = open(name_file+'/'+name_linkfile+'.txt','a+')#create if not have
                    open_file.close()
                    
                    open_file = open(name_file+'/'+name_linkfile+'.txt','r+')#thang_ngay_nam.txt
                    #open_file1 = open(name_file+'/1.txt','a+') #check tinh thuong xuyen
                    time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','r+')
                    hiendien_ten = list(time_os.read().split())
                    if name in rutgon_:
                        if name not in hiendien_ten:
                            hiendien += 1
                    
                    if name not in list(open_file.read().split()):
                        
                        cursor = database.cursor()
                        image_64 = 'sbuilding'+name+str(time.localtime(time.time()).tm_mday)+str(time.localtime(time.time()).tm_mon)+str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_hour)+'readbase'
                        #image_64 = '../test_options/static/'+image_64+'.jpg'
                        cv2.imwrite('../test_options/static/sbuilding/'+image_64+'.jpg',frame)
                        # time.sleep(0.5)
                        #time.sleep(2
                        # image_base = open('status_sv/'+image_64+'.jpg', 'rb')
                        
                        # imread = image_base.read()
                        # image_64 = base64.encodebytes(imread)

                        # print(image_64)
                        # print(type(image_64))
                        #image_base.close()
                        #try:
                           # os.remove('status_sv/'+image_64+'.jpg')
                        #except:
                            #pass
                        # test_base = open('test64.txt','w+')
                        # test_base.write(image_64.decode('utf-8'))
                        # test_base.close()

                        # image_64=image_64.decode("utf-8")
                        # print(type(image_64))

                        cursor.execute("use mysqldb1")
                        # cursor.execute("insert into b values({})".format(image_64))
                        query = """insert into realtime_0 values(%s,%s,%s,%s,%s,%s)"""
                        query_1 = """insert into realtime_0 select %s,%s,%s,%s,%s,%s,hovaten,donvi,ngaysinh,gioitinh,\
                        chucvu,trinhdo,hocham from manager where maso = %s"""
                        value_query = name,str(time.localtime(time.time()).tm_mday),str(time.localtime(time.time()).tm_mon),str(time.localtime(time.time()).tm_year),str(time.localtime(time.time()).tm_hour),image_64,name
                        cursor.execute(query_1,value_query)
                        database.commit()
                        cursor.close()
                        #database.close()
                        bien_vang=1
                        open_file.close()
                        open_file = open(name_file+'/'+name_linkfile+'.txt','a+')#thang_ngay_nam.txt
                        open_file.write('\n'+str(name))
                        open_file.close()
                elif name =="Unknow":
                    unknow_count +=1
                    if unknow_count >=10:
                        unknow_count =0
                        print("warning")
                        image_64 = 'sbuilding'+name+str(time.localtime(time.time()).tm_mday)+str(time.localtime(time.time()).tm_mon)+str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_hour)+'readbase'
                        
                        cv2.imwrite('../test_options/static/sbuilding/'+image_64+'.jpg',frame)
                        # time.sleep(0.5)
                        #time.sleep(2
                        #image_base = open('status_sv/'+image_64+'.jpg', 'rb')
                        
                        #imread = image_base.read()
                        #image_64 = base64.encodebytes(imread)
                        

                        # print(image_64)
                        # print(type(image_64))
                        #image_base.close()
                        #try:
                            #os.remove('status_sv/'+image_64+'.jpg')
                        #except:
                            #pass
                        
                        try:
                            #print(111)
                            # database1 = pymysql.connect(host='localhost',
                            #                         user='be',
                            #                         password='blueeyes',
                            #                         autocommit = True

                            #                         )
                            #print(222)
                            cursor1 = database.cursor()
                            #print(333)
                            cursor1.execute("use mysqldb1")
                            query_3="""insert into realtime_0(id,ngay,thang,nam,gio,url,hovaten,donvi,ngaysinh,gioitinh,chucvu,trinhdo,hocham) values(0,%s,%s,%s,%s,%s,'unknown','unknown',0,0,0,0,0)"""
                            values_2 = str(time.localtime(time.time()).tm_mday),str(time.localtime(time.time()).tm_mon),str(time.localtime(time.time()).tm_year),str(time.localtime(time.time()).tm_hour),image_64
                            cursor1.execute(query_3,values_2)
                            database.commit()
                            cursor1.close()
                            # database1.close()
                        except:
                            pass
                        
                time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','a+')
                time_os.close()
                time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','r+')
                try:
                    if name in list(time_os.read().split()):
                        thuongxuyen_ = 1
                    
                    else :
                        thuongxuyen_ = 0
                    
                except:
                    traceback.print_exc()
                    pass
                time_os.close()
                    
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.5*2
        thick = 1
        glow = 2 * thick
        
        # Color settings
        black = (0, 0, 0)
        white = (255, 255, 255)
        yellow = (0, 255, 255)
        red = (0, 255, 255)
        #cv2.putText(frame, localtime, (800, 50), font, scale, red, glow)
        if name != "Unknow":
            if name in k:
                bien=1
            else:
                bien=0
        else:
            if bien_==10 :
                bien=0
                #bien_=0
            else:
                bien=1

    
        for i in k:
            if i == "Unknow":
                k.remove("Unknow")
        ls=[]
        for i in k:
            if i not in ls:
                n.append(i)

        k=ls
        process_this_frame = not process_this_frame

        time_local = time.localtime(time.time())   #truy xuat thong tin time

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            #print(distance_cal(4.0,870,int(right-left))*2.54)
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            # problem : nhieu nguoi va 1 nguoi .
            #k=[name]
            k.append(name)
            n=[]
            for i in k:
                if i not in n:
                    n.append(i)
            #print(n)
            if len(n)>=2 :
                    text_signal = open("best/signal.txt",'w+')
                    text_signal.write("1")
                    text_signal.close()
                    # text_signal = open("best/ten.txt",'w+')
                    # text_signal.write("EVERYONE")
                    # text_signal.close()
                    #time.sleep(1)
            elif(len(n)<2):
                text_signal = open("best/signal.txt","w+")
                text_signal.write("0")
                text_signal.close()
                #time.sleep(1)
            if name!="Unknow" :
                pass
            else :
                if bien_ >5:
                    cv2.putText(frame, "WARNING UNKNOW", (400,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,179,120),4,cv2.LINE_AA)
                if bien==0:
                    print("Canh bao nguoi la")
            

        
            cv2.putText(frame,name, (left + 6, bottom - 6), font, 1.0, (000, 255, 255), 1)
            if name not in ["TranQuangHuy","NguyenLuongQuang","LeTienNhat","LaTanDat"] and name!="Unknow":
            	cv2.putText(frame,"Kinh Chao Thay/Co : ",(550,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,70,100),4);cv2.putText(frame,str(name),(550,175),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,100),4)
            	if a =="happiness":
            		cv2.putText(frame, "He Thong Phat hien",(50,600),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,100),4)
            		cv2.putText(frame, "Thay/Co dang vui",(90,650),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,100),4)
            	#elif a=="neutral":
            		#cv2.putText(frame, "He Thong Phat hien",(50,600),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            		#cv2.putText(frame, "Thay/Co dang bin",(90,650),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            elif name in ["TranQuangHuy","NguyenLuongQuang","LeTienNhat","LaTanDat"]:
            	if a =="happiness":
            		cv2.putText(frame, "He Thong Phat hien",(50,600),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            		cv2.putText(frame, "Ban dang vui",(90,650),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            	#elif a=="neutral":
            		#cv2.putText(frame, "He Thong Phat hien",(50,600),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            		#cv2.putText(frame, "Ban dang buon",(90,650),cv2.FONT_HERSHEY_SIMPLEX,1,(255,50,110),4)
            else:
            	pass
        #data.draw(frame)//camxuc
        #threading.Thread(target=readvideo_).start()
        for (y1,x2,y2,x1) in face_locations:
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255, 255, 0), 2)
        # cv2.imshow(sourceName, frame)
        boxes_center = [(int((l+r)*100/2/FRAME_WIDTH),int((t+b)*100/2/FRAME_WIDTH)) for t,r,b,l in face_locations]
        if boxes_center:
            print("Face location:", boxes_center)
            print("ID: ", name)
            print()
        # cap.write(frame)
        #share_data['image'] = frame
        if paused:
            key = cv2.waitKey(0)
        else:
            end = datetime.now()
            delta = (end - start)
            if fps != 0:
                delay = 0.001#int(max(1, ((1 / fps) - delta.total_seconds()) * 100))
            else:
                delay = 1
        

            key = cv2.waitKey(delay)
        if key == ord('q') or key == ord('Q') or key == 27:
        	cap.release()
        	break
        elif key == ord('p') or key == ord('P'):
            paused = not paused
        elif args.source == 'video' and (key == ord('r') or key == ord('R')):
            frameNum = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
        elif args.source == 'video' and paused and key == 2424832: # Left key
            frameNum -= 1
            if frameNum < 0:
                frameNum = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
        elif args.source == 'video' and paused and key == 2555904: # Right key
            frameNum += 1
            if frameNum >= frameCount:
                frameNum = frameCount - 1
        elif args.source == 'video' and key == 2162688: # Pageup key
            frameNum -= (fps * 10)
            if frameNum < 0:
                frameNum = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
        elif args.source == 'video' and key == 2228224: # Pagedown key
            frameNum += (fps * 10)
            if frameNum >= frameCount:
                frameNum = frameCount - 1
            video.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
        elif key == 7340032: # F1
            showHelp(sourceName, frame.shape)

        if not paused:
            frameNum += 1
        
    #app.add_url_rule('/hello','tinhtao',tinhtao)
        #return jsonify(a)
    video.release()
    cap.release()
    cv2.destroyAllWindows()

#---------------------------------------------
def drawInfo(frame, frameNum, frameCount, paused, fps, source):
    """
    Draws text info related to the given frame number into the frame image.

    Parameters
    ----------
    image: numpy.ndarray
        Image data where to draw the text info.
    frameNum: int
        Number of the frame of which to drawn the text info.
    frameCount: int
        Number total of frames in the video.
    paused: bool
        Indication if the video is paused or not.
    fps: int
        Frame rate (in frames per second) of the video for time calculation.
    source: str
        Source of the input images (either "video" or "cam").
    """

    # Font settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.5
    thick = 1
    glow = 3 * thick

    # Color settings
    black = (0, 0, 0)
    yellow = (0, 255, 255)

    # Print the current frame number and timestamp
    if source == 'video':
        text = 'Frame: {:d}/{:d} {}'.format(frameNum, frameCount - 1,
                                            '(paused)' if paused else '')
    else:
        text = 'Frame: {:d} {}'.format(frameNum, '(paused)' if paused else '')
    size, _ = cv2.getTextSize(text, font, scale, thick)
    x = 5
    y = frame.shape[0] - 2 * size[1]
    cv2.putText(frame, text, (x, y), font, scale, black, glow)
    cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

    if source == 'video':
        timestamp = datetime.min + timedelta(seconds=(frameNum / fps))
        elapsedTime = datetime.strftime(timestamp, '%H:%M:%S')
        timestamp = datetime.min + timedelta(seconds=(frameCount / fps))
        totalTime = datetime.strftime(timestamp, '%H:%M:%S')

        text = 'Time: {}/{}'.format(elapsedTime, totalTime)
        size, _ = cv2.getTextSize(text, font, scale, thick)
        y = frame.shape[0] - 5
        cv2.putText(frame, text, (x, y), font, scale, black, glow)
        cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

    # Print the help message
    text = 'Press F1 for help'
    size, _ = cv2.getTextSize(text, font, scale, thick)
    x = frame.shape[1] - size[0] - 5
    y = frame.shape[0] - size[1] + 5
    cv2.putText(frame, text, (x, y), font, scale, black, glow)
    cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

#---------------------------------------------
def showHelp(windowTitle, shape):
    """
    Displays an image with helping text.

    Parameters
    ----------
    windowTitle: str
        Title of the window where to display the help
    shape: tuple
        Height and width of the window to create the help image.
    """

    # Font settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1.0
    thick = 1

    # Color settings
    black = (0, 0, 0)
    red = (0, 0, 255)

    # Create the background image
    image = np.ones((shape[0], shape[1], 3)) * 255

    # The help text is printed in one line per item in this list
    helpText = [
    'Controls:',
    '-----------------------------------------------',
    '[q] or [ESC]: quits from the application.',
    '[p]: toggles paused/playing the video/webcam input.',
    '[r]: restarts the video playback (video input only).',
    '[left/right arrow]: displays the previous/next frame (video input only).',
    '[page-up/down]: rewinds/fast forwards by 10 seconds (video input only).',
    ' ',
    ' ',
    'Press any key to close this window...'
    ]

    # Print the controls help text
    xCenter = image.shape[1] // 2
    yCenter = image.shape[0] // 2

    margin = 20 # between-lines margin in pixels
    textWidth = 0
    textHeight = margin * (len(helpText) - 1)
    lineHeight = 0
    for line in helpText:
        size, _ = cv2.getTextSize(line, font, scale, thick)
        textHeight += size[1]
        textWidth = size[0] if size[0] > textWidth else textWidth
        lineHeight = size[1] if size[1] > lineHeight else lineHeight

    x = xCenter - textWidth // 2
    y = yCenter - textHeight // 2

    for line in helpText:
        cv2.putText(image, line, (x, y), font, scale, black, thick * 3)
        cv2.putText(image, line, (x, y), font, scale, red, thick)
        y += margin + lineHeight

    # Show the image and wait for a key press
    cv2.imshow(windowTitle, image)
    cv2.waitKey(0)

#---------------------------------------------
def parseCommandLine(argv):
    """
    Parse the command line of this utility application.

    This function uses the argparse package to handle the command line
    arguments. In case of command line errors, the application will be
    automatically terminated.

    Parameters
    ------
    argv: list of str
        Arguments received from the command line.

    Returns
    ------
    object
        Object with the parsed arguments as attributes (refer to the
        documentation of the argparse package for details)

    """
    parser = argparse.ArgumentParser(description='Tests the face and emotion '
                                        'detector on a video file input.')

    parser.add_argument('source', nargs='?', const='Yes',
                        choices=['video', 'cam'], default='cam',
                        help='Indicate the source of the input images for '
                        'the detectors: "video" for a video file or '
                        '"cam" for a webcam. The default is "cam".')

    parser.add_argument('-f', '--file', metavar='<name>',
                        help='Name of the video file to use, if the source is '
                        '"video". The supported formats depend on the codecs '
                        'installed in the operating system.')

    parser.add_argument('-i', '--id', metavar='<number>', default=0, type=int,
                        help='Numerical id of the webcam to use, if the source '
                        'is "cam". The default is 0.')


    args = parser.parse_args()

    if args.source == 'video' and args.file is None:
        parser.error('-f is required when source is "video"')

    return args

#---------------------------------------------
# namespace verification for invoking main
#---------------------------------------------
if __name__ == '__main__':
    
    #app.run(debug = True)
#MyApp().run()
    while True:
       main(sys.argv[1:])
    database.close()
