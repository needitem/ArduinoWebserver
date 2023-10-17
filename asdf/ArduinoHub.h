#pragma once

#include "StringTok.h"
#include "buzzer.h"
#include "light.h"
#include "LightSensor.h"
#include "Voltmeter.h"
#include "motor.h"

#define SERVO_SPEED	(180./1500.) // 단위: 각도/밀리초

class ArduinoHub
{
  public:
    ArduinoHub(void)
    {
        setup();
       
    }
    ~ArduinoHub() {}

    void setup(void)
    {
        m_buzzer.setup(4);
        m_light.setup(5,6,7);
        m_voltmeter.setup(A0);
        m_lightSensor.setup(3);
    }

    void start(void)
    {
        while(1)
        {
            m_st.appendSerial();
            if (m_st.hasLine())
            {
                executeCmd();
            }
        }
    }

//-----------------command-------------------

    void executeCmd()
    {

        String sToken = m_st.cutToken().toString();

        if(sToken == "get")
        {
            execGet();
        }
        else if (sToken == "set")
        {
            execSet();
        }
        else{
            m_st.cutLine();
        }
    }

    void execGet()
    {
        String sToken = m_st.cutToken().toString();
        if(sToken == "volt")
        {
            Serial.print("volt = ");
            float voltage = getVolt();
            Serial.println(String(voltage));
        }
        else if (sToken == "light")
        {
            Serial.print("light = ");
            getLight();
        }
        else if (sToken == "servo")
        {
            Serial.print("servo = ");
            m_servo.getServoPos();
        }
        else{
            m_st.cutLine();
        }
    }

    void execSet()
    {
        String sToken = m_st.cutToken().toString();
        if(sToken == "servo")
        {
            int angle = m_st.cutToken().toInt();
            
            Serial.println("servo set to " + String(angle));
        }
        else if (sToken == "led")
        {
            String color = m_st.cutToken().toString();
            Serial.println(color);
            setLedColor(color); 
            Serial.println("led set to " + color);
        }
        else if (sToken == "buzzer")
        {
            int freq = m_st.cutToken().toInt();
            int duration = m_st.cutToken().toInt();
            setBuzzer(freq, duration);
            Serial.println("buzzer set to " + String(freq) + "Hz, " + String(duration) + "ms");
        }
        else{
            m_st.cutLine();
        }
    }

//-----------------function-------------------

    float getVolt()
    {
        return m_voltmeter.getVolt();
    }

    void getLight()
    {
        switch(m_lightSensor.getLightState())
        {
            case 350:
                Serial.println("bright");
                break;
            case 700:
                Serial.println("ambient");
                break;
            case 900:
                Serial.println("dark");
                break;
        }
    }

    void setLedColor(String color)
    {
        int tempColorNum;

       switch(color[0])
       {
           case 'r':
                tempColorNum = 1;
                break;
           case 'g':
                tempColorNum = 2;
                break;
           case 'b':
                tempColorNum = 3;
                break;

           default:
                tempColorNum = 7;
                break;
       }

        m_light.setEveryColorbyNumber(tempColorNum);
    }

    void setBuzzer(int freq, int second)
    {
        m_buzzer.beep(freq, second);
    }



    //-----------test----------------
        void ledTest()
        {
            m_light.setRed(255);
        }
    void buzzerTest()
    {
        m_buzzer.beep(1000,500);
    }
    void lightSensorTest()
    {
        m_lightSensor.getLightState();
        Serial.println(m_lightSensor.getLightState());
    }

//---------------------------------
    
  private:
    buzzer m_buzzer;
    light m_light;
    Voltmeter m_voltmeter;
    LightSensor m_lightSensor;
    StringTok m_st;
    motor m_servo;

};