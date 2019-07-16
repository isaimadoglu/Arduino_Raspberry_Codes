#include <Servo.h>
Servo servo_motor;
#define pot_pin A0
#define servo_pin A1
int potValue=0,potMap=0;

void setup() 
{
  pinMode(pot_pin,INPUT);
  servo_motor.attach(servo_pin);

}

void loop() 
{
  potValue=analogRead(pot_pin);
  potMap=map(potValue, 0 , 1023, 0 , 180);
  servo_motor.write(potMap);
  delay(3);

}
