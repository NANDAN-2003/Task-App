from flask import Flask,request,jsonify
from pymongo import MongoClient
from flask_cors import CORS
from date import datetime

app=Flask(__name__)
CORS(app)

client=MongoClient("mongodb+srv://nandannand2003_db_user:fO7X1VRhgUgEgtha@cluster0.p0h3vcw.mongodb.net/?appName=Cluster0")
db=client["Student"]
collection=db["collection"]

@app.route("/task",methods=["GET"])
def get_task():
    data=list(collection.find({},{"_id":0}))
    return jsonify(data)

@app.route("/task",methods=["POST"])
def add_task():
    data=request.json
    data["timestamp"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    collection.insert_one(data)
    return jsonify({"msg":"task added"})

@app.route("/task/<title>",methods=["DELETE"])
def delete_task(title):
    collection.delete_one({"title":title})
    return jsonify({"msg":"task deleted"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)



