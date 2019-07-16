#define potPin A0
#define transistorPin 3

int potValue = 0;
int potMap = 0;

void setup()
{

pinMode(potPin,INPUT);
pinMode(transistorPin, OUTPUT);

}

void loop()
{

potValue = analogRead(potPin)/4;

potMap = map(potValue, 0, 1023, 0, 255);

analogWrite(transistorPin, potMap);

 }
