import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
import pytesseract
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

model = YOLO('/home/syedatta/Documents/best.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('/home/syedatta/License_plate_detection/License-Plate-Detection/mycarplate.mp4')

with open("/home/syedatta/License_plate_detection/License-Plate-Detection/coco1.txt", "r") as my_file:
    data = my_file.read()
class_list = data.split("\n")

area = [(27, 375), (16, 456), (1015, 451), (992, 378)]

count = 0
processed_numbers = set()

df = pd.DataFrame(columns=['NumberPlate', 'Date', 'Time'])

while True:    
    ret, frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
        break
   
    frame = cv2.resize(frame, (1020, 500))
    
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
   
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        
        d = int(row[5])
        c = class_list[d] 
        
        cx = int(x1 + x2) // 2
        cy = int(y1 + y2) // 2
        
        result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
        if result >= 0:
            crop = frame[y1:y2, x1:x2]
            gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(gray, 15, 17, 17)

            text = pytesseract.image_to_string(gray).strip()
            text = text.replace('(', '').replace(')', '').replace(',', '').replace(']','').replace('}','').replace('|','')
            
            if text not in processed_numbers:
               processed_numbers.add(text)
               
               current_datetime = datetime.now()
               date_str = current_datetime.strftime("%Y-%m-%d")
               time_str = current_datetime.strftime("%H:%M:%S")
               
               df = df._append({'NumberPlate': text, 'Date': date_str, 'Time': time_str}, ignore_index=True)
               
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.imshow('crop', crop)

    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)
    cv2.imshow("RGB", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()    
cv2.destroyAllWindows()

print(df)
df.to_csv("/home/syedatta/License_plate_detection/car_plate_data.csv", index=False)
