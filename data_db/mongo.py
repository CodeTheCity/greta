import pprint
from datetime import datetime, tzinfo, timezone, date, timedelta
import os, json
from pymongo import MongoClient
import pprint
import os.path

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
data = mydb["data"]
corrected = mydb["corrected_data"]
directory = 'data/big_dump/parcedJsons/'

# all parced jsons folder in db
def pushdata():
    if(data.count_documents({})== 0):
        for filename in os.listdir(directory):        
                with open( directory + filename , 'r') as f:
                    datastore = json.load(f)
                    m = data.insert_one(datastore)
                    n = corrected.insert_one(datastore)

# all sensors data for specific time   
# how to search
def query_a_time_period(x,y):
    query_timeperiod = [
        {"$unwind": "$readings"},
        {"$match":{"readings.timestamp": { "$gt": x, "$lt": y } }},
        {"$replaceRoot":{"newRoot": "$readings"}}]
    cursor = data.aggregate(query_timeperiod)
    result = list(cursor)
    pprint.pprint(result)
    return result

def removedb():
    myclient.drop_database('mydb')
    
    
def get_all_ids():
    location_id = data.distinct("location_id")
    return location_id
    
    
def get_all_coordinates():
    all_ids = get_all_ids()
    for document in all_ids:
        print(data.find_one( {"location_id":document},
                            {"location_id":"true", "latitude": "true", "longitude":"true" }))
        
def correction():
    query_param = [
        {"$unwind": "$readings"},
        {"$match":{"readings.humidity": { "$gt": "70"} }},
        {"$replaceRoot":{"newRoot": "$readings"}}]
    cursor = corrected.aggregate(query_param)
    result = list(cursor)
    #pprint.pprint(result)
    for doc in result:
        if "P1" in doc:
            doc["P1"] = str( 0 - float(doc["P1"]))
            doc["P2"] = str( 0 - float(doc["P2"]))  
            print (doc)
    
def main():   
    
    start_time  = "1530857160"
    finish_time = "1530870160"
    #removedb()
    pushdata() 
    
    #get_all_ids()
    get_all_coordinates()
    
    #correction()
    #print_collection_data("corrected_data")
    
    #query_a_time_period(start_time,finish_time)
    
    
    
    #removedb 
    
    return()


if __name__ == '__main__':
    main()
