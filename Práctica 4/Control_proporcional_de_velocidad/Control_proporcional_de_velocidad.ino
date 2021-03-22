int val = 0;
int analogPin = A0;
int ciclo = 0;
void setup()
{
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(6, OUTPUT);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
}

void loop() {
  val = analogRead(analogPin);
  ciclo = map(val, 0, 1023, 0, 255);
  digitalWrite(6, HIGH);
  if(ciclo<128){
    digitalWrite(10, LOW);
    analogWrite(11, 128 - ciclo);
  } else {
    if(ciclo>128){
      digitalWrite(11, LOW);
      analogWrite(10, ciclo - 128);
    } else{
      digitalWrite(11, LOW);
      digitalWrite(10, LOW);
    }
  }
}
