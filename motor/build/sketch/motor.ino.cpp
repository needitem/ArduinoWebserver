#include <Arduino.h>
#line 1 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino"
#include <Servo.h>
#include "motor.h"
#include "light.h"
#include "buzzer.h"

Servo servo;
motor _motor;
light _light;
buzzer _buzzer;

int cnt;

#line 13 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino"
void setup();
#line 17 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino"
void loop();
#line 13 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino"
void setup() {
  _motor.setup();
}

void loop() {

  if(cnt % 1000 == 0) //every 1 second
  {
    //_light.setEveryColorbyNumber(cnt/1000);
    _motor.toggleMotor();
    //_buzzer.playEveryTonebyNumber(cnt/1000);
  }
  cnt++;
  delay(1);

}

