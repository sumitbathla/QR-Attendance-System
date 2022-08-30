from pyzbar.pyzbar import decode
from PIL import Image
import cv2, time 
import csv

import warnings
warnings.filterwarnings("ignore")

video = cv2.VideoCapture(0)

studentsList = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        studentsList.append((row[1]))
    print(studentsList) 

while True:
    check, frame = video.read()
    d = decode(frame)
    try:
        for obj in d:
            name = d[0].data.decode()
            if name in studentsList:
                studentsList.remove(name)
                print()
                print("Attendance Marked for" + name)
                print("Students Left:")
                print(studentsList)
                print()
    except:
        print("Error")

    cv2.imshow("Attendance", frame)
    key = cv2.waitKey(1)
    if key==ord("q"):
        print()
        print("Absentees:")
        print(studentsList)
        break

video.release()
cv2.destroyAllWindows()