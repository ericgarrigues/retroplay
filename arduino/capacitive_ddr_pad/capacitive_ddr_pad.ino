#include <CapacitiveSensor.h>

//7000 ohms with aluminium foil. 5000 with copper.

#define SERIAL_SPEED 115200
#define SERIAL_DELAY 10

CapacitiveSensor   arrow1 = CapacitiveSensor(8,A0);
CapacitiveSensor   arrow2 = CapacitiveSensor(8,A1);
CapacitiveSensor   arrow3 = CapacitiveSensor(8,A2);
CapacitiveSensor   arrow4 = CapacitiveSensor(8,A3);
CapacitiveSensor   arrow5 = CapacitiveSensor(8,A4);
CapacitiveSensor   arrow6 = CapacitiveSensor(8,A5);

void setup()                    
{

   Serial.begin(SERIAL_SPEED);

}

void loop()                    
{
    long start = millis();
    long total1 =  arrow1.capacitiveSensor(30);
    long total2 =  arrow2.capacitiveSensor(30);
    long total3 =  arrow3.capacitiveSensor(30);
    long total4 =  arrow4.capacitiveSensor(30);
    long total5 =  arrow5.capacitiveSensor(30);
    long total6 =  arrow6.capacitiveSensor(30);
    
    Serial.print(total1);
    Serial.print(";");
    Serial.print(total2);
    Serial.print(";");
    Serial.print(total3);
    Serial.print(";");
    Serial.print(total4);
    Serial.print(";");
    Serial.print(total5);
    Serial.print(";");
    Serial.print(total6);
    Serial.print("\n");

    delay(SERIAL_DELAY); 
}
