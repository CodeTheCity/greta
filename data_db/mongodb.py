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
info = mydb["info"]


directory = 'data/big_dump/parcedJsons/'
infolist = 'data/big_dump/info.json'
# all parced jsons folder in db
def pushdata():
    if(data.count_documents({})== 0):
        for filename in os.listdir(directory):        
                with open( directory + filename , 'r') as f:                
                    datastore = json.load(f)
                    for document in datastore:
                        m = data.insert_one(document)
                        n = corrected.insert_one(document)
                        print("document" + str(m) + " pushed completed.")
                    
                    
def pushinfo():
    if(info.count_documents({})== 0):
        with open( infolist , 'r') as f:                
            datastore = json.load(f)
            for document in datastore:
                inserted_data = info.insert_one(document)
                print (str(inserted_data)  + "info completed.")
                

# all sensors data for specific time   
# how to search
def query_a_time_period(start_time,finish_time):
    query_param =[{"$match":{ "timestamp":{"$gt":start_time,"$lt":finish_time}}}]
    cursor = data.aggregate(query_param)
    result = list(cursor)
    pprint.pprint(result)
    return result

def removedb():
    myclient.drop_database('mydb')
    
    
def get_all_ids():
    location_id = info.distinct("location_id")
    return location_id
    
    
def get_all_coordinates():
    all_ids = get_all_ids()
    arry = []
    for document in all_ids:
        arry.append(info.find_one( {"location_id":document},
                            {"location_id":"true", "latitude": "true", "longitude":"true" }))
    return arry

        
def correction(x):
    query_param =[{"$match":{ "humidity":{"$gt":x}}}]
    cursor = data.aggregate(query_param)
    result = list(cursor)
    for doc in result:
        if "P1" in doc:
            doc["P1"] = 0 - doc["P1"]
            doc["P2"] =  0 - doc["P2"]
            # change  for sensor with high humidity
            print (doc)     
            
    
def findGeneral_info(x):
    print(info.find_one({"location_id": x}))
    return info.find_one({"location_id": x})
                         
                
    
def main():   
    
    start_time  = 1574457160
    finish_time = 1575701600
    #removedb()
    pushdata() 
    pushinfo()
    #get_all_ids()
    #get_all_coordinates()
    
    #correction(70)
    #print_collection_data("corrected_data")
    
    query_a_time_period(start_time,finish_time)
    
    
    
    #removedb 
    
    return()


if __name__ == '__main__':
    main()
