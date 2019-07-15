#define ledPin 7  // Led Pin is chosen as Port 7

int brightness = 0;

void setup() {
  
  pinMode(ledPin, OUTPUT);

}

void loop() {

  delay(3);

  brightness++;

  analogWrite(ledPin, brightness);

  if(brightness == 255)
  brightness = brightness%255;
  
}
