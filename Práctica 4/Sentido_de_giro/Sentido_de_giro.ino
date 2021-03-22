void setup()
{
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  digitalWrite(13, HIGH);
}

void loop()
{
  if(digitalRead(9) == LOW && digitalRead(10) == LOW){
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
  }
  else {
    if(digitalRead(9) == HIGH && digitalRead(10) == LOW){
      digitalWrite(12, HIGH);
      digitalWrite(11, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, HIGH);
    } else{
      if(digitalRead(9) == LOW && digitalRead(10) == HIGH){
        digitalWrite(12, LOW);
        digitalWrite(11, HIGH);
        digitalWrite(7, HIGH);
        digitalWrite(6, LOW);
      } else{
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(7, HIGH);
        digitalWrite(6, HIGH);
      }
    }
  }
}
