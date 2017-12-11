*********************************************************************************
It is a basic coding for attendace system using face recognition

Requirements:
opencv 2.4.13,
python 2.7,
a webcam .

The face recognition involves 3 steps
*Dataset
*Trainer
*Detector

The dataset is the pics captured using the webcam which is done by executing the code 
in capture1.py.
The trainer is a file generated of extension .xml using the code tainer.py,the trainer
file is used to detect the face.
Finally the detector is used to detect face with their name.

     The names of the perosons should be fed into the database before the detector starts
comparing,the feeding of data is now done manually but in future I automate it.
     Finally you should create seperate table for attendance in which attendance will be marked,I
used wampserver with mysql as the backend