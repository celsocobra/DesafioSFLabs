import cv2
import numpy as np

filename1 = '1591803600_033.avi'
filename2 =  '1591821600_015.avi'

cap1 = cv2.VideoCapture(filename1)
cap2 = cv2.VideoCapture(filename2)
totalNoFrames1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
totalNoFrames2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# Check if camera opened successfully
if (cap1.isOpened()== False):
  print("Error opening video stream or file")

count = 0
#recording
frame_width = int(cap1.get(3))
frame_height = int(cap1.get(4))
fps = int(cap1.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
rec = cv2.VideoWriter(filename1+filename2+'d.avi', fourcc, fps,(frame_width,frame_height))

# looping de gravação 
count = 0
while(cap1.isOpened()):
    # Capture frame-by-frame
    ret, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if ret == True and ret2==True:
        if(count < (totalNoFrames1)):
            rec.write(frame1)
        else:
            rec.write(frame2)    
    count+=1    

# releases
cap1.release()
cap2.release()
rec.release()

# Closes all the frames
cv2.destroyAllWindows()
