#------!!!!!!!!!!!!!!!!!!!!!!!------------------Samus------------------------!!!!!!!!!!!!!!!!!!!!!!!--------------------- 
@app.route("/Samus/getGames")
def getSamusGames():
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "select g_name, g_console, g_releaseDate from Games, joinCandG, Character where g_gameID = j_gameID and c_charID = j_charID and  c_name = "'"Samus"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        return store

@app.route("/Samus/getFranchise")
def getSamusFranch():
         #connect to SMASH database
        connect = sql.connect("smash.db")
        #control database
        cursor  = connect.cursor()
        query = "select distinct(f_name) from Character, Games, Franchise, joinCandG where c_charID = j_charID and j_gameID = g_gameID and g_franchID = f_franchID and c_name = "'"Samus"'";"
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store

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
        query = '''select u_userName, cs_comment, u_main from User, commSect, Character where u_userID = cs_userID 
                 and c_charID = cs_charID and c_name = "Samus";'''
        cursor.execute(query)
        store = cursor.fetchall()
        store = json.dumps(store)
        print store
        return store