import sqlite3 as lite
from sqlite3.dbapi2 import connect
import sys

con = lite.connect("db/Diary.db")

def createUserTable():
    
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY, Name TEXT, Password TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS Entries(Id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Body TEXT)")

def saveUser(name, password):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Users (Name, Password) VALUES ('"+ name +"', '" + password + "')")

def readUser():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        return cur.fetchall()

def saveEntry(title, body):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Entries (Title, Body) VALUES ('" + title + "', '" + body + "')")