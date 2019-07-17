#include <Servo.h>
Servo ESC;
int potValue=0, potMap = 0;
#define potPin A0


void setup() {
  // Attach the ESC on pin 9
  Serial.begin(9600);
  ESC.attach(9); // (pin, min pulse width, max pulse width in microseconds)
  ESC.writeMicroseconds(0); // 
  delay(1000); 
  ESC.writeMicroseconds(1100); 

}
void loop() {
  potValue = analogRead(potPin);   // reads the value of the potentiometer (value between 0 and 1023)
  
  potMap = map(potValue, 0, 1023, 1550, 2000);   // scale it to use it with the servo library (value between 0 and 180)
  Serial.println(potMap);
  ESC.writeMicroseconds(potMap);    // Send the signal to the ESC
}
