#from flask import Flask
import sqlite3 as sql

#global variables used for connection and key
connect = None
cursor = None

#connect to SMASH database
connect = sql.connect("smash.db")
#control database
cursor  = connect.cursor()
 
#-1 disconnect from database and exit
def exit():
    global connect
    connect.close()

#---UPDATE STATEMENTS---#
#delete user (enter username)
#delete character (delete everything to do with character in it)
#update userName (have to enter password)
def updateState():
    userInput = 0
    while(True):
        if userInput == 0:
            print "--------------------------------------------"
            print "UPDATE STATEMENTS:"
            print "--------------------------------------------"
            print "1.- Delete user (enter username)"
            print "2.- Delete character (delete everything to do with character in it)"
            print "3.- Update userName (have to enter password)"
            print "4.- Update MAIN"    
            print "0   <<PRINT MENU AGAIN>>"
            print "-1  <<BACK TO MAIN MENU>>"
            print "--------------------------------------------"
        userInput = raw_input(">> ")
        userInput = int(userInput) 
        if userInput == 1:
            print "HELLO"
        elif userInput == -1:
            print "Back To Main Menu"
            return 


#-----INSERT------#
#create user account
#post a comment about certain character
#like a character or dislike
#make an account
#administrator add character
#administrator add game (ask for character)
#administrator add franchise (ask for character)
#administrator add moves to character
def insertState():
    userInput = 0
    while(True):
        if userInput == 0:
            print "--------------------------------------------"
            print "INSERT STATEMENTS:"
            print "--------------------------------------------"
            print "1.- Create user account"
            print "2.- Post a comment about certain character"
            print "3.- Like a character or dislike"
            print "4.- Make an account"
            print "5.- Administrator add character"
            print "6.- Administrator add game (ask for character)"
            print "7.- Administrator add franchise (ask for character)"
            print "8.- Administrator add moves to character"
            print "0   <<PRINT MENU AGAIN>>"
            print "-1  <<BACK TO MAIN MENU>>"
            print "--------------------------------------------"
        userInput = raw_input(">> ")
        userInput = int(userInput) 
        if userInput == 1:
            print "HELLO"
        elif userInput == -1:
            print "Back To Main Menu"
            return 

#---GET STATEMENTS----#
#get character with most likes
#get character's game
#order characters DESC based on their chronological release date
#get character's franchise
#get character's moves!
#get character's certain move (from list in moves)
#order characters based on their tier, display name
#get comments made about certain character (ask for char) display char and comment
#check if user with same username or password is in the system
def getState():
    userInput = 0
    while(True):
        if userInput == 0:
            print "--------------------------------------------"
            print "GET STATEMENTS:"
            print "--------------------------------------------"
            print "1.- Get character with most likes"
            print "2.- Get character's game"
            print "3.- Order characters DESC based on their chronological release date"
            print "4.- Get character's franchise"
            print "5.- Get character's moves!"
            print "6.- Get character's certain move (from list in moves)"
            print "7.- Order characters based on their tier, display name"
            print "8.- Get comments made about certain character (ask for char) display char and comment"
            print "9.- Check if user with same username or password is in the system"
            print "0   <<PRINT MENU AGAIN>>"
            print "-1  <<BACK TO MAIN MENU>>"
            print "--------------------------------------------"
        userInput = raw_input(">> ")
        userInput = int(userInput) 
        if userInput == 1:
            print "HELLO"
        elif userInput == -1:
            print "Back To Main Menu"
            return 

#PRINT MENU
while(True):
    print "-----------------------"
    print "SELECT TYPE OF QUERY:"
    print "-----------------------"
    print "1.- INSERT STATEMENTS"
    print "2.- GET STATEMENTS"
    print "3.- UPDATE STATEMENTS"
    print "-1  <<EXIT DATABASE>>"
    print "-----------------------"

    userInput = raw_input(">> ")
    userInput = int(userInput)

    if userInput == 1:
        insertState()
    elif userInput == 2:
        getState()
    elif userInput == 3:
        updateState()
    elif userInput == -1:
        exit()
        print "BYE!!"
        break
