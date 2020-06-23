import cv2
import numpy as np

#tempo de corte em segundos
time_cut1 = 296
time_cut2 = 414

filename = '2020-06-10_5e6cc740081bb44ed69a2538_1591794000.avi'
cap = cv2.VideoCapture(filename)
totalNoFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

count = 0
#recording
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
rec = cv2.VideoWriter(filename+'c.avi', fourcc, fps,(frame_width,frame_height))

# Read until video is completed
while (cap.isOpened()):
    #Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        if(count > (fps*time_cut1) and count < (fps*time_cut2)):
            rec.write(frame)
    count+=1    

# When everything done, release the video capture object
cap.release()
rec.release()
# Closes all the frames
cv2.destroyAllWindows()
