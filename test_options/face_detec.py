import pandas as pd
from mtcnn import MTCNN
import mtcnn
import numpy as np
import os
import glob
import cv2
import shutil
from pathlib import Path


def run(string_,id_):
  face_detector = MTCNN(min_face_size=25)

  face_count = 0
  #for path in glob.glob('test.mp4'):
    #print("Processing video ", path)
  video = cv2.VideoCapture(string_)
  break_temp = 0
  while True:

    ret, frame = video.read()
    # cv2.imshow('a',frame)
    if break_temp == 1 :
      break
    if ret == False:
      break
    faces = face_detector.detect_faces(frame)
    for face in faces:
      x,y,w,h = face['box']
      print(w,h)
      if w >= 77 and h >= 96:
        crop = frame[y:y+h,x:x+w,:]
        try:
          if not os.path.exists(str(id_)):
            os.mkdir(str(id_))
          else:
            pass
          # print('Writting to ',  + f'/{face_count}.jpg')
          cv2.imwrite(str(id_)+'/'+str(face_count)+'.jpg', crop)
          face_count += 1
          if face_count == 50 :
            break_temp = 1
            break
            print("done 100 image") 
            
        except:
          print("Error on ", crop.shape)
    # cv2.waitKey(1)
  video.release()
# run("output1.mp4",122150051)
'''
for folder in FOLDER_LIST:
  if folder not in IGNORE_LIST:
    print(f"Extract faces from {folder}")
    face_count = 0
    for path in glob.glob(folder + '/*.mp4'):
      print("Processing video ", path)
      video = cv2.VideoCapture(path)
      while True:
        ret, frame = video.read()
        if ret == False:
          break
        faces = face_detector.detect_faces(frame)
        for face in faces:
          x,y,w,h = face['box']
          print(w,h)
          if w >= 77 and h >= 96:
            crop = frame[y:y+h,x:x+w,:]
            try:
              print('Writting to ', folder + f'/{face_count}.jpg')
              cv2.imwrite(folder + f'/{face_count}.jpg', crop)
              face_count += 1
            except:
              print("Error on ", crop.shape)
        
      video.release()
'''