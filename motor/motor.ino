#include <Servo.h>
#include "motor.h"
#include "light.h"
#include "buzzer.h"

Servo servo;
motor _motor;
light _light;
buzzer _buzzer;

int cnt;

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
