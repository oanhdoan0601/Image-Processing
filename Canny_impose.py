#######################################################
# Purpose   :Canny impose for Edge Detection in Real time             # 
#######################################################

 

# import libraries of python OpenCV  
 
import cv2  
  
# np is an alias pointing to numpy library 
import numpy as np 
  
  
# capture frames from a camera

url = 0

cap = cv2.VideoCapture(url) 
# initiate alpha for blending egde image to real time frame
alpha =0.4 
minVal=40
maxVal=240
# loop runs if capturing has been initialized 
while(1): 
  
    # reads frames from a camera 
    ret, frame = cap.read() 

    # Display an original image 
    cv2.imshow('Original',frame) 
  
    # finds edges in the input image image and 
    # marks them in the output map edges 
    edges = cv2.Canny(frame,minVal,maxVal)
    #height, width, channels = frame.shape
    #print(channels)
    edges_impose= cv2.merge((edges,edges,edges))
    # Display edges in a frame 
    cv2.imshow('Edges',edges) 
    #impose frame and edges
    added_image = cv2.addWeighted(edges_impose,alpha,frame,1-alpha,0)
    cv2.imshow('added_image', added_image)
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(5) & 0xFF
    if k == ord('s'):
        cv2.imwrite('Impose_Image.png',added_image) 
    if k == 27: 
        break
       # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1

    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0


    # press p   plus 10 from minVal
    if k== ord('p'):
        minVal +=20
        if minVal>=120:
           minVal =120
    # press m to minus 10 from maxVal
    elif k== ord('m'):
        maxVal -= 20
        if maxVal <=140:
           maxVal = 120

# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  
