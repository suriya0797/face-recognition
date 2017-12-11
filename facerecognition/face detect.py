import cv2
import numpy as np
import datetime
import pymysql

def putattendance(Id):
    conn=pymysql.connect(user="root",password="",host="127.0.0.1",port=3306,database="facerecattend")
    a = conn.cursor();
    print("Database connection created...")
    sql = "select * from faceattend;"
    print("Query Yet to execute...");
    a.execute(sql);
    print("Query executed...");
    sql3="select * from faceattend where id1='"+Id+"';"
    a.execute(sql3);
    res2=a.fetchall()
    for row in res2:
        n1=row[1]
    now =datetime.datetime.now()
    date=now.strftime("%y-%m-%d %H:%M:%S")
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    print(date)
    sql2="insert into attendance (id1,date,name,attendance) values('"+Id+"','"+date+"','"+n1+"','present');"
    a.execute(sql2)
    print("The attendance to "+n1+" on "+date+" was marked.");
    
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")
id=0
conn=pymysql.connect(user="root",password="",host="127.0.0.1",port=3306,database="facerecattend")
a = conn.cursor();
print("Database connection created...")
sql = "select * from faceattend;"
print("Query Yet to execute...");
a.execute(sql);
print("Query executed...");
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
result=a.fetchall()
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        Id=str(id)
        print(Id)
        for row in result :
            sql1="select * from faceattend where id1='"+Id+"';"
            a.execute(sql1)
            res1=a.fetchall()
            for row in res1:
                name1=row[1];
            print(name1)
        cv2.cv.PutText(cv2.cv.fromarray(img),str(name1),(x,y+h),font,255)
    cv2.imshow("FACE",img)
    if(cv2.waitKey(1)==ord('q')):
        putattendance(Id)
        break
cam.release()
cv2.destroyAllWindows()                   
