from flask import Flask, redirect, url_for, request,render_template
import threading
import queue
import time
import os
import sys
import argparse
import cv2
import numpy as np
from collections import OrderedDict
from datetime import datetime, timedelta

from faces import FaceDetector
from data import FaceData
from gabor import GaborBank
from emotions import EmotionsDetector

class VideoData:

    """
    Helper class to present the detected face region, landmarks and emotions.
    """

    #-----------------------------------------
    def __init__(self):
        """
        Class constructor.
        """

        self._faceDet = FaceDetector()
        '''
        The instance of the face detector.
        '''

        self._bank = GaborBank()
        '''
        The instance of the bank of Gabor filters.
        '''

        self._emotionsDet = EmotionsDetector()
        '''
        The instance of the emotions detector.
        '''

        self._face = FaceData()
        '''
        Data of the last face detected.
        '''

        self._emotions = OrderedDict()
        '''
        Data of the last emotions detected.
        '''

    #-----------------------------------------
    def detect(self, frame):
        """
        Detects a face and the prototypic emotions on the given frame image.

        Parameters
        ----------
        frame: numpy.ndarray
            Image where to perform the detections from.

        Returns
        -------
        ret: bool
            Indication of success or failure.
        """

        ret, face = self._faceDet.detect(frame)
        if ret:
            self._face = face

            # Crop just the face region
            frame, face = face.crop(frame)

            # Filter it with the Gabor bank
            responses = self._bank.filter(frame)

            # Detect the prototypic emotions based on the filter responses
            self._emotions = self._emotionsDet.detect(face, responses)
            
            return self._emotions
        else:
            self._face = None
            return False

    #-----------------------------------------
    def draw(self, frame):
        """
        Draws the detected data of the given frame image.

        Parameters
        ----------
        frame: numpy.ndarray
            Image where to draw the information to.
        """
        # Font settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.5
        thick = 1
        glow = 3 * thick

        # Color settings
        black = (0, 0, 0)
        white = (255, 255, 255)
        yellow = (0, 255, 255)
        red = (0, 0, 255)

        empty = True

        # Plot the face landmarks and face distance
        x = 5
        y = 0
        w = int(frame.shape[1]* 0.2)

        try:
            face = self._face
            empty = face.isEmpty()
            #face.draw(frame)
        except:
            pass

        # Plot the emotion probabilities
        try:
            emotions = self._emotions
            if empty:
                labels = []
                values = []
            else:
                labels = list(emotions.keys())
                values = list(emotions.values())
                bigger = labels[values.index(max(values))]

                # Draw the header
                text = 'emotions'
                size, _ = cv2.getTextSize(text, font, scale, thick)
                y += size[1] + 20

                cv2.putText(frame, text, (x, y), font, scale, black, glow)
                cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

                y += 5
                cv2.line(frame, (x,y), (x+w,y), black, 1)

            size, _ = cv2.getTextSize('happiness', font, scale, thick)
            t = size[0] + 20
            w = 150
            h = size[1]
            for l, v in zip(labels, values):
                lab = '{}:'.format(l)
                val = '{:.2f}'.format(v)
                size, _ = cv2.getTextSize(l, font, scale, thick)

                # Set a red color for the emotion with bigger probability
                color = red if l == bigger else yellow

                y += size[1] + 15

                p1 = (x+t, y-size[1]-5)
                p2 = (x+t+w, y-size[1]+h+5)
                cv2.rectangle(frame, p1, p2, black, 1)

                # Draw the filled rectangle proportional to the probability
                p2 = (p1[0] + int((p2[0] - p1[0]) * v), p2[1])
                cv2.rectangle(frame, p1, p2, color, -1)
                cv2.rectangle(frame, p1, p2, black, 1)

                # Draw the emotion label
                cv2.putText(frame, lab, (x, y), font, scale, black, glow)
                cv2.putText(frame, lab, (x, y), font, scale, color, thick)

                # Draw the value of the emotion probability
                cv2.putText(frame, val, (x+t+5, y), font, scale, black, glow)
                cv2.putText(frame, val, (x+t+5, y), font, scale, white, thick)
        except Exception as e:
            print(e)
            pass
# frame = cv2.imread('nhat__.jpg')
# small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25,interpolation = cv2.INTER_CUBIC)
# rgb_small_frame = small_frame[:, :, ::-1]

# data = VideoData()
# a = data.detect(rgb_small_frame)
# print(a)

app = Flask(__name__)
name ="abcy"
#name_="aa"
name_ = queue.Queue(maxsize=1)
time_ = queue.Queue(maxsize=1)
list_name = queue.Queue(maxsize=1)
list_name_vang = queue.Queue(maxsize=1)
list_SV = queue.Queue(maxsize=1)
signal = queue.Queue(maxsize=1) #chaocac ban
chuyencan = queue.Queue(maxsize=1)
ten_signal = queue.Queue(maxsize=1) #chao ten
camxuc = queue.Queue(maxsize=1)#camxuc
try:
	signal_text = open("best/camxuc.txt","r")
	camxuc = signal_text.read().split()[0]
	signal_text.close()
except:
	pass
try:
	signal_text = open("best/text_signal.txt","r")
	signal = signal_text.read().split()[0]
	signal_text.close()
