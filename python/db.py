import psycopg2
import time

class db:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="taeho0828")
            self.cursor = self.connection.cursor()
            print("Database connected")
        except:
            print("Failed to connect to database")
            exit(1)
            
    def writeToDB(self, cmd):
        self.cursor.execute(str(cmd))
        self.connection.commit()

    def disconnectToDB(self):
        self.cursor.close()
        self.connection.close()

    def insertData(self, time, voltage):
        try:
            self.cursor.execute("INSERT INTO volt_table(meas_time, volt) VALUES (%s, %s)", (str(time), str(voltage)))
            self.connection.commit()
        except Exception as e:
            print("An error occurred: ", e)
            self.connection.rollback()
            pass
        
    def selectData(self):
        self.cursor.execute("SELECT meas_time, volt FROM volt_table")
        rows = self.cursor.fetchall()
        return rows
    
    def deleteData(self):
        self.cursor.execute("DELETE FROM volt_table")
        self.connection.commit()
    
    def countVoltTable(self):
        self.cursor.execute("SELECT COUNT(*) FROM volt_table")
        count = self.cursor.fetchone()
        return count
    