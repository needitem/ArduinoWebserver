#pragma once
#define DEAFULT_LIGHT_PORT_RED (4)
#define DEAFULT_LIGHT_PORT_GREEN (5)
#define DEAFULT_LIGHT_PORT_BLUE (6)

int everyColor[][3] = {
    {0, 0, 0},
    {255, 0, 0},
    {0, 255, 0},
    {0, 0, 255},
    {255, 255, 0},
    {0, 255, 255},
    {255, 0, 255},
    {255, 255, 255}
};

class light
{
    public:
        light(){
            initLight();
        }
        ~light(){

        }

        void setRed(int red){
            digitalWrite(portRed, red);
        }
        void setGreen(int green){
            digitalWrite(portGreen, green);
        }
        void setBlue(int blue){
            digitalWrite(portBlue, blue);
        }
        void setRGB(int red, int green, int blue){
            setRed(red);
            setGreen(green);
            setBlue(blue);
        }

        void setEveryColor(){
            for (int i = 0; i < 8; i++)
            {
                setRGB(everyColor[i][0], everyColor[i][1], everyColor[i][2]);
            }
        }

        void setEveryColorbyNumber(int number){
            setRGB(everyColor[number%7][0], everyColor[number%7][1], everyColor[number%7][2]);
        }
    private:
        int portRed = DEAFULT_LIGHT_PORT_RED;
        int portGreen = DEAFULT_LIGHT_PORT_GREEN;
        int portBlue = DEAFULT_LIGHT_PORT_BLUE;
                
        void initLight(){
            pinMode(portRed, OUTPUT);
            pinMode(portGreen, OUTPUT);
            pinMode(portBlue, OUTPUT);
        }

};