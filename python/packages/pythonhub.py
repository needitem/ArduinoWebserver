from serial import Serial
import time
import os
import packages.db as db
import statistics as st
import matplotlib.pyplot as plt
import pandas as pd
from pandasql import sqldf

os.environ["PYTHONUNBUFFERED"] = "1"


class PythonHub:
    def __init__(self, comPort="/dev/ttyACM0", baudrate=9600, timeout=1):
        try:
            self.ser = Serial(comPort, baudrate, timeout=timeout)
            self.clearSerial()
            self.dbObj = db.db()
            self.volts = ()
            self.voltTimes = ()
            self.lights = ()
            self.lightsteps = ()
            self.lightTimes = ()
            self.temp = ()
            self.tempTimes = ()
        except:
            print("Failed to open serial port:", comPort)
            print("Please check the port name and try again.")
            exit(1)

        print("Serial port:", self.ser.name)
#------------------------------Serial---------------------------------
    def writeSerial(self, *args):
        sCmd = " ".join(args) + "\n"

        # debug input
        print("Sending:", sCmd)

        self.ser.write(sCmd.encode())
        time.sleep(0.1)
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

    def __del__(self):
        self.ser.close()


#-----------------------------------------------------------------------------
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
        
        
#-------------------volt------------------------------------

    def getVolt(self):
        try:
            self.clearSerial()
            volt = float(self.writeSerial("get","volt"))
            return volt
        except Exception as e:
            print("An error occurred: ", e)
            pass
    def saveVoltToDB(self):
        try:
            volt = self.getVolt()
            times = int(time.time())
            self.dbObj.insertData("volt_table", times, volt)
            return volt
            
        except:
            return "Fail"
        
    def samplingVoltandSaveToTuple(self, delay, count):
        for i in range(count):
            try:
                self.volts += (float(self.getVolt()),)
                self.voltTimes += (int(time.time()),)
                time.sleep(delay)
            except:
                continue
            
    def loadFromDB(self):
        for row in self.dbObj.selectData("volt_table"):
            #add values in self.volt and self.time
            self.volts += (row[1],)
            self.voltTimes += (row[0],)
        
    def saveVoltTuplesToDB(self):
        for volt, voltTime in zip(self.volts, self.voltTimes):
            self.dbObj.insertData("volt_table", voltTime, volt)
            
    def countVoltDB(self):
        return self.dbObj.countTable("volt_table")
        
    def addVoltTuple(self):
        volt = float(self.getVolt())
        voltTime = time.time()
        if volt >= 0:
            self.volts += (float(volt),)
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
            print(f"volt: {float(volt):.2f}V, time: {time.ctime(times)}")
            
    def getVoltMean(self):
        print("Mean: ", st.mean(self.volts))
        return st.mean(self.volts)
    
    def getVoltvariance(self):
        print("Variance: ", st.variance(self.volts))
        return st.variance(self.volts)
    
    def getVoltstdev(self):
        print("Standard Deviation: ", st.stdev(self.volts))
        return st.stdev(self.volts)
    
    def plotVolt(self):
        plt.title("Voltage")
        plt.xlabel("Time")
        plt.ylabel("Voltage")
        plt.axis([min(self.voltTimes), max(self.voltTimes), 3.2, 3.4])
        plt.plot(self.voltTimes, self.volts)
        plt.show()

    def getVoltMeanPD(self):
        query = "SELECT volt FROM volt_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Mean: ", df['volt'].mean())
        return df['volt'].mean()
    

    def getVoltvariancePD(self):
        query = "SELECT volt FROM volt_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Variance: ", df['volt'].var())
        return df['volt'].var()    
    
    def getVoltstdevPD(self):
        query = "SELECT volt FROM volt_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Standard Deviation: ", df['volt'].std())
        return df['volt'].std()
    
    def getVoltMedianPD(self):
        query = "SELECT volt FROM volt_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Median: ", df['volt'].median())
        return df['volt'].median()
    
    def describeVoltTable(self):
        query = "SELECT volt FROM volt_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print(df['volt'].describe())
        return df['volt'].describe()
    
    def writeHtmlVoltTuple(self):
        html = "<table border='1'>"
        html += "<tr><th>Volt</th><th>Time</th></tr>"
        for volt, times in zip(self.volts, self.voltTimes):
            html += "<tr><td>" + str(volt) + "</td><td>" + str(time.ctime(times)) + "</td></tr>"
        html += "</table>"
        return html            
