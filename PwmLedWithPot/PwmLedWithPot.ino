#define potantiometerPin A0
#define ledPin 2

int potValue = 0;
int potMap = 0;

void setup() {

  pinMode(potantiometerPin, INPUT);
  pinMode(ledPin, OUTPUT);

  Serial.println(9600);
}

void loop() {

  potValue = analogRead(potantiometerPin);
  
  delay(2);

  // We map the value came from potantiometer between 0 and 255 here:
  potMap = map(potValue, 0, 1023, 255, 0);

  delay(2);

  // We give the PWM signal according to the mapped value of the value came from potantiometer here:
  analogWrite(ledPin, potMap);

  Serial.println(potValue);
}
