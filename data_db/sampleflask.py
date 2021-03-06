from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]

data = mydb["data"]
corrected = mydb["corrected_data"]
info = mydb["info"]

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



@app.route('/1')
def ha():
    return render_template('map.html')
        
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

app.run('0.0.0.0',80)