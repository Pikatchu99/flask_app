from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/api/v1/all', methods=['GET'])
def hello():
    return 200, jsonify({"Equipe backend": ["Henok", "Modeste"]})
