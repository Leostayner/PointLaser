#include <PID_v1.h>

double Setpoint;
double Input;
double Output;
PID myPID(&Input, &Output, &Setpoint, 0.4, 0, 0,DIRECT);


// Pino analgico do potenciometro
int potpin = A0;

// Variavel que armazena o valor lido do potenciometro
int val;     
int incomingByte = 0;   // for incoming serial data  
int number;
int pin;  
static char buffer[20];
int count;



void setup() 
{
  Setpoint = 300;
  Input = analogRead(0);
  // Define que o servo esta ligado a porta 9
  Serial.begin(9600);      // open the serial port at 9600 bps:
  pinMode(3, OUTPUT);          // sets the digital pin 13 as output
  pinMode(5, OUTPUT);          // sets the digital pin 13 as output
  count = 0;
  int number;
  myPID.SetMode(AUTOMATIC);

  myPID.SetOutputLimits(-255, 255);

  
}

void loop(){
  // Le o valor do potenciometro (valores entre 0 e 1023) 
  Input = analogRead(potpin);
  number = 0;
  
  
  // send data only when you receive data:
  if (Serial.available() > 0) {
    int c = Serial.read();
        if (c == '\n') {           // received complete line
            buffer[count] = '\0';  // terminate the string
            count = 0;
            number = atoi(buffer);
            Serial.print(number);
            Setpoint = map(number,-360,360,0,1023);
            
        }
        else if (count < sizeof buffer - 1) {
            buffer[count++] = c;
        } 
    }
    myPID.Compute();
    if(Output < 0){
    pin = 5; 
    }
    else{
      pin = 3;  
    }
//    Serial.print(Setpoint);
    analogWrite(pin, Output);
    delay(20);
    analogWrite(pin, 0);
    
      

}





