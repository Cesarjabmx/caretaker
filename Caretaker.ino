#include "Servo.h"
#include "DHT.h"  //Añadimos la libreria con la cual trabaja nuestro sensor
#define DHTPIN 8     // Indicamos el pin donde conectaremos la patilla data de nuestro sensor
#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);  //Indica el pin con el que trabajamos y el tipo de sensor

Servo x, y;
int width = 640, height = 480;  // total resolution of the video
int xpos = 90, ypos = 90;  // initial positions of both Servos

int pinaltvoz=13;
int frecuencia=1000;
long duracion = 5000;
void setup() {

  //Inicio comunicacion serie 
  Serial.begin(9600); 

  x.attach(9);
  y.attach(10);

  x.write(xpos);
  y.write(ypos);

  //Mensaje de inicio
  Serial.println("Sensor DHTR11:");
  //Iniciamos el sensor
  dht.begin();

  pinMode(pinaltvoz, OUTPUT);
  
}

const int angle = 2;   // degree of increment or decrement


void loop() {


  if (Serial.available() > 0)
  {

    int x_mid, y_mid;
    if (Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();  // read center x-coordinate
      if (Serial.read() == 'Y')
        y_mid = Serial.parseInt(); // read center y-coordinate
    }

    if (x_mid > width / 2 + 30)
      xpos += angle;
    if (x_mid < width / 2 - 30)
      xpos -= angle;
    if (y_mid < height / 2 + 30)
      ypos -= angle;
    if (y_mid > height / 2 - 30)
      ypos += angle;


     // if the servo degree is outside its range
    if (xpos >= 180)
      xpos = 180;
    else if (xpos <= 0)
      xpos = 0;
    if (ypos >= 180)
      ypos = 180;
    else if (ypos <= 0)
      ypos = 0;

    x.write(xpos);
    y.write(ypos);

    //used for testing
    Serial.print("\t");
    Serial.print(x_mid);
    Serial.print("\t");
    Serial.println(y_mid);

    } 


  int h = dht.readHumidity();  //Guarda la lectura de la humedad en la variable float h
  int t = dht.readTemperature();  //Guarda la lectura de la temperatura en la variable float 
  

  Serial.print("Humedad relativa: "); 
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: "); 
  Serial.print(t);
  Serial.println(" *C");


   if (t>=34)
  {
    Serial.print("TEMPERATURA ALTA");
    Serial.print(" %\t");
    tone(pinaltvoz, frecuencia, duracion);
    delay(1000);
  }
  else {
    //delay(1000);
    Serial.print("TODO OK");
    Serial.print(" \t");
  }



}