#include <PID_v1.h>

double Setpoint;
double Input;
double Output;
PID myPID(&Input, &Output, &Setpoint, 0.4, 0, 0, DIRECT);


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
  Setpoint = 920;
  Input = analogRead(0);
  // Define que o servo esta ligado a porta 9
  Serial.begin(9600);      // open the serial port at 9600 bps:
  pinMode(3, OUTPUT);          // sets the digital pin 13 as output
  pinMode(5, OUTPUT);          // sets the digital pin 13 as output
  count = 0;
  int number;
  myPID.SetMode(AUTOMATIC);
  
}

void loop(){
  // Le o valor do potenciometro (valores entre 0 e 1023) 
  Input = analogRead(potpin);
  number = 0;
  myPID.Compute();
  Serial.print(Output);
  if (Output< 0){
    pin = 5;
    Output = -Output;
    }
  else{
    pin = 3;
    }
  analogWrite(pin, Output);
  delay(20);
  analogWrite(pin, 0); 

  
  // send data only when you receive data:
  if (Serial.available() > 0) {
    int c = Serial.read();
        if (c == '\n') {           // received complete line
            buffer[count] = '\0';  // terminate the string
            count = 0;
            number = atoi(buffer);
            if(number < 0){
//              Serial.write('n');
              pin = 5;
              number = -number;
            }
            else{
//              Serial.write('p');
              pin = 3;
            }
            
            number = map(number, -360, 360, 0, 255);
//            analogWrite(pin, number);
//            delay(20);
//            analogWrite(pin, 0); 
        }
        else if (count < sizeof buffer - 1) {
            buffer[count++] = c;
        }
}}





