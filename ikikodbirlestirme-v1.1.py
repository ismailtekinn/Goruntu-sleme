import cv2
import numpy as np

x=0   # cisim x koordinat için değişken
y=0   # cisim y koordinat için değişken

cap = cv2.VideoCapture(0)
_, prev = cap.read()
prev = cv2.flip(prev, 1)
_, new = cap.read()
new = cv2.flip(new, 1)
rows, cols, _ = prev.shape

x_medium = int(cols / 2)
y_medium = int(cols / 2)
w_medium = int(cols / 2)
h_medium = int(cols / 2)
center = int(cols / 2) 

while True:
    #diff = cv2.absdiff(prev, new)
    #diff = cv2.cvtColor(diff, cv2.COLOR_BGR2HSV)
    hsv_frame = cv2.cvtColor(prev, cv2.COLOR_BGR2HSV)
    low_red = np.array([161, 155, 84])    # alt kırımızı rengin bilgileri 
    high_red = np.array([179, 255, 255])  # üst kırımızı rengin bilgileri
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)  # renk bilgileri değişkenen atandı 
    
    contor, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.circle(prev, (320, 225), 5, (0, 0, 255), -1)
    cv2.line(prev, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)  # x koordinatı ekranda gösterildi
    #cv2.line(prev, (x_medium, 0),(x_medium, 310 ), 4 (0, 0, 255),-1 )  
    
    for contors in contor:
        if cv2.contourArea(contors) > 3000:
            (x, y, w, h) = cv2.boundingRect(contors)
            (x1, y1), rad = cv2.minEnclosingCircle(contors)
            #x_medium = int((x + x + w) / 2)
            x1 = int(x1)
            y1 = int(y1)
            
            # cv2.line(prev, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)  # x koordinatı ekranda gösterildi
            cv2.line(prev, (320, 225), (x1, y1), (255, 0, 0), 2) 
            
            cv2.putText(prev, "{}".format(int(np.sqrt((x1 - 320) ** 2 + (y1 - 225) ** 2))), (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            print(x1 - 320)
            
            
            # cv2.putText(prev, "{}".format(int(np.sqrt((x1 - 320) ** 2 )), (100, 100),
            #             cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)  
            # cv2.putText(prev, "{}" .format(int(np.sqrt(x1-320) ** 2)), (0, 0, 255), 2)
            #cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

            
            cv2.rectangle(prev, (x, y), (x + w, y + h), (0,255, 0), 2)
            cv2.circle(prev, (x1, y1), 5, (0, 255, 0), -1)
            
            if (x1-320 > 0):  
               # print("cisim ekranın Sagında")
               cv2.putText(prev,  "Cisim Ekranin"  +str(int(x1)-320)+   "Birim Saginda"   ,(x1-320, y1-225), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1)
               
            
            elif(x1-320 < 0):
               # print("cisim ekranın solunda")
               cv2.putText(prev, "Cisim Ekranin"  +str(int(x1)-320)+   " Birim Solunda"  +str(int(x1)-320)+ " Birim Saga Kaydırın" ,(x1-320, y1-225), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1)
            
            
    cv2.imshow("orig", prev)
    prev = new
    _, new = cap.read()
    new = cv2.flip(new, 1)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()