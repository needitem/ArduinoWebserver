#pragma once

#include "MyServo.h";
#include "RgbLed.h";
#include "buzzer.h";
#include "StringTok.h";
#include "LightSensor.h";
#include "Voltmeter.h";

class ArduinoHub {

public:
  ArduinoHub(void) {}
  ~ArduinoHub() {}

  void setup(void) {
    m_myservo.setup();
    m_buzzer.setup();
    m_rgbLed.setup();
  };

  void start(void) {
    while (1) {

      m_stInput.appendSerial();
      if (m_stInput.hasLine())  // 명령어 정상 입력
      {
        exeCmd();  // 명령어 실행
      }
    }
  }

  void exeCmd(void) {
    // 0. 명령어 끝은 엔터(\n)로 끝남
    //Serial.println("input = [" + m_stInput.toString() + "]");
    String sToken = m_stInput.cutToken().toString();

    //Serial.println("token #1 = [" + sToken + "]");
    if (sToken == "get") exeGet();
    else if (sToken == "set") exeSet();
    else m_stInput.cutLine();  // 잘못된 명령 -> 현재 줄을 삭제
  }

  void exeGet(void) {  // Get 명령어 실행
                       // 1. 전압 읽기 : get(#1) volt(#2)
    String sToken = m_stInput.cutToken().toString();
    // Serial.println("token #2 = [" + sToken + "]");
    if (sToken == "volt") exeVolt();
    else if (sToken == "light") exeLight();
    else m_stInput.cutLine();
  }

  void exeVolt(void) {
    double volt = m_voltmeter.getVolt();
    Serial.println(String(volt, 10));  // Serial에 출력
  }

  void exeLight(void) {
    int nLight = m_lightsensor.getLightStep();
    Serial.println("\nlight = " + String(nLight));
    int nLightState = m_lightsensor.getLightState();
    Serial.println("light state = " + String(nLightState));
    Serial.println("light state = " + m_lightsensor.lightStateToStr(nLightState));
  }

  void exeSet(void) {  // Set 명령어 실행

    String sToken = m_stInput.cutToken().toString();

    if (sToken == "servo") exeServo();
    else if (sToken == "led") exelight();
    else if (sToken == "buzzer") exebuzzer();
    else m_stInput.cutLine();
  }

  void exeServo(void) {
    String sToken = m_stInput.cutToken().toString();
    m_myservo.move(sToken.toInt());
  }

  void exelight(void) {
    String sToken = m_stInput.cutToken().toString();
    if (sToken == "RED") {
      m_rgbLed.turnRed(true);
      m_rgbLed.turnGreen(false);
      m_rgbLed.turnBlue(false);
    } else if (sToken == "GREEN") {
      m_rgbLed.turnRed(false);
      m_rgbLed.turnGreen(true);
      m_rgbLed.turnBlue(false);
    } else if (sToken == "BLUE") {
      m_rgbLed.turnRed(false);
      m_rgbLed.turnGreen(false);
      m_rgbLed.turnBlue(true);
    } else if (sToken == "YELLOW") {
      m_rgbLed.turnRed(true);
      m_rgbLed.turnGreen(true);
      m_rgbLed.turnBlue(false);
    } else if (sToken == "BLACK") {
      m_rgbLed.turnRed(false);
      m_rgbLed.turnGreen(false);
      m_rgbLed.turnBlue(false);
    } else if (sToken == "PINK") {
      m_rgbLed.turnRed(true);
      m_rgbLed.turnGreen(false);
      m_rgbLed.turnBlue(true);
    } else if (sToken == "CYAN") {
      m_rgbLed.turnRed(false);
      m_rgbLed.turnGreen(true);
      m_rgbLed.turnBlue(true);
    } else if (sToken == "WHITE") {
      m_rgbLed.turnRed(true);
      m_rgbLed.turnGreen(true);
      m_rgbLed.turnBlue(true);
    } else m_stInput.cutLine();
  }

  void exebuzzer(void) {
    String sToken = m_stInput.cutToken().toString();
    if (sToken == "DO") exeDelay(523);
    else if (sToken == "RE") exeDelay(587);
    else if (sToken == "MI") exeDelay(659);
    else if (sToken == "FA") exeDelay(698);
    else if (sToken == "SOL") exeDelay(784);
    else if (sToken == "LA") exeDelay(880);
    else if (sToken == "SI") exeDelay(988);
  }

  void exeDelay(int tok) {
    String sToken = m_stInput.cutToken().toString();
    m_buzzer.play(tok, sToken.toInt());
  }



private:
  StringTok m_stInput;
  Voltmeter m_voltmeter;
  LightSensor m_lightsensor;
  MyServo m_myservo;
  RgbLed m_rgbLed;
  buzzer m_buzzer;
};