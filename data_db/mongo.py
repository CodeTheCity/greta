import pprint
from datetime import datetime, tzinfo, timezone, date, timedelta
import os, json
from pymongo import MongoClient
import pprint
import os.path
from flask import Flask, render_template, jsonify

app = Flask(__name__)
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
data = mydb["data"]
directory = 'data/big_dump/parcedJsons/'



# all parced jsons folder in db
def pushdata():
    if(data.count_documents({})== 0):
        for filename in os.listdir(directory):        
                with open( directory + filename , 'r') as f:
                    datastore = json.load(f)
                    m = data.insert_one(datastore)  

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
    arry = []
    for document in all_ids:
        arry.append(data.find_one( {"location_id":document},
                            {"location_id":"true", "latitude": "true", "longitude":"true" }))
    return arry


@app.route('/info', methods=['GET'])
def get_all_points():
    get_raw_points = get_all_coordinates()
    list_coordinates = []
    for data in get_raw_points:
        list_coordinates.append({'location_id': data['location_id'],
              'coords': [data['latitude'],data['longitude']]})
    print (list_coordinates)
    return render_template('info.html',  list_coordinates = list_coordinates)

@app.route('/')
def main():
    return render_template('main.html')



 
start_time  = "1530857160"
finish_time = "1530860160"
    #removedb()
pushdata() 
get_all_coordinates()
    
#query_a_time_period(start_time,finish_time)
    
    
    
    #removedb 
    


app.run('0.0.0.0',80)



