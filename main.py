import numpy as np
import cv2
import cv2.cv as cv
import serial
import serial.tools.list_ports
import time
from threading import Thread
import struct
from transmissor import Transmissor

class Main:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # self.h = 6.5*37.795672
        # self.f = 17.75
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.centro = [320,240]
        self.data = 1
        self.ser = None
        self.buffer = None
        self.found = False
        self.running = True
        self.transmissor = Transmissor()

    def camera(self):
        while True:
            ret, img = self.cap.read()
            image = cv2.GaussianBlur(img,(5,5),10)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.2, 100)

            if circles is not None:
                self.found = True
                circles = np.round(circles[0, :]).astype("int")
                range_x = np.arange(circles[0][0]-10,circles[0][0]+10,1)
                range_y = np.arange(circles[0][1]-10,circles[0][1]+10,1)
                
                for (x, y, r) in circles:
                    cv2.circle(img, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), -1)

                distancia = self.centro[1] - y
                cv2.putText(img,'Distancia X: {0}cm'.format(self.centro[0] - x),(100,100), self.font, 1,(0,0,255),2)
                cv2.putText(img,'Distancia Y: {0}cm'.format(self.centro[1] - y),(100,150), self.font, 1,(0,0,255),2)
                self.data = self.centro[1] - y
                Thread(target = self.transmissor.send(self.data)).start()
            else:
                self.found = False

            cv2.imshow("Alvo", img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                self.running = False
                break
        cap.release()
        cv2.destroyAllWindows()



    def main(self):
        self.camera()


Main().main()