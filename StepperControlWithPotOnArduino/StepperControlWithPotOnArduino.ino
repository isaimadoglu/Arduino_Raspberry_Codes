
#include <Stepper.h>

#define motorSteps 200     // change this depending on the number of steps
                           // per revolution of your motor
#define motorPin1 8
#define motorPin2 9
#define motorPin3 10
#define motorPin4 11
#define potPin A0
#define ledPin 13
int forward=200;
int potValue=0;

// initialize of the Stepper library:
Stepper myStepper(motorSteps, motorPin1,motorPin2,motorPin3,motorPin4); 

void setup() {
  
  // set the motor speed at 60 RPMS:
  myStepper.setSpeed(60);
  pinMode(potPin,INPUT);
  
  // Initialize the Serial port:
  Serial.begin(9600);

  
}

void loop() {

  potValue=analogRead(potPin);
  potValue=map(potValue,0,1023,100,200);
  if(potValue<=70){
    potValue=50;
  }
  Serial.println(potValue);
  // Step forward 100 steps:
  myStepper.step(forward);
  delay(potValue);

}
