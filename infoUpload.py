import datetime
import csv
import os
currentTime = datetime.datetime.now()

def get_database():
	from pymongo import MongoClient
	import pymongo
	CONNECTION_STRING = "mongodb+srv://admin-preetam:pam%21%40%23QW@cluster0.bq71x.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
	from pymongo import MongoClient
	client = MongoClient(CONNECTION_STRING)
	return client.IoTDB
    

def get_report(file):
	cycles = []
	cycle = []
	status = True
	csvFile = csv.reader(file)
	
	for row in csvFile:
		if row[0] == 'Status' and row[1]== 'Fail':
			status = False
		if (row[0].find('END') == -1) :
			if row[0][0] == '#':
				pass
			else:
				cycle.append(row)
		else:
			cycletoMap = {item[0]: item[1] for item in cycle}
			cycles.append(cycletoMap)
			cycle = []

	return cycles, status


if __name__ == "__main__":    
    
    # Get the database
	dbname = get_database()

	filePath =  './product3.csv'
	head, tail = os.path.split(filePath)
	productNumber = tail.split('Report .')[0]
	file = open(filePath)
	cycles, status = get_report(file)
	print(status)
	report = {
		'cycles': cycles,
		'productNumber': productNumber,
		'status': status
	}
	 
	dbname['reports'].insert_one(report)