except:
	pass
try:
	signal_text = open("best/ten.txt","r")
	ten_signal = signal_text.read().split()[0]
	signal_text.close()
except:
	pass
danhsachvang = ["a",'b']
try:
   danhsachvang = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
         str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'_vang.txt'\
         ,'r')
   list_name_vang = danhsachvang.read().split()
   danhsachvang.close()
except:
   pass
# list_name_vang = danhsachvang.read().split()
# danhsachvang.close()
danhsachsv = open('best/listsv.txt','r')
list_SV = danhsachsv.read().split()
danhsachsv.close()
danhsachcomat=["c",'d']
try:
   danhsachcomat = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
         str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'.txt','r')
   list_name=danhsachcomat.read().split()
   danhsachcomat.close()
except:
   pass
# list_name=danhsachcomat.read().split()
#print(list_name)
# danhsachcomat.close()
chuyencan1 = open('best/chuyencan.txt','r')
chuyencan=chuyencan1.read().split()
chuyencan1.close()
try:
   for i in list_SV:
      if i not in list_name:
         chuyencan[list_SV.index(i)]=int(chuyencan[list_SV.index(i)])+1
      else:
         pass
except:
   pass
chuyencan2 = open('best/chuyencan.txt','w+')
for i in chuyencan:
   chuyencan2.write("\n"+str(i))
chuyencan2.close()
   
list_camxuc = []
for i in range(23):
   list_camxuc.append('x')
# frame = cv2.imread('nhat__.jpg')
# small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25,interpolation = cv2.INTER_CUBIC)
# rgb_small_frame = small_frame[:, :, ::-1]

# data = VideoData()
# a = data.detect(rgb_small_frame)
# print(a)
for i in list_SV:
   try:
      a = os.listdir('status_sv/'+str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday)\
         +'_'+str(time.localtime(time.time()).tm_year)+ '/'+i)
      frame = cv2.imread('status_sv/'+str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday)\
         +'_'+str(time.localtime(time.time()).tm_year)+ '/'+i+'/'+i+'.jpg')
      small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25,interpolation = cv2.INTER_CUBIC)
      rgb_small_frame = small_frame[:, :, ::-1]
      data = VideoData()
      camxuc__ = data.detect(rgb_small_frame)
      list_camxuc[list_SV.index(i)]=camxuc__
   except:
      continue


def name():
   global name_
   global list_name
   global list_SV
   global list_name_vang
   global chuyencan
   global signal
   global ten_signal
   global camxuc

   while 1:
      danhsachvang=["a",'d']

      try:
         danhsachvang = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
            str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'_vang.txt'\
            ,'r')
         list_name_vang = danhsachvang.read().split()
         danhsachvang.close()
      except:
         pass
      # list_name_vang = danhsachvang.read().split()
      # danhsachvang.close()
      danhsachsv = open('best/listsv.txt','r')
      list_SV = danhsachsv.read().split()
      danhsachsv.close()
      danhsachcomat =["b", 'e']
      try:
         danhsachcomat = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
            str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'.txt','r')
         list_name=danhsachcomat.read().split()
         danhsachcomat.close()
      except:
         pass
      # list_name=danhsachcomat.read().split()
      #print(list_name)
      # danhsachcomat.close()
      try:
      	signal_text = open("best/text_signal.txt",'r')
      	signal = signal_text.read().split()[0]
      	signal_text.close()
      except:
      	pass
      try:
      	signal_text = open("best/camxuc.txt","r")
      	camxuc = signal_text.read().split()[0]
      	signal_text.close()
      except:
      	pass
      try:
      	signal_text = open("best/ten.txt","r")
      	ten_signal = signal_text.read().split()[0]
      	signal_text.close()
      except:
      	pass

      letiennhat = open('best/ten.txt','r')
      name_=letiennhat.readline()
      letiennhat.close()

      chuyencan1 = open('best/chuyencan.txt','r')
      chuyencan=chuyencan1.read().split()
      chuyencan1.close()
      #print(time_)
      #print(name_)

@app.route('/login/<name>')
def failed(name):
   return 'fail pass or user'
@app.route('/upload/<name>') 
def upload():
	return render_template('upload.html')
@app.route('/<name>')
def successis(name):
	#PEOPLE_FOLDER = os.path.join('static', 'people_photo')
	#app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
	#full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
   # name1="a"
   #print(name1)ten_signal
   #return render_template("index1.html")
	return render_template('index.html',lit_comat = list_name, lit_vang = list_name_vang, lit_sv = list_SV, lits=chuyencan,list_camxuc=list_camxuc,signal=signal,camxuc=camxuc,ten_signal=ten_signal)
@app.route('/login',methods = ['POST', 'GET'])ten_signal
def login():
   if request.method == 'POST':
      user = request.form['nm']
      passe = request.form['pass']
      if user == "admin" and passe == "admin":
      	return redirect(url_for('successis',name = user ))
      elif user == "admin1" and passe == "admin1":
      	return redirect(url_for('upload',name=user))
      else:
      	return redirect(url_for('failed',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
#@app.route('/index')
#def show_index():
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    
if __name__ == '__main__':
   threading.Thread(target = name).start()
   #print(name_)
   app.run(debug = False)
