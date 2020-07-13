import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:be123456@10.10.46.139:554/Streaming/Channels/101')
FRAME_WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FPS = int(cap.get(cv2.CAP_PROP_FPS))
FPS = 25
out = cv2.VideoWriter('output3.avi', cv2.VideoWriter_fourcc(*'MJPG'),FPS,(FRAME_WIDTH,FRAME_HEIGHT))
while (1):
	ret , frame = cap.read()
	if ret == True:
		#frame = cv2.flip(frame,0)
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()