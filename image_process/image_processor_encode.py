#------------------------------------------------------
# The program is an evaluation of the opencv library
#------------------------------------------------------
__author__ = "Sumeet Vaidya"
#------------------------------------------------------

import cv2
import numpy as np
import urllib
import urllib.request as ur
from imutils import paths
import glob
import face_recognition
import pickle
import os

cascPath = "etc/haarcascade_frontalface_default.xml"

image_dir="./images"
enc_dir="./data"
enc_file = enc_dir+"/face_enc"

#get paths of each file in folder named Images
#Images here contains my data(folders of various persons)
all_images = glob.glob(image_dir+"/*.*")
knownEncodings = []
knownNames = []

# loop over the image paths
for imagePath in all_images:
    print (imagePath)
    # extract the person name from the image path
    name = imagePath.split(os.path.sep)[-1]
    name = name.split('.')[0]
    print (name)

    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #Use Face_recognition to locate faces
    boxes = face_recognition.face_locations(rgb,model='hog')
    # compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)

    # loop over the encodings
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
#save encodings along with their names in dictionary data
data = {"encodings": knownEncodings, "names": knownNames}
#use pickle to save data into a file for later use
f = open(enc_file, "wb")
f.write(pickle.dumps(data))
f.close()



#image_file="images/test/waxobe_2021.jpeg"
#faceCascade = cv2.CascadeClassifier(cascPath)
#image = cv2.imread(image_file)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#faces = faceCascade.detectMultiScale(
#    gray,
#    scaleFactor=1.1,
#    minNeighbors=5,
#    minSize=(30, 30),
#    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
#)

#print ("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#cv2.imshow("Faces found", image)
#cv2.waitKey(0)
# wait forever, if Q is pressed then close cv image window
#if cv2.waitKey(0) & 0xFF == ord('q'):
#   cv2.destroyAllWindows()
