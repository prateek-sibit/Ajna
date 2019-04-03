# Script for Extracting Faces

import cv2
import numpy as np
from random import randint

face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

def face_detector(frame, directory):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2,
                                             minNeighbors=5, 
                                             minSize=(20,20))
    
    if faces is ():
        return frame
    
    for (x,y,w,h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        cv2.imwrite(directory + str(randint(0,10000))+".jpg",roi_color)

# Loading image
filename_img = 'data/input/football.jpg'
directory = 'Extracted/test2/'

img = cv2.imread(filename_img)
face_detector(img, directory)
        