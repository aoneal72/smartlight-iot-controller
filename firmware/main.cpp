#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(200);
  Serial.println("Smartlight firmware boot");
}

void loop() {
  delay(1000);
  Serial.println("tick");
}