#----------------------------Light---------------------------------
    def getLight(self):
        try:
            light = self.writeSerial("get", "light")
            #print("Received: ", light)
            print(light)
            return light
        except:
            pass
        
        
    def saveLightToDB(self):
        try:
            light = self.getLight()
            lightstep = self.getLightStep()
            times = int(time.time())
            self.dbObj.insertData("light_table", times, light, lightstep)
            return light, lightstep
            
        except:
            return "Fail"
        
        
    def getLightStep(self):
        try:
            light = self.writeSerial("get", "lightstep")
            light = float(light)
            #print("Received: ", light)
            return light
        except:
            pass
        
    def sampleLightToTuple(self, delay, count):
        for i in range(count):
            try:
                self.lights += (self.getLight(),)
                self.lightsteps += (int(self.getLightStep()),)
                self.lightTimes += (int(time.time()),)
                time.sleep(delay)
            except:
                continue
            
    def clearLightTuple(self):
        self.lights = ()
        self.lightsteps = ()
        self.lightTimes = ()
        
    def countLightDB(self):
        return self.dbObj.countTable("light_table")
    
    def saveLightTuplesToDB(self):
        for light, lightstep, lightTime in zip(self.lights, self.lightsteps, self.lightTimes):
            print(light, lightstep, lightTime)
            self.dbObj.insertData("light_table", lightTime, light, lightstep)

        
    def loadLightFromDB(self):
        for row in self.dbObj.selectData("light_table"):
            #add values in self.volt and self.time
            self.lights += (row[1],)
            self.lightsteps += (row[2],)
            self.lightTimes += (row[0],)
            
    def printLightTuples(self):
        for light, lightstep, lightTime in zip(self.lights, self.lightsteps, self.lightTimes):
            print(f"light: {light}, lightstep: {lightstep}, time: {time.ctime(lightTime)}")
            
    def avgLight(self):
        print("Average light: ", st.mean(self.lightsteps))
        return st.mean(self.lightsteps)
    
    def varianceLight(self):
        print("Variance light: ", st.variance(self.lightsteps))
        return st.variance(self.lightsteps)
    
    def stdevLight(self):
        print("Standard Deviation light: ", st.stdev(self.lightsteps))
        return st.stdev(self.lightsteps)
    
    def plotLight(self):
        plt.title("Light")
        plt.xlabel("Time")
        plt.ylabel("Light")
        plt.axis([min(self.lightTimes), max(self.lightTimes), 0, 900])
        plt.plot(self.lightTimes, self.lightsteps)
        plt.show()
        

    def getLightMeanPD(self):
        query = "SELECT light_step FROM light_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Mean: ", df['light_step'].mean())
        return df['light_step'].mean()
    
    def getLightvariancePD(self):
        query = "SELECT light_step FROM light_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Variance: ", df['light_step'].var())
        return df['light_step'].var()
    
    def getLightstdevPD(self):
        query = "SELECT light_step FROM light_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Standard Deviation: ", df['light_step'].std())
        return df['light_step'].std()
    
    def getLightMedianPD(self):
        query = "SELECT light_step FROM light_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print("Median: ", df['light_step'].median())
        return df['light_step'].median()
    
    def describeLightTable(self):
        query = "SELECT light_step FROM light_table"
        df = pd.read_sql(query, self.dbObj.connection)
        print(df['light_step'].describe())
        return df['light_step'].describe()
    
    def writeHtmlLightTuple(self):
        html = "<table border='1'>"
        html += "<tr><th>Light</th><th>Light Step</th><th>Time</th></tr>"
        for light, lightstep, lightTime in zip(self.lights, self.lightsteps, self.lightTimes):
            html += "<tr><td>" + str(light) + "</td><td>" + str(lightstep) + "</td><td>" + str(time.ctime(lightTime)) + "</td></tr>"
        html += "</table>"
        return html
    
    