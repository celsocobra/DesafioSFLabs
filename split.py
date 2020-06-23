import cv2
import numpy as np



#tempo de corte em segundos
time_cut = 60  

filename = '1591803600_033.avi'
cap = cv2.VideoCapture(filename)
totalNoFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# checar se a captura esta sendo feita
if (cap.isOpened()== False):
  print("Error opening video stream or file")


#recording
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
rec1 = cv2.VideoWriter(filename+'a.avi', fourcc, fps,(frame_width,frame_height))
rec2 = cv2.VideoWriter(filename+'b.avi', fourcc, fps,(frame_width,frame_height))

# looping de gravação 
count = 0
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        if(count < fps*time_cut):
            rec1.write(frame)
        else:
            rec2.write(frame)    
    count+=1    

# releases
cap.release()
rec1.release()
rec2.release()
# Closes all the frames
cv2.destroyAllWindows()
