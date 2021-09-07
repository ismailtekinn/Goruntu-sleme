import cv2
import numpy as np


x=0   # cisim x koordinat için değişken
y=0   # cisim y koordinat için değişken



cap = cv2.VideoCapture(0)  # alınan video cap değişkeine atandı


cap.set(3,600)
cap.set(4,600) # cap değişkenine atanan videonun boyutu belirlendi
_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
y_medium = int(cols / 2)
w_medium = int(cols / 2)
h_medium = int(cols / 2)
center = int(cols / 2)     # cizme ait x y h w bilgileri değişkenlere atandı

while True: 
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # renk algilama işlemi başlatıldı
    
    low_red = np.array([161, 155, 84])    # alt kırımızı rengin bilgileri 
    high_red = np.array([179, 255, 255])  # üst kırımızı rengin bilgileri
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)  # renk bilgileri değişkenen atandı 
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)    # renk algılanırsa işleme devam edilecek
    
    for pic, contour in enumerate(contours): 
        
        area = cv2.contourArea(contour) 
        if(area > 500): 
            x, y, w, h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame, (x, y),  (x + w, y + h),  (0, 0, 255), 2) 

            cv2.putText(frame, "KirmiziBolge", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt) # algılanan rengin x ve y koordinatları bulundu        
        x_medium = int((x + x + w) / 2)
        break
    
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)  # x koordinatı ekranda gösterildi
    cv2.imshow("Frame", frame)    
    print("x ",x," y ",y)
    key = cv2.waitKey(1) 
    if key == 27:   # renk olup olmadığı sorgulandı
        break
        
cap.release()
cv2.destroyAllWindows()