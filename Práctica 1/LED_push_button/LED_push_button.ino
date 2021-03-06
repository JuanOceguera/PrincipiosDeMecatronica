void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, INPUT);
}

void loop()
{
  if(digitalRead(12) == HIGH){
    digitalWrite(13, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(13, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
  }
  else {
    digitalWrite(13, HIGH);
    delay(500); // Wait for 1000 millisecond(s)
    digitalWrite(13, LOW);
    delay(500); // Wait for 1000 millisecond(s) 
  }
}
