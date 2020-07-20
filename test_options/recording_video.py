import cv2
import numpy as np
import pymysql
import os
database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,db="mysqldb1")
cap = cv2.VideoCapture('rtsp://admin:be123456@10.10.46.224:554/Streaming/Channels/101')
# cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('video/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

while(True):
  ret, frame = cap.read()

  if ret == True:
    frame = cv2.resize(frame,(0,0),fx=1/2,fy=1/2)
    cursor = database.cursor()
    cursor.execute("select * from learn_values")
    # cursor = database.cursor()

    a = cursor.fetchall()[0][0]
    cursor.close()
    print(a)
    if a == 1:
      try:
        if not os.path.exists('video/outpy.avi'):
          out = cv2.VideoWriter('video/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))
        else:
          pass
      except:
        pass
      # Write the frame into the file 'output.avi'
      out.write(frame)
    elif a == 2 :
      print(a)
      print('stop')
      out.release()
      # cursor.close()
      pass
    else:
      pass

    # Display the resulting frame    
    cv2.imshow('frame',frame)

    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break  

# When everything done, release the video capture and video write objects
cap.release()

database.close()
# Closes all the frames
cv2.destroyAllWindows() 