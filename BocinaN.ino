int pinaltvoz=13;
int frecuencia=1000;
long duracion = 5000;
void setup() {

  pinMode(pinaltvoz, OUTPUT);
  
}

void loop() {
  
  tone(pinaltvoz, frecuencia, duracion);
  delay(1000);

}
