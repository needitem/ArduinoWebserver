#pragma once

#define DEF_PORT_R	(5)
#define DEF_PORT_G	(6)
#define DEF_PORT_B	(7)
#define RED_BIT (1) // 001
#define GREEN_BIT (2) // 010
#define BLUE_BIT (4) // 100

enum ColorType{
	BLACK = 0,
	RED=1,
	GREEN=2,
	YELLOW=3,
	BLUE=4,
	PINK=5,
	CYAN=6,
	WHITE=7
};


class RgbLed
{
public:
	RgbLed(void) { setPort(DEF_PORT_R, DEF_PORT_G, DEF_PORT_B); } // ������
	~RgbLed() {}	// �Ҹ���, �ı���
	void setup(void){initLed();}
	void setPort(int nPortR, int nPortG, int nPortB)
	{
		m_nPortR = nPortR, m_nPortG = nPortG, m_nPortB = nPortB;
	}

	void turnRgb(int nColor){
		int nR = nColor & RED_BIT;
		int nG = nColor & GREEN_BIT;
		int nB = nColor & BLUE_BIT;
		
		digitalWrite(DEF_PORT_R, (nR) ? true : false);
		digitalWrite(DEF_PORT_G, (nG) ? true : false);
		digitalWrite(DEF_PORT_B, (nB) ? true : false);
	}

  void turnRed(bool bOn)
	{
		if (bOn) digitalWrite(m_nPortR, HIGH);
		else digitalWrite(m_nPortR, LOW);
	}
	void turnGreen(bool bOn)
	{
		if (bOn) digitalWrite(m_nPortG, HIGH);
		else digitalWrite(m_nPortG, LOW);
	}
	void turnBlue(bool bOn)
	{
		if (bOn) digitalWrite(m_nPortB, HIGH);
		else digitalWrite(m_nPortB, LOW);
	}
  
  
	void turnSevenLed(){
		for(int i=0;i<=7;i++){
			turnRgb(i);
			delay(1000);
		}
	}

private:
	int m_nPortR, m_nPortG, m_nPortB; // RGB ��Ʈ
	initLed(void){
		pinMode(m_nPortR, OUTPUT);
		pinMode(m_nPortG, OUTPUT);
		pinMode(m_nPortB, OUTPUT);
	}	
};