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
#------------------------IKE---------------------------------------------
@app.route('/Ike')
def ikedesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Ike"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/moves")
def ikeMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_CharID = 7;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/tier")
def ikeTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_CharID = 7;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/class")
def ikeClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_CharID = 7;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store


if __name__ == '__main__':
        app.run(debug =True)
