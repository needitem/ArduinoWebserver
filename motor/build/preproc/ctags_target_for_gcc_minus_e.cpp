# 1 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino"
# 2 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino" 2
# 3 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino" 2
# 4 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino" 2
# 5 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\motor.ino" 2

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
