#include <Servo.h>
#include<LiquidCrystal.h>    // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);    // initialize the interface pins
Servo myservo;// create servo object to control a servo

int val = 0;// variable to read the value from the analog pin
int analogPin = A0;
float V = 0;
float ang = 0;

void setup() {
  myservo.attach(9);// attaches the servo on pin 9 to the servo 
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows:
}

void loop() {
//  for (int i = 0; i <= 180; i++)
//  {
//    myservo.write(i);// sets the servo position according to the scaled value
//    delay(20);// waits for the servo to get there
//  }
//  for (int i = 180; i >= 0; i--)
//  {
//    myservo.write(i);// sets the servo position according to the scaled value
//    delay(20);// waits for the servo to get there
//  }
  
 //Seguir al potenciómetro
  val = analogRead(analogPin);
  ang = map(val, 0, 1023, 0, 180);
  myservo.write(ang);
  delay(20);

  //Mostrar en LCD
  V = map(val, 0, 1023, 0, 5);
  lcd.setCursor(0, 0);
  lcd.print ("Voltaje: ");
  lcd.setCursor(9, 0);
  lcd.print(V);
  lcd.setCursor(2, 1);
  lcd.print ("Angulo: ");
  lcd.setCursor(8, 1);
  lcd.println(ang);
}
