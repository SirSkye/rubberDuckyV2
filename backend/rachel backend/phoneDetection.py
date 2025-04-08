import torch
import cv2
import pygame

#load model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m/l/x

cap = cv2.VideoCapture(0)
pygame.mixer.init() #pygame mixer for sound player

phone = False


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)


#draw box thing ariund pbjects, and run th model
    for *box, conf, cls in results.xyxy[0]:
        if int(cls) in [0, 67]:  #0 ->person, 67=cell phone
            label = model.names[int(cls)] #print the name next to the box
            
            if int(cls) == 67:
                phone = True 
    
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            if(phone):
                print("DETECTED PHONE. GET OFF YO PHONE BOY. YO PHONE LINGING")
                pygame.mixer.music.load("iphone-alarm-remix.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(9)
                phone = False
            
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
   



cap.release()
cv2.destroyAllWindows()