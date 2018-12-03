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


#update Character
@app.route("/updateChar" ,  methods = ["GET", "POST"])
def updareChar():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check) 
                parse1 = parse["char"]
                
                #char info
                tier = parse1["tier"]
                description = parse1["description"]
                class1 = parse1["class"]
                name = parse1["character"]
                
                #moveSet
                ultimate =  parse1["move1"]
                side = parse1["move2"]
                bAttack = parse1["move3"]
                recovery = parse1["move4"]

                charID = getCharacterId(name)
                updateCharacter(charID, tier, description, class1)
                updateMoves(charID, ultimate, side, bAttack, recovery)

                return "wow"
        return "cool"

def updateMoves(charID, ultimate, side, bAttack, recovery):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        query = '''UPDATE Moves SET m_ultimate = ''' + '"' + ultimate + '"' + ''',m_sideSmash = ''' + '"' + side + '"' + ''', m_bAttack = ''' + '"' + bAttack +  '"' + ''', m_recovery = ''' + '"' + recovery +  '"' + ''' WHERE m_charID = ''' + str(charID) + ''';'''
        print query
        cursor.execute(query)
        connect.commit() 

def updateCharacter(name, tier, description, class1):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        query = '''UPDATE Character SET c_tier = ''' + "'" + tier + "'" + ''',c_class = ''' + "'" + class1 + "'" + ''', c_desc = ''' + '"' + description +  '"' + ''' WHERE c_charID = ''' + str(name) + ''';'''
        print query
        cursor.execute(query)
        connect.commit() 
        
def getCharacterId(character):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        query = '''SELECT c_charID from Character WHERE c_name = ''' +  "'" + character + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]



#get users
@app.route("/getUsers")
def getUsers():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName from User;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

        

#delete Users
@app.route("/DeleteUser" ,  methods = ["GET", "POST"]  )
def deleteUser():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check) 
                parse1 = parse["user1"]
                user = parse1["user"]

                userID = getUserID(user)
                print userID

                deleteAllUser(userID)

                return "cool"

        return "meh"

def getUserID(user):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        query = '''SELECT u_userID FROM User where u_userName = ''' + "'" + user + "'"+ ''';'''
        cursor.execute(query)
        store = cursor.fetchall()
        print store
        return store[0][0] 

def deleteAllUser(userID):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        cursor.execute('''DELETE FROM User WHERE u_userID = ''' + str(userID) + ''';''')
        connect.commit() 

        cursor.execute('''DELETE FROM commSect WHERE cs_userID = ''' + str(userID) +  ''';''')
        connect.commit() 


#get franchise
@app.route("/getFranchise")
def getFranchise():
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select f_name from Franchise;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#get TimeLine
@app.route("/getTimeline")
def getTimeLine():
          #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select c_name, f_initialRelease from Character, Games, Franchise,
                 joinCandG where c_charID = j_charID
                and j_gameID = g_gameID and g_franchID = f_franchID
                 group by c_name order by f_initialRelease;'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

#create character !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route("/createCharacter",  methods = ["GET", "POST"] )
def createCharacter():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check) 
                parse1 = parse["newChar"]
                
                #char info
                tier = parse1["tier"]
                description = parse1["description"]
                name = parse1["name"]
                class1 = parse1["class"]
                
                #moveSet
                ultimate =  parse1["move1"]
                side = parse1["move2"]
                bAttack = parse1["move3"]
                recovery = parse1["move4"]

                #game
                franchise = parse1["franchise"]
                game1 = parse1["game1"]
                date1 = parse1["date1"]
                console1 = parse1["console1"]
                game2 = parse1["game2"]
                date2 = parse1["date2"]
                console2 = parse1["console2"]

                insertNewCharacter(name, tier, class1, description)
                charID = getCharacterId(name)
                insertMoves(charID, ultimate, side, bAttack, recovery)
                insertLikeSystem (charID)

                franchID = getFranchID(franchise)
                gameID1 = insertGame(game1, date1, console1, franchID)
                gameID2 = insertGame(game2, date2, console2, franchID)
                insertJoinCharGame(charID, gameID1)
                insertJoinCharGame(charID, gameID2)


                return "it works"
        return "cool"

def insertJoinCharGame(charID, gameID):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO joinCandG (j_charID, j_gameID)
                        VALUES (?,?)''' , (charID, gameID))
        connect.commit() 

def insertMoves(charID, ultimate, side, bAttack, recovery):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO Moves (m_charID, m_ultimate, m_sideSmash, m_bAttack, m_recovery)
                        VALUES (?,?,?,?,?)''' , (charID, ultimate, side, bAttack, recovery))
        connect.commit() 

def getFranchID(franchise):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        query = '''SELECT f_franchID FROM Franchise where f_name = ''' + "'" + franchise + "'"+ ''';'''
        cursor.execute(query)
        store = cursor.fetchall()
        print store
        return store[0][0] 

def insertGame(game1, date1, console1, franchise):
        connect = sql.connect("smash.db")
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO Games (g_franchID, g_console, g_name,  g_releaseDate)
                        VALUES (?,?,?,?)''' , (franchise, console1, game1, date1))
        connect.commit() 

        query = '''SELECT max(g_gameID) FROM Games'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0] 
        

def insertNewCharacter(name, tier, class1, description):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO Character (c_name, c_tier, c_class, c_desc)
                        VALUES (?,?,?,?)''' , (name, tier, class1, description))
        connect.commit()

def getCharacterId(character):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_charID from Character WHERE c_name = ''' +  "'" + character + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

def insertLikeSystem(charID):
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO Voting (l_charID, l_like, l_dislike)
                        VALUES (?,?,?)''' , (charID, 0, 0))
        connect.commit()


#check if admin
@app.route("/admin", methods = ["GET", "POST"])
def checkAdmin():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check)
                parse1 = parse["user"]
                userName = parse1["userName"]

                print userName

                #connect to SMASH database
                connect = sql.connect("smash.db")
                #control database
                cursor  = connect.cursor()
                query = ''' SELECT u_admin FROM User
                        WHERE  u_userName = ''' + "'" + userName + "'" + ''';'''
                cursor.execute(query)
                store = cursor.fetchall()
                print "PRINT THIS SHIIIIT"
                hello = store[0][0]
                print hello

                if(hello == 1):
                        return "true"
                else:
                        return "false"
                
        return "wow"


#UPDATE LIKES AND DISLIKES
@app.route("/updateLikes", methods = ["GET", "POST"])
def updateLikes():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check)
                print check
                parse1 = parse["check"]
                userName = parse1["userName"]
                character = parse1["character"]
                like = parse1["like"]
                dislike = parse1["dislike"]

                userID = getUserId(userName)
                charID = getCharacterId(character)

                insertLike(userID,  charID, like, dislike)

                return "arikado"

def insertLike(userName, character, like, dislike):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO joinVandU (jvu_charID, jvu_userID, jvu_like, jvu_dislike)
                        VALUES (?,?,?,?)''' , (userName, character, like, dislike))
        connect.commit()

        # -- WILL BE 1 IN DISLIKE OR 1 IN LIKE, DEPENDING ON ACTION, PYTHON WILL TAKE
        # -- CARE OF SPECIFICS
        query = '''UPDATE Voting
        SET l_like = (l_like + ''' + str(like) + ''' ), l_dislike = (l_dislike + ''' + str(dislike) + ''')
        where l_charID =''' +  str(character) + ''';'''

        cursor.execute(query)
        connect.commit()

def getCharacterId(character):
          #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_charID from Character WHERE c_name = ''' +  "'" + character + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

def getUserId(userName):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT u_userID from User WHERE u_userName = ''' +  "'" + userName + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]


#CHECK LIKE STATUS
@app.route("/checkLikeStatus", methods = ["GET", "POST"])
def checkLikeStatus():
        if request.method == "POST":
                check = request.data    
                parse = json.loads(check)
                print check
                parse1 = parse["check"]
                userName = parse1["userName"]
                character = parse1["character"]

                userID = getUserId(userName)
                charID = getCharacterId(character)

                print userID
                print charID
                checko = checkStatus(userID, charID)
        
                print checko

                return  checko
        return "cool2"

def checkStatus(userID, charID):
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = ''' SELECT jvu_charID FROM joinVandU
                WHERE  jvu_charID = ''' + str(charID) + ''' AND
                jvu_userID = ''' + str (userID)   + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()

        try:
                test = store[0][0]
        except IndexError:
                return "false"

        return "true"

def getCharacterId(character):
          #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_charID from Character WHERE c_name = ''' +  "'" + character + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

def getUserId(userName):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT u_userID from User WHERE u_userName = ''' +  "'" + userName + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

#--------------------------------------------------------------------------------------------#

#CREATE A USER!!!
@app.route("/createUser", methods = ["GET", "POST"])
def createUser():
        print "cool"
        if request.method == "POST":
                user = request.data
                parse = json.loads(user)
                parse1 = parse["newUser"]
                userName = parse1["userName"]
                password = parse1["password"]
                main = parse1["main"]
                email = parse1["email"]
                name = parse1["name"]
                lname = parse1["lname"]

                # print(userName)
                # print(name)
                # print(lname)
                # print(password)
                # print(main)
                # print(email)
                
                insertUser(userName, password, main, email, name, lname)

                return "cool"
        return "okay"
def insertUser(userName, password, main, email, name, lname):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        cursor.execute('''INSERT INTO User (u_firstName, u_lastName, u_email, u_userName, u_admin, u_main)
                        VALUES (?,?,?,?,?,?)''' , (name, lname, email, userName,  0, main))
        connect.commit()




@app.route('/blog', methods = ["GET", "POST"])
def register():
        if request.method == "POST":
                # comment = request.form.get("comment", False)
                comment = request.data
                parse = json.loads(comment)
                parse1 = parse["blog"]
                comment = parse1["comment"]
                character = parse1["character"]
                userName = parse1["userName"]
                print character
                print comment
                print userName
                charID = getCharacterId(character)
                userID = getUserId(userName)
                print charID
                print userID
                insertComment(comment, charID, userID)
                return "wow"
        return "I was a post"

def getCharacterId(character):
          #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_charID from Character WHERE c_name = ''' +  "'" + character + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

def getUserId(userName):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT u_userID from User WHERE u_userName = ''' +  "'" + userName + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        return store[0][0]

def insertComment(comment, charID, userID):
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''INSERT INTO commSect (cs_userID, cs_charID, cs_comment)
                   VALUES (''' + str(userID) + "," + str(charID) + "," + "'" + comment + "'" + ''') ;'''
        cursor.execute(query)
        connect.commit()

valid = "HELLO"
#LOG IN LOGIC!!
@app.route("/logIn", methods = ["GET", "POST"])
def logIn():
        if request.method == "POST":
                info = request.data
                parse = json.loads(info)
                info = parse["user"]
                print info
                userName = info["userName"]
                password = info["password"]
                global valid
                valid = checkValid(userName, password)
                print valid
                return valid
        if request.method == "GET":
                return valid

