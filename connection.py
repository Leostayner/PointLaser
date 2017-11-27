import numpy as np
import cv2
import cv2.cv as cv
import serial
import serial.tools.list_ports
import time
from threading import Thread
import struct

class Main:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # self.h = 6.5*37.795672
        # self.f = 17.75
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.centro = [640,360]
        self.data = 1
        self.ser = None
        self.buffer = None
        self.found = False
        self.running = True


    def get_ports(self):
        ports = serial.tools.list_ports.comports()
        return ports

    def findArduino(self,portsFound):
        commPort = 'None'
        numConnection = len(portsFound)
        for i in range(0,numConnection):
            port = portsFound[i]
            print(port)
            strPort = str(port)
            
            if 'Generic' in strPort: 
                splitPort = strPort.split(' ')
                commPort = (splitPort[0])
        return commPort           

    def getData():
        arduinoString = arduinoData.readline()
        arduinoString = arduinoString[:-2]
        arduinoString = arduinoString.decode()            
        return float(arduinoString)

    def sendData(self):
        if self.running:
            st = str(self.data)
            if len(st) == 2:
                str(self.data)
            while True:
                if self.found:
                    
                    #self.ser.write('&&'+str(self.data)+'||')
                    self.ser.write(str(self.data)+'\n')
                    print("[PYTHON] Sent: {}" .format(self.data))
                time.sleep(0.2)
        # ser.read()

    def convertPWM():
        value = 1 * C
        return value

    def listen(self):
        if self.running:
            while True:
                if  self.ser.in_waiting:
                    self.buffer = self.ser.read()
                    print('[ARDUINO] Listening: {}'.format(self.buffer))
                time.sleep(0.1)
        


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
            else:
                self.found = False

            cv2.imshow("Alvo", img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                # t1.stop()
                # t2.stop()
                self.running = False
                break
        cap.release()
        cv2.destroyAllWindows()



    def main(self):
        foundPorts = self.get_ports()        
        connectPort = self.findArduino(foundPorts)
        if connectPort != 'None':
            self.ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
            print('Connected to ' + connectPort)
            Thread(target = self.listen).start()
            Thread(target = self.sendData).start()
            self.camera()
        else:
            print('Connection Issue!')


Main().main()




