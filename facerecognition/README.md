# Face Recognition Attendance System - FACEIUM

## Description:
    Faceium is a simple model system for attedance by using face as a id.

## Requirements:

- Opencv 2.4.9

- Python 2.7

- Webcam
   
- Wamp server 

## Packages

- cv2
- pymysql
- os
- numpy
- PIL
The packages can also be installed from this link
http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-image

## The face recognition involves 3 steps

- Dataset

- Trainer

- Detector


The dataset is the pics captured using the webcam which is done by executing the code 
in capture1.py and in this phase the names of the person are stored along with the id.

The trainer is a file generated of extension .xml using the code tainer.py,the trainer
file is used to detect the face.

Finally the detector is used to detect face with their name.
   comparing,the feeding of data is now done manually but in future I automate it.
   Finally you should create seperate table for attendance in which attendance will be marked,I
   used wampserver with mysql as the backend
   The harrcascade.yml file which I included in the project is a file which analyzes the image and 
   gives the training.yml file so just store all the image dataset folder,recognizer folder which 
   contains the trainer file,harcascade and all the coding files in one folder so that it will not
   throw error due to unknown path.
