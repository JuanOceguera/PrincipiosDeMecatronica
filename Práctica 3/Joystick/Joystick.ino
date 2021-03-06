#define joyX A0
#define joyY A1

float xValue;
float yValue;
void setup() {
  Serial.begin(9600);
}

void loop() {
  xValue = map(analogRead(joyX), 0, 1023, -10, 10)/10.0;
  yValue = map(analogRead(joyY), 0, 1023, -10, 10)/10.0;
  Serial.print(xValue);
  Serial.print("\t");
  Serial.println(yValue);
}
