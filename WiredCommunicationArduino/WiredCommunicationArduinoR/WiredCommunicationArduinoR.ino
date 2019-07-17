
int ledValue=0;
#define ledPin 9

void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  while(Serial.available()>0){
    ledValue=Serial.parseInt();
    if(Serial.read()=='\n') break;
  }
  analogWrite(ledPin,ledValue);
  Serial.println(ledValue);
}
