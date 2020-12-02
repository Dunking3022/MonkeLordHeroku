
import sqlite3

handle = sqlite3.connect('apedatabase.sqlite')
cursor = handle.cursor()
    
def userverification(username):
    cursor.execute('SELECT * FROM main where Username = ?;',(username,))
    returnedstuff = cursor.fetchall()
    if returnedstuff == []:
        return("Failed")
    else:
        return("Passed")

def createaccount(username,dctag):
    handle.execute('INSERT INTO Main(Username,dctag) VALUES(?,?);',(username,dctag))

def stats(username):
    cursor.execute('SELECT * FROM main where Username = ?;',(username,))
    returnedstuff = cursor.fetchall()
    if returnedstuff == []:
        return None
    else:
        return returnedstuff

def transfer(fromacc,toacc,amt):
    cursor.execute('select money from main where username = ?',(fromacc,))
    bal = str(cursor.fetchone()[0])
    if(int(bal)>int(amt)):
            cursor.execute('UPDATE main set money = money + ? where username = ? ',(amt,toacc))
            cursor.execute('UPDATE main set money = money - ? where username = ? ',(amt,fromacc))
            print("Succesfully transferred ")
            return("Success")
    else:
        print("Transaction Failed")
        return("Failed")
def updatedb():
    handle.commit()
    
def getdctag(id):
    cursor.execute('select dctag from main where username = ?',(id,))
    output = cursor.fetchone()
    return(output[0])
    