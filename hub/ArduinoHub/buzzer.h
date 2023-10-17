#pragma once

#define DEF_BUZZER_PORT	(4)

enum NoteType
{
	DO = 523, RE = 587, MI = 659, FA = 698, SOL = 784, LA = 880, SI = 988
};

class buzzer
{
public:
	buzzer(void) { setPort(DEF_BUZZER_PORT); }
	~buzzer() {}

	void setPort(int nPort) { m_nPort = nPort; }
	void setup(void) { initBuzzer(); }
	void play(int nNote, int nTime)
	{
		tone(m_nPort, nNote, nTime);
		delay(nTime);
	}

private:
	int m_nPort;

	void initBuzzer(void)
	{
		pinMode(m_nPort, OUTPUT);
	}
};