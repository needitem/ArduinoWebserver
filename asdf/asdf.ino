#include "ArduinoHub.h"
#include <Servo.h>

#define SERIAL_RATE 9600

ArduinoHub arduinoHub;
/**
 * 명령어들
 * 1. get volt
 * 2. get light
 * 3. set servo #pos
 * 4. set led color (color: text) ex) red, green, blue, 
 * 5. set buzzer note #delay
 * 
*/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(SERIAL_RATE);
  arduinoHub.setup();
}

void loop() {
  arduinoHub.start();
  //arduinoHub.motorTest();
  //m_motor.toggleMotor();
}
