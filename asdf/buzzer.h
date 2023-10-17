#pragma once

int note[] = {2093, 2349, 2637, 2794, 3136, 3520, 3951, 4186}; //C, D, E, F, G, A, B, C

class buzzer
{
    public:
        buzzer(){

        }
        ~buzzer(){

        }

        void beep(int frequency, int duration){
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
                
        void setup(int port){
            this->port = port;
            pinMode(port, OUTPUT);
        }
        
    private:
        int port;


};