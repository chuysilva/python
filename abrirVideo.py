import cv2
from time import sleep

#Guardar en cap que video voy a capturar
cap = cv2.VideoCapture('')

#Para poder mostrar frame por frame 
while cap.isOpened():
    ret, im = cap.read()
    if ret == False:
        break
    cv2.imshow('imagen', im)

    #Si se presiona ESC se sale del video
    if cv2.waitKey(1) == 27:
        break

    sleep(1/30)