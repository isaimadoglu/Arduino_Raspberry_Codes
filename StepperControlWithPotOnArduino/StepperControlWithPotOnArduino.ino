#include <Stepper.h>

#define motorAdimi 200     
                           
#define motorPin1 8
#define motorPin2 9
#define motorPin3 10
#define motorPin4 11
#define potPin A0

int ileri=200;
int potValue=0;


Stepper stepMotor(motorAdimi, motorPin1,motorPin2,motorPin3,motorPin4); 

void setup() {
  
  
  stepMotor.setSpeed(60);
  pinMode(potPin,INPUT);
  
  
  Serial.begin(9600);

  
}

void loop() {

  potValue=analogRead(potPin);
  potValue=map(potValue,0,1023,100,200);
  if(potValue<=70){
    potValue=50;
  }
  Serial.println(potValue);
  stepMotor.step(ileri);
  
}
