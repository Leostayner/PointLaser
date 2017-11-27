
#include <Servo.h> 
Servo myservo;  // create servo object to control a servo 

// Pino analgico do potenciometro
int potpin = 0;

// Variavel que armazena o valor lido do potenciometro
int val;     
int incomingByte = 0;   // for incoming serial data
int i = 0;
int pin3 = 3;
int pin5 = 5;  
  


void setup() 
{ 
  // Define que o servo esta ligado a porta 9
  Serial.begin(9600);      // open the serial port at 9600 bps:
  pinMode(3, OUTPUT);          // sets the digital pin 13 as output
pinMode(5, OUTPUT);          // sets the digital pin 13 as output
  
  
      
  
}


void loop(){
    int pin = 3;
    bool busy = false;
    char myString;
    int n = 0;
  // Le o valor do potenciometro (valores entre 0 e 1023) 
  val = analogRead(potpin);
  // send data only when you receive data:
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    char incomingByte = Serial.read();
    if (incomingByte == '&'){
        Serial.print('F');
        busy = true;
    }
    if(incomingByte == '|' and busy == true){
        Serial.print('E');

    }
    if(busy == true and incomingByte !='&' and incomingByte !='|'){
        if(incomingByte == '-'){
            pin = 5;
        }
        else{
            myString += incomingByte;
            

        }

    }
        
  
  n = atoi(myString);
  n = map(n, -460, 230, 0, 255);     // scale it to use it with the servo (value between 0 and 180)
  analogWrite(pin, 50);
  delay(25);
  }
  else{
    analogWrite(pin3, 0);
    analogWrite(pin5, 0);
  }
}


