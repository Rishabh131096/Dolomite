import cv2
import json
import base64
import time

data = {}

cap = cv2.VideoCapture("test.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

t=0

End_of_Video = False

while(1):
	
	num_of_frame = 0
	#End_of_video = False
	
	while(num_of_frame!=25):
		
		ret, frame = cap.read()
		
		if ret==False:
			End_of_Video = True
			break

		fgmask = fgbg.apply(frame)
		
		num_of_frame = num_of_frame+1
		print num_of_frame
	
	if End_of_Video==True:
		break
	
	k = cv2.waitKey(1)
	if k == 27:
		break
		
	ret,thresh = cv2.threshold(fgmask,100,255,0)
	__,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	largest_area = 0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		
		if area>largest_area:
			largest_area=area
			x,y,w,h = cv2.boundingRect(cnt)
			
	rect = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	if(rect is None):
		continue
	rect = frame[y:y+h,x:x+w]
	
	imgName = "IMG" + str(t) + ".jpg"
	cv2.imwrite(imgName,rect)
	
	data[t]=[]
	retvalO, bufferO = cv2.imencode('.jpg', frame)
	retvalC, bufferC = cv2.imencode('.jpg', rect)
	jpg_as_text_O = base64.b64encode(bufferO)
	jpg_as_text_C = base64.b64encode(bufferC)
	data[t].append({'TimeStamp': time.time(), 'Original_Image': jpg_as_text_O, 'Cropped_Image': jpg_as_text_C})
	
	t = t+1

	
with open('data.txt','w') as outfile:
	json.dump(data,outfile)
	
cap.release()
cv2.destroyAllWindows()