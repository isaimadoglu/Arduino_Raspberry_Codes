#define potPin A0
const int leftForward = 8; 
const int leftBackward = 9; 
const int rightForward = 10; 
const int rightBackward = 11;
int potValue;

void setup() 
{
  pinMode(leftForward , OUTPUT);
  pinMode(leftBackward , OUTPUT);
  pinMode(rightForward , OUTPUT);
  pinMode(rightBackward , OUTPUT);
  pinMode(potPin, INPUT);
}
void loop()
{
  potValue=analogRead(potPin);
  potValue=map(potValue,0,1023,0,255);
  
  if(potValue >= 0 && potValue <= 49){
  //go forward
  digitalWrite(leftForward , HIGH);
  digitalWrite(leftBackward , LOW);
  digitalWrite(rightForward , HIGH);
  digitalWrite(rightBackward , LOW);
  };

  if(potValue >= 50 && potValue <= 99){
  //go backward for 5sec
  digitalWrite(leftForward , LOW);
  digitalWrite(leftBackward , HIGH);
  digitalWrite(rightForward , LOW);
  digitalWrite(rightBackward , HIGH);
  };

  if(potValue >= 100 && potValue <= 149){
  //go Left for 5sec
  digitalWrite(leftForward , HIGH);
  digitalWrite(leftBackward , LOW);
  digitalWrite(rightForward , LOW);
  digitalWrite(rightBackward , LOW);
  };
  
  if(potValue >= 150 && potValue <= 199){
  //go Right for 5sec
  digitalWrite(leftForward , LOW);
  digitalWrite(leftBackward , LOW);
  digitalWrite(rightForward , HIGH);
  digitalWrite(rightBackward , LOW);
  };

  if(potValue >= 200 && potValue <= 255){
  //Stop for 5sec
  digitalWrite(leftForward , LOW);
  digitalWrite(leftBackward , LOW);
  digitalWrite(rightForward , LOW);
  digitalWrite(rightBackward , LOW);
  };

 }
