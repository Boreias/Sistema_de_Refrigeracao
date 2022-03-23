#define ventilador1 2
#define ventilador2 3
#define ventilador3 4
#define ventilador4 5
#define ventilador5 6
#define ventilador6 7
#define ventilador7 8
#define ventilador8 9
#define ventilador9 10

const int sensor_temp = A0;
int ventiladores[9] = {ventilador1,
                       ventilador2,
                       ventilador3,
                       ventilador4,
                       ventilador5,
                       ventilador6,
                       ventilador7,
                       ventilador8,
                       ventilador9};
float temperatura;
int temperaturaLigar = 25; //Seria obtido a partir do backend
int i;
bool ligado;


void setup()
{
  for(i=0; i<9; i++){
    pinMode(ventiladores[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop()
{
  temperatura = (float(analogRead(sensor_temp)) * 5 / 1023) / 0.01;
  Serial.print("Temperatura: ");
  Serial.println(temperatura);
  delay(50);

  if(temperatura<temperaturaLigar){
    for(i=0; i<9; i++){
      digitalWrite(ventiladores[i], LOW);
      ligado = false;
    }
  } else {
    for(i=0; i<9; i++){
      digitalWrite(ventiladores[i], HIGH);
      ligado = true;
    }
  }
}
