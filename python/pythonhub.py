from serial import Serial
import time
import os
os.environ['PYTHONUNBUFFERED'] = '1'

class PythonHub:
    def __init__(self, comPort='COM3', baudrate=9600, timeout=1):
        try:
            self.ser = Serial(comPort, baudrate, timeout=timeout)
        except:
            print("Failed to open serial port:", comPort)
            print("Please check the port name and try again.")
            exit(1)
            
        print("Serial port:", self.ser.name)
    
    def writeSerial(self, *args):
        sCmd = ' '.join(args) + '\n'
        
        #debug input
        print("Sending:", sCmd)

        self.ser.write(sCmd.encode())
        time.sleep(1)
        nRead = self.ser.inWaiting()
        if nRead > 0:
            data = self.ser.read(nRead)
            print("Received:", data.decode())

    def talk(self):
        while True:
            sCmd = input("Enter command or 'exit':")
            if sCmd == 'exit':
                break
            else:
                self.writeSerial(sCmd)

    def run(self):
        self.talk()

    def close(self):
        self.ser.close()
