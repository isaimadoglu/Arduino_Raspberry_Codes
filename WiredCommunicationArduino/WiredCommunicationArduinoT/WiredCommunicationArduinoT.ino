#define potPin A0
int potValue=0;

void setup()
{
  pinMode(potPin,INPUT);
  Serial.begin(9600);
}

void loop()
{
  potValue=analogRead(potPin);
  potValue=map(potValue, 0 , 1023, 0, 255);
  Serial.println(potValue);
} 
