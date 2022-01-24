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
    wft = 0     # water filling time
    wht = 0     # water heating time

    for row in csvFile:
        if (row[0].find('WaterFillingTime') != -1):
            wft = row[1]

        elif (row[0].find('WaterHeatingTime') != -1):
            wht = row[1]

        elif (row[0].find('E') == -1): # if 'END' is not present
            if (row[0].find('Criteria') != -1):
                modifiedRow = [row[0], row[1] + row[2]]
                cycle.append(modifiedRow)
            else:
                cycle.append(row)

        else:
            status = statusCheck(cycle)
            # print(cycle, "\n")
            cycletoMap = {item[0]: item[1] for item in cycle}
            cycles.append(cycletoMap)
            cycle = []

    return cycles, status, wft, wht

def statusCheck(cycle):
    for item in cycle:
        if(item[1] == 'Rinse'):
            pass
    status = 'OK'
    statusRow = ['Status', status]
    cycle.append(statusRow)
    return True

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
    cycles, status, wft, wht = get_report(file)

    # schema of the report 
    report = {
        'cycles': cycles,
        'status': status,
        'productNumber': productNumber,
        'wft': wft,
        'wht': wht,
        'date': currentDate,
        'time': currentTime,
    }

    # upload to database
    dbname['reports'].insert_one(report)