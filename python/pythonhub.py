from serial import Serial
import time
import os

os.environ["PYTHONUNBUFFERED"] = "1"


class PythonHub:
    def __init__(self, comPort="/dev/ttyACM0", baudrate=9600, timeout=1):
        try:
            self.ser = Serial(comPort, baudrate, timeout=timeout)
            self.clearSerial()
            self.clearVoltTuple()

        except:
            print("Failed to open serial port:", comPort)
            print("Please check the port name and try again.")
            exit(1)

        print("Serial port:", self.ser.name)

    def writeSerial(self, *args):
        sCmd = " ".join(args) + "\n"

        # debug input
        print("Sending:", sCmd)

        self.ser.write(sCmd.encode())
        time.sleep(1)
        nRead = self.ser.inWaiting()
        if nRead > 0:
            data = self.ser.read(nRead)
            print("Received:", data.decode())
            return data.decode()

    def talk(self):
        while True:
            sCmd = input("Enter command or 'exit':")
            if sCmd == "exit":
                break
            elif sCmd == "help":
                self.help()
            else:
                try:
                    self.writeSerial(sCmd)
                    self.clearSerial()
                except:
                    print("Failed to send command:", sCmd)
                    print("Please check the command and try again.")

    def clearSerial(self):
        self.ser.flushInput()
        self.ser.flushOutput()

    def run(self):
        self.talk()

    def close(self):
        self.ser.close()

    def __del__(self):
        self.close()

    def help(self):
        print("PythonHub Commands:")
        print("  get volt")
        print("  get light")
        print("  set servo <angle>")
        print("  set led <color>")
        print("  set buzzer <freq> <duration>")

    def getVolt(self):
        try:
            volt = self.writeSerial("get", "volt")
            volt = float(volt)
            return volt
        except:
            pass

    def getLight(self):
        try:
            light = self.writeSerial("get", "light")
            light = float(light)
            print("Received: ", light)
            return light
        except:
            pass

    def setServo(self, angle):
        try:
            self.writeSerial("set", "servo", str(angle))
        except:
            pass

    def setLed(self, color):
        try:
            self.writeSerial("set", "led", color)
        except:
            print("Failed to set LED color:", color)

    def setBuzzer(self, freq, duration):
        try:
            self.writeSerial("set", "buzzer", str(freq), str(duration))
        except:
            pass

    def addVoltTuple(self):
        volt = self.getVolt()
        voltTime = time.time()
        if volt >= 0:
            self.volts += (volt,)
            self.voltTimes += (voltTime,)
            return True
        else:
            print("Failed to get voltage reading.")
            print("Please check the sensor connection.")
            return False

    def clearVoltTuple(self):
        self.volts = ()
        self.voltTimes = ()


    def printVoltTuple(self):
        for volt, times in zip(self.volts, self.voltTimes):
            print(f"volt: {volt:.2f}V, time: {time.ctime(times)}")
