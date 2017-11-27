import numpy as np
import cv2
import cv2.cv as cv
import serial
import serial.tools.list_ports
import time
from threading import Thread


cap = cv2.VideoCapture(0)
h = 6.5*37.795672
f = 17.75
font = cv2.FONT_HERSHEY_SIMPLEX
centro = [320,240]
self.data = None
#Conexao Arduino
# Com = "/dev/cu.usbmodem1451"
# ser = serial.Serial(Com,9600)
# print("Connection succesfull")
erro = 0
C = 0.4

def get_ports():
    
    ports = serial.tools.list_ports.comports()
    
    return ports

def findArduino(portsFound):
    
    commPort = 'None'
    numConnection = len(portsFound)
    
    for i in range(0,numConnection):
        port = foundPorts[i]
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

def sendData():
    while True:
        if data!= None:
            data = str(data)
            ser.write(data)
            print("Sent")
            time.sleep(1)
    
    # ser.read()

def convertPWM():
    value = 1 * C   
    return value

def listen():
    while True:
        VALUE_SERIAL=ser.read()


def main():
    while True:
        ret, img = cap.read()
        image =cv2.GaussianBlur(img,(5,5),10)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.2, 100)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            range_x = np.arange(circles[0][0]-10,circles[0][0]+10,1)
            range_y = np.arange(circles[0][1]-10,circles[0][1]+10,1)
            
            for (x, y, r) in circles:
                cv2.circle(img, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), -1)

            distancia = centro[1] - y
            cv2.putText(img,'Distancia X: {0}cm'.format(centro[0] - x),(100,100), font, 1,(0,0,255),2)
            cv2.putText(img,'Distancia Y: {0}cm'.format(centro[1] - y),(100,150), font, 1,(0,0,255),2)
            self.data = centro[1] - y

        cv2.imshow("Alvo", img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

foundPorts = get_ports()        
connectPort = findArduino(foundPorts)
if connectPort != 'None':
    ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
    print('Connected to ' + connectPort)
    Thread(target = sendData).start()
    main()
else:
    print('Connection Issue!')
