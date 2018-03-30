#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------


import json
import sqlite3

# SQLite DB Name
DB_Name =  "dbMQTT.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()

	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def Sensor_Data_Handler(jsonData):
	#Parse Data
	json_Dict = json.loads(jsonData)
	ID = json_Dict['ID']
	Data_and_Time = json_Dict['Date']
	Sensor_value = json_Dict['Value']

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into sensor (ID, Date_n_Time, Sensor_value) values (?,?,?)",[ID, Data_and_Time, Sensor_value])
	del dbObj
	print("Inserted *Sensor Data into Database.")
	print("")

def Weather_Data_Handler(jsonData):
	#Parse Data
	json_Dict = json.loads(jsonData)
	ID = json_Dict['ID']
	Data_and_Time = json_Dict['Date']
	weather_value = json_Dict['Value']

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into weather (ID, Date_n_Time, weather_value) values (?,?,?)",[ID, Data_and_Time, weather_value])
	del dbObj
	print("Inserted *Weather Data into Database.")
	print("")

# Function to save Humidity to DB Table
def Location_Data_Handler(jsonData):
	#Parse Data
	json_Dict = json.loads(jsonData)
	#ID = json_Dict['ID']
	#Data_and_Time = json_Dict['Date']
	#lx = json_Dict['lx']
	#ly = json_Dict['ly']
	loc = json_Dict['loc']
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into location (loc) values (?)",[loc])
	del dbObj
	print("Inserted *location Data into Database.")
	print("")


#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "sensor":
		Sensor_Data_Handler(jsonData)
	elif Topic == "weather":
		Weather_Data_Handler(jsonData)
	elif Topic == "location":
		Location_Data_Handler(jsonData)

#===============================================================
