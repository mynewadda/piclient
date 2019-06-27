from flask import Flask,jsonify
from json import dumps

from pymongo import MongoClient
client = MongoClient("mongodb://Kumar:galaxymilk3%23@cluster1-shard-00-00-jz1pv.mongodb.net:27017,cluster1-shard-00-01-jz1pv.mongodb.net:27017,cluster1-shard-00-02-jz1pv.mongodb.net:27017/measurements?ssl=true&replicaSet=Cluster1-shard-0&authSource=admin&w=majority")
db = client.measurements
app = Flask(__name__)

@app.route("/get", methods = ['GET'])
def get_all_contact():
        contacts = db.measurements.find()
        o=[]
        for c in contacts:
            o.append({'temp':c['temp'],'pressure':c['pressure'],'humidity':c['humidity']})
        return jsonify({'data':o})



if __name__ == '__main__':
      app.run(debug=True,port='2345')
