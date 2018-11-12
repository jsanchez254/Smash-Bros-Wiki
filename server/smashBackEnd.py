from flask import Flask
import sqlite3 as sql
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#global variables used for connection and key
connect = None
cursor = None

#connect to SMASH database
connect = sql.connect("smash.db")
#control database
cursor  = connect.cursor()

@app.route('/')
def index():
    #connect to SMASH database
    connect = sql.connect("smash.db")
    #control database
    cursor  = connect.cursor()
    query = "SELECT c_name from Character;"
    cursor.execute(query)
    store = cursor.fetchall()
    store = json.dumps(store)
    return store
    


if __name__ == '__main__':
        app.run(debug =True)
