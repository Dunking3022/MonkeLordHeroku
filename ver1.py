import sqlite3
import datetime
import random 


print(datetime.date.today())
handle = sqlite3.connect('apedatabase.sqlite')
cursor = handle.cursor()

def top():
    cursor.execute('SELECT username from main ORDER by money DESC LIMIT 5;')
    toplist = cursor.fetchall()
    print(toplist)
    
def daily(id):
    cursor.execute('SELECT lastdaily,money from main where username = ?',(str(id),))
    lastdaily = cursor.fetchone()
    print("Last Daily Date - ",lastdaily[0])
    if (lastdaily[0]) < str(datetime.date.today()):
        dailyamt = random.choice(["10","50","20","100"])
        print("Adding ",dailyamt," to user's account")
        cursor.execute("update main set money = ? where username = ?",((int(lastdaily[1])+int(dailyamt)),id))
        cursor.execute("UPDATE main set lastdaily = ? where username = ?",(datetime.date.today(),id))
        print("All done for today")
        handle.commit()
        cursor.execute('SELECT lastdaily,money from main where username = ?',(str(id),))
        print("Rechecking money")
        temp = cursor.fetchone()
        print(temp)
        return(dailyamt,str(int(lastdaily[1])+int(dailyamt)))
        
    else:
        print("Can't do for today ")
        return(None)
        cursor.commit()
