import datetime
import csv
import os


def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://preetam3620:preetam3620@cluster0-shard-00-00.bq71x.mongodb.net:27017,cluster0-shard-00-01.bq71x.mongodb.net:27017,cluster0-shard-00-02.bq71x.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client.IoTDB


def get_report(file):
    cycles = []
    cycle = []
    status = True
    csvFile = csv.reader(file)
    WaterFillingTime = 0     # water filling time
    WaterHeatingTime = 0     # water heating time

    for row in csvFile:
        if (row[0].find('WaterFillingTime') != -1):
            WaterFillingTime = row[1]
        elif (row[0].find('WaterHeatingTime') != -1):
            WaterHeatingTime = row[1]
        elif (row[0].find('E') == -1): # if 'END' is not present
            if (row[0].find('Criteria') != -1):
                modifiedRow = [row[0], row[1] + row[2]]
                cycle.append(modifiedRow)
            else:
                cycle.append(row)
        else:
            statusCheck(cycle)
            cycletoMap = {item[0]: item[1] for item in cycle}
            cycles.append(cycletoMap)
            cycle = []

    for cycle in cycles:
        if (cycle['Status'] == False):
            status = False
    
    print(cycles)
    return cycles, status, WaterFillingTime, WaterHeatingTime


def statusCheck(cycle):
    cycleStatus = True
    
    if (cycle[0][1] == 'Rinse'):
        if (cycle[1][1] != 'OFF'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'OFF'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'ON'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'ON'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'ON'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'ON'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'ON'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'ON'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
    elif (cycle[0][1] == 'Button pressed1'):
        if (cycle[1][1] != 'clockwise'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'OFF'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'ON'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'OFF'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'OFF'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'ON'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'OFF'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'OFF'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
        elif (int(cycle[10][1]) > 95 and int(cycle[10][1]) < 85): # Weight
            cycleStatus = False
    elif (cycle[0][1] == 'Button pressed2'):
        if (cycle[1][1] != 'OFF'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'clockwise'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'OFF'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'ON'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'OFF'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'OFF'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'ON'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'OFF'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
        elif (int(cycle[10][1]) > 95 and int(cycle[10][1]) < 85): # Weight
            cycleStatus = False   
    elif (cycle[0][1] == 'Button pressed3'):
        if (cycle[1][1] != 'clockwise'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'OFF'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'ON'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'OFF'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'OFF'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'ON'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'OFF'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'OFF'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
        elif (int(cycle[10][1]) > 50 and int(cycle[10][1]) < 45): # Weight
            cycleStatus = False
    elif (cycle[0][1] == 'Button pressed4'):
        if (cycle[1][1] != 'OFF'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'clockwise'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'OFF'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'ON'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'OFF'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'OFF'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'ON'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'OFF'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
        elif (int(cycle[10][1]) > 50 and int(cycle[10][1]) < 45): # Weight
            cycleStatus = False
    elif (cycle[0][1] == 'Button pressed5'):
        if (cycle[1][1] != 'OFF'): # GB1
            cycleStatus = False
        elif (cycle[2][1] != 'OFF'): # GB2
            cycleStatus = False
        elif (cycle[3][1] != 'OFF'): # GB3
            cycleStatus = False
        elif (cycle[4][1] != 'OFF'): # Mixer1
            cycleStatus = False
        elif (cycle[5][1] != 'OFF'): # Mixer2
            cycleStatus = False
        elif (cycle[6][1] != 'OFF'): # Mixer3
            cycleStatus = False
        elif (cycle[7][1] != 'OFF'): # Water in Mixer1
            cycleStatus = False
        elif (cycle[8][1] != 'OFF'): # Water in Mixer2
            cycleStatus = False
        elif (cycle[9][1] != 'OFF'): # Water in Mixer3
            cycleStatus = False
        elif (int(cycle[10][1]) > 85 and int(cycle[10][1]) < 75): # Temp
            cycleStatus = False
        elif (int(cycle[10][1]) > 95 and int(cycle[10][1]) < 85): # Weight
            cycleStatus = False

    statusRow = ['Status', cycleStatus]
    cycle.append(statusRow)
    

def uploadReport(filePath):
    currentDateTime = str(datetime.datetime.now())
    currentDate = currentDateTime[0:10]
    currentTime = currentDateTime[11:19]

    # connect to database 
    dbname = get_database()

    # get productNumber from fileName
    head, tail = os.path.split(filePath)
    productNumber = tail.split('.')[0]

    # parse the file and get the data of cycles
    file = open(filePath)
    cycles, status, WaterFillingTime, WaterHeatingTime = get_report(file)

    # schema of the report 
    report = {
        'cycles': cycles,
        'status': status,
        'productNumber': productNumber,
        'WaterFillingTime': WaterFillingTime,
        'WaterHeatingTime': WaterHeatingTime,
        'date': currentDate,
        'time': currentTime,
    }

    # upload to database
    dbname['reports'].insert_one(report)