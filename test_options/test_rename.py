import os
import cv2
#os.mkdir("1733987745")
#os.rename("1733987745","../1733987745")
#files = os.listdir(os.getcwd()+'/uploads')
#for f in files:
#    os.remove(os.getcwd()+'/uploads/'+f)
os.rename('video/outpy.avi','video/output1.avi')
cv2.VideoWriter('video/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,850))

