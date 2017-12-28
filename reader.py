import cv2
import numpy as np
import json
import base64

u=0
with open('data.txt') as json_file:  
    data = json.load(json_file)
while(u<53):
	for p in data[str(u)]:
		print('TimeStamp: ' + str(p['TimeStamp']))
		jpg_original = base64.b64decode(p['Original_Image'])
		jpg_cropped = base64.b64decode(p['Cropped_Image'])
		with open('test1.jpg', 'wb') as f_output:
			f_output.write(jpg_original)
		with open('test2.jpg', 'wb') as f_output:
			f_output.write(jpg_cropped)
		imgO = cv2.imread("test1.jpg",1)
		imgC = cv2.imread("test2.jpg",1)
		cv2.imshow("IMAGEOrig",imgO)
		cv2.imshow("IMAGECrop",imgC)
		cv2.waitKey(100)
	u=u+1	

