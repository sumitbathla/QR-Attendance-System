import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2, time 
import csv

counter = 0

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        img = qrcode.make((row[1]))
        img.save("QR/code"+ str(counter) +".jpg")
        counter+=1