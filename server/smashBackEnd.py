from flask import Flask, request
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


@app.route('/register', methods = ["GET", "POST"])
def register():
        if request.method == "POST":
                # comment = request.form.get("comment", False)
                comment = request.data
                parse = json.loads(comment)
                parse1 = parse["blog"]
                comment = parse1["comment"]
                print comment
                return "wow"
        return "I was a post"

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
#------!!!!!!!!!!!!!!!!!!!!!!!------------------IKE------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
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

@app.route("/Ike/like")
def ikeLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Ike";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/dislike")
def ikedislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Ike";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/comments")
def IkeComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Ike";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store


#------!!!!!!!!!!!!!!!!!!!!!!!------------------TOON LINK------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Toon_Link')
def Toon_Linkdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Toon Link"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/moves")
def Toon_LinkMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/tier")
def Toon_LinkTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/class")
def Toon_LinkClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/like")
def Toon_LinkLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/dislike")
def Toon_Linkdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Toon_Link/comments")
def Toon_LinkComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store



if __name__ == '__main__':
        app.run(debug =True)
