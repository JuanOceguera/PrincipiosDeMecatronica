#include<LiquidCrystal.h>    // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);    // initialize the interface pins

int analogPin = A2;
float val;

void setup() {
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows:
  Serial.begin(9600);
}

void loop() {
  val = map(analogRead(analogPin), 0, 1023, 0, 500)/10.0+9.7;
  lcd.setCursor(0, 0);
  lcd.print ("Temperatura [C]");
  lcd.setCursor(5, 1);
  lcd.print(val);
  Serial.print(analogRead(analogPin));
  Serial.print("\t");
}
