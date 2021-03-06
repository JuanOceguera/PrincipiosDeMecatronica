#include<LiquidCrystal.h>    // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);    // initialize the interface pins

void setup() {
  lcd.begin(16, 2);    // set up the LCD's number of columns and rows:
}
void loop() {
//  lcd.setCursor(1, 0);
//  lcd.print("Principios de");// Print a message to the LCD.
//  lcd.setCursor(2, 1);
//  lcd.print("Mecatronica");
//
////Texto parpadee
//  lcd.setCursor(1, 0);
//  lcd.print("Principios de");// Print a message to the LCD.
//  lcd.setCursor(2, 1);
//  lcd.print("Mecatronica");
//  delay(750);
//  lcd.clear();
//  delay(250);

//Imprimir el nombre
  lcd.clear();
  lcd.setCursor(15,0);
  lcd.print("J");
  lcd.setCursor(15,1);
  lcd.print("O");
  delay(250);

  lcd.clear();
  lcd.setCursor(14,0);
  lcd.print("Ju");
  lcd.setCursor(14,1);
  lcd.print("Oc");
  delay(250);

  lcd.clear();
  lcd.setCursor(13,0);
  lcd.print("Jua");
  lcd.setCursor(13,1);
  lcd.print("Oce");
  delay(250);

  lcd.clear();
  lcd.setCursor(12,0);
  lcd.print("Juan");
  lcd.setCursor(12,1);
  lcd.print("Oceg");
  delay(250);

  lcd.clear();
  lcd.setCursor(11,0);
  lcd.print("Juan ");
  lcd.setCursor(11,1);
  lcd.print("Ocegu");
  delay(250);

  lcd.clear();
  lcd.setCursor(10,0);
  lcd.print("Juan M");
  lcd.setCursor(10,1);
  lcd.print("Ocegue");
  delay(250);

  lcd.clear();
  lcd.setCursor(9,0);
  lcd.print("Juan Ma");
  lcd.setCursor(9,1);
  lcd.print("Oceguer");
  delay(250);

  lcd.clear();
  lcd.setCursor(8,0);
  lcd.print("Juan Man");
  lcd.setCursor(8,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(7,0);
  lcd.print("Juan Manu");
  lcd.setCursor(7,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(6,0);
  lcd.print("Juan Manue");
  lcd.setCursor(6,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(5,0);
  lcd.print("Juan Manuel");
  lcd.setCursor(5,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(4,0);
  lcd.print("Juan Manuel");
  lcd.setCursor(4,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Juan Manuel");
  lcd.setCursor(3,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(2,0);
  lcd.print("Juan Manuel");
  lcd.setCursor(2,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("Juan Manuel");
  lcd.setCursor(1,1);
  lcd.print("Oceguera");
  delay(250);

  lcd.clear();
  lcd.print("Juan Manuel");
  lcd.setCursor(0,1);
  lcd.print("Oceguera");
  delay(2500);

}
