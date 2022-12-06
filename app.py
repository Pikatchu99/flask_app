from flask import Flask
from flask import request, jsonify
from pymongo import MongoClient
import sys, traceback

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    try:
        client = MongoClient("mongodb+srv://yemalin-location:0J4JpSHCZCOYRRRw@yemalin-location.9ffbggd.mongodb.net/")
        db = client["yemalin-location"]
        users = db["users"]
        user = users.find_one()
        return "Welcome " + user["name"] + user["surname"] + "in " + user["team"]
    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return str(traceback.print_tb(exc_traceback) + traceback.print_exception(exc_value))
        # return str(error)

@app.route('/api/v1/all', methods=['GET'])
def hello():
    return jsonify({"Equipe backend": ["Henok", "Modeste"]})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
