int analogPin = A0;    // potentiometer wiper (middle terminal) connected to analog pin 3
               // outside leads to ground and +5V
int val = 0;    // variable to store the value read
float V = 0;
int X;
void setup() {
  Serial.begin(9600);    //  setup serial
  pinMode(13, OUTPUT);
}

void loop() {
  val = analogRead(analogPin);    // read the input pin
  Serial.print ("Conversion analogico-digital: ");
  Serial.println(val);    // debug value
  V = val*5/1023.0;
  Serial.print ("El voltaje analogico es: ");
  Serial.println(V);
  X = map(val, 0, 1023, 0, 255);
  analogWrite(13, X);
  //Realizar los cambios necesarios para que el LED encienda si y s ́olo si el voltaje que entra al puerto A0es mayor a 3V.
//  if(V > 3){
//    digitalWrite(13, HIGH);
//  } else{
//    digitalWrite(13, LOW);
//  }
//  delay(1000);
  //Realizar los cambios necesarios para que el LED encienda con una intensidad proporcional al voltajede entrada en el puerto A0 desde 0 hasta 5V. Utilizar la funci ́onAnalogWrite().
 // analogWrite(13, val/1023*255);
}