def checkValid(userName, password):
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT u_userName from User WHERE u_email = ''' +  "'" + userName + "'" + '''
                AND u_userName = ''' + "'" +  password + "'" + ''' ;'''
        cursor.execute(query)
        store = cursor.fetchall()
        try:
                test = store[0][0]
        except IndexError:
                test = "null1"
        if test == "null":
                return test
        else:
                return test

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
@app.route("/Ike/getGames")
def getGames():
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "select g_name, g_console, g_releaseDate from Games, joinCandG, Character where g_gameID = j_gameID and c_charID = j_charID and  c_name = "'"Ike"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Ike/getFranchise")
def getFranch():
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "select distinct(f_name) from Character, Games, Franchise, joinCandG where c_charID = j_charID and j_gameID = g_gameID and g_franchID = f_franchID and c_name = "'"Ike"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

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
                 and c_charID = cs_charID and c_name = "Toon Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------BAYONETTA------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Bayonetta')
def Bayonettadesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Bayonetta"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/moves")
def BayonettaMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/tier")
def BayonettaTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/class")
def BayonettaClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/like")
def BayonettaLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/dislike")
def Bayonettadislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Bayonetta/comments")
def BayonettaComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Bayonetta";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store


        #------!!!!!!!!!!!!!!!!!!!!!!!------------------SNAKE------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Snake')
def Snakedesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Snake"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/moves")
def SnakeMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/tier")
def SnakeTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/class")
def SnakeClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/like")
def SnakeLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/dislike")
def Snakedislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Snake/comments")
def SnakeComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Snake";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

        #------!!!!!!!!!!!!!!!!!!!!!!!------------------SAMUS------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Samus')
def Samusdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Samus"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/moves")
def SamusMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/tier")
def SamusTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/class")
def SamusClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/like")
def SamusLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/dislike")
def Samusdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/comments")
def SamusComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Falco------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Falco')
def Falcodesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Falco"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/moves")
def FalcoMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/tier")
def FalcoTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/class")
def FalcoClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/like")
def FalcoLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/dislike")
def Falcodislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Falco/comments")
def FalcoComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Falco";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Fox------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Fox')
def Foxdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Fox"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/moves")
def FoxMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/tier")
def FoxTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/class")
def FoxClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/like")
def FoxLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/dislike")
def Foxdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Fox/comments")
def FoxComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Fox";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Link------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Link')
def Linkdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Link"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/moves")
def LinkMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/tier")
def LinkTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/class")
def LinkClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/like")
def LinkLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/dislike")
def Linkdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Link/comments")
def LinkComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Lucina------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Lucina')
def Lucinadesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Lucina"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/moves")
def LucinaMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/tier")
def LucinaTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/class")
def LucinaClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/like")
def LucinaLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/dislike")
def Lucinadislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Lucina/comments")
def LucinaComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Lucina";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Piranha_Plant------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Piranha_Plant')
def Piranha_Plantdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Piranha Plant"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/moves")
def Piranha_PlantMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/tier")
def Piranha_PlantTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/class")
def Piranha_PlantClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/like")
def Piranha_PlantLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/dislike")
def Piranha_Plantdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Piranha_Plant/comments")
def Piranha_PlantComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Piranha Plant";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Young LINK------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Young_Link')
def Young_Linkdesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Young Link"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/moves")
def Young_LinkMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/tier")
def Young_LinkTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/class")
def Young_LinkClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/like")
def Young_LinkLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/dislike")
def Young_Linkdislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Young_Link/comments")
def Young_LinkComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Young Link";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Mega_Man------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Mega_Man')
def Mega_Mandesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Mega Man"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/moves")
def Mega_ManMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/tier")
def Mega_ManTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/class")
def Mega_ManClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/like")
def Mega_ManLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/dislike")
def Mega_Mandislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Mega_Man/comments")
def Mega_ManComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Mega Man";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Greninja------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Greninja')
def Greninjadesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Greninja"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/moves")
def GreninjaMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/tier")
def GreninjaTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/class")
def GreninjaClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/like")
def GreninjaLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/dislike")
def Greninjadislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Greninja/comments")
def GreninjaComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Greninja";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Corrin------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Corrin')
def Corrindesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Corrin"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/moves")
def CorrinMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/tier")
def CorrinTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/class")
def CorrinClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/like")
def CorrinLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/dislike")
def Corrindislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Corrin/comments")
def CorrinComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Corrin";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

#------!!!!!!!!!!!!!!!!!!!!!!!------------------Cloud------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route('/Cloud')
def Clouddesc():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "SELECT c_desc from Character WHERE c_name = "'"Cloud"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/moves")
def CloudMoves():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT m_ultimate, m_sideSmash, m_bAttack, m_recovery 
                FROM Character, Moves where m_charID = c_CharID
                AND c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/tier")
def CloudTier():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_tier
                FROM Character where
                 c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/class")
def CloudClass():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''SELECT c_class
                FROM Character where
                 c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/like")
def CloudLike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_like from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/dislike")
def Clouddislike():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select distinct l_dislike from Character, joinVandU, Voting  where
                c_charID = jvu_charID and l_charID = jvu_charID and c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Cloud/comments")
def CloudComments():
        #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = '''select u_userName, cs_comment from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Cloud";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

if __name__ == '__main__':
        app.run(debug =True)
