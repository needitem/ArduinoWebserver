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

    def insertData(self,table_name, time, value1, value2=0):
        if table_name == "volt_table":
            try:
                self.cursor.execute(f"INSERT INTO {table_name}(meas_time, volt) VALUES (%s, %s)", (str(time), str(value1)))
                self.connection.commit()
            except Exception as e:
                print("An error occurred: ", e)
                self.connection.rollback()
                pass
        elif table_name == "light_table":
            try:
                self.cursor.execute(f"INSERT INTO {table_name}(meas_time, light, light_step) VALUES (%s, %s, %s)", (str(time), str(value1), value2))
                self.connection.commit()
            except Exception as e:
                print("An error occurred: ", e)
                self.connection.rollback()
                pass
        
    def selectData(self, table_name):
        if table_name == "volt_table":
            self.cursor.execute(f"SELECT meas_time, volt FROM {table_name}")
        elif table_name == "light_table":
            self.cursor.execute(f"SELECT meas_time, light, light_step FROM {table_name}")
            
        rows = self.cursor.fetchall()
        return rows
    
    def deleteData(self, table_name):
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.connection.commit()
    
    def countTable(self, table_name):
        self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = self.cursor.fetchone()
        #count : (97,) ==> 97
        count = count[0]
        return count
    