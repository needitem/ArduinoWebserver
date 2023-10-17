#line 1 "C:\\Users\\th072\\OneDrive\\바탕 화면\\수업내용\\iot\\motor\\buzzer.h"
#pragma once
#define DEAFULT_BUZZER_PORT (7)

int note[] = {2093, 2349, 2637, 2794, 3136, 3520, 3951, 4186}; //C, D, E, F, G, A, B, C

class buzzer
{
    public:
        buzzer(){
            setup();
        }
        ~buzzer(){

        }

        void beep(int duration, int frequency){
            tone(port, frequency, duration);
        }

        void playEveryNote(){
            for (int i = 0; i < 8; i++)
            {
                beep(1000, note[i]);
            }
        }

        void playEveryTonebyNumber(int number){
            beep(1000, note[number%7]);
        }

    private:
        int port = DEAFULT_BUZZER_PORT;
                
        void setup(){
            pinMode(port, OUTPUT);
        }

};