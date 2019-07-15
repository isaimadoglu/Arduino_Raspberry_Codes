int ledPin = 7;

int brightness = 0;

void setup() {

  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  delay(3);

  brightness++;

  analogWrite(ledPin, brightness);
  
  Serial.println(brightness);

  if(brightness == 255)
  brightness = brightness%255;
  
}
