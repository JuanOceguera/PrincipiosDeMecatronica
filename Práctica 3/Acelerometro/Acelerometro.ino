#include<LiquidCrystal.h>    // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);    // initialize the interface pins

int analogPinX = A12;
int analogPinY = A13;
int analogPinZ = A14;
float gx, gy, gz, roll, pitch;

void setup() {
  pinMode(A11, OUTPUT);
  pinMode(A15, OUTPUT);
  digitalWrite(A15, LOW);
  analogWrite(A11, 169);
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows:
  Serial.begin(9600);
}

void loop() {
  gx = (analogRead(analogPinX)-339)/67.5;
  gy = (analogRead(analogPinY)-334)/67.5;
  gz = (analogRead(analogPinZ)-273)/67.5;
  Serial.print ("Gx: ");
  Serial.println(gx);
  Serial.print ("Gy: ");
  Serial.println(gy);
  Serial.print ("Gz: ");
  Serial.println(gz);
  roll = 180-atan2(-gx, gz)*57.3*-1*2;
  if(roll > 359){
    roll = 0;
  }
  pitch = 180-atan2(gy,sqrt(gx*gx+gz*gz))*57.3*2;
  if(pitch > 359){
    roll = 0;
  }
  Serial.print ("Roll: ");
  Serial.println(roll);
  Serial.print ("Pitch: ");
  Serial.println(pitch);
  //Serial.print ("Vertical: ");
  //Serial.println(90+atan2(sin(atan2(-gx, gz)),tan(atan2(gy,sqrt(gx*gx+gz*gz))))*57.3);
  lcd.setCursor(4, 0);
  lcd.print ("Angulo:");
  lcd.setCursor(5, 1);
  lcd.print(90+atan2(sin(atan2(-gx, gz)),tan(atan2(gy,sqrt(gx*gx+gz*gz))))*57.3);
  delay(1000);
}
