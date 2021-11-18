char inChar;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0)
  {
    inChar = Serial.read();
    if(inChar=='e')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("Светодиод включен");
    }
    else if(inChar=='d')
    {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("Светодиод выключен");
    }
  }

}
