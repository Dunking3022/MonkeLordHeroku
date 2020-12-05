import pyrebase

config = {
  "apiKey": "AIzaSyCQwDyYLNLajDckw657zOJcBPrrnA3rkkQ",
  "databaseURL" : "https://monkebot-3022.firebaseapp.com",
  "authDomain" : "monkebot-3022.firebaseapp.com",
  "projectId": "monkebot-3022",
  "storageBucket": "monkebot-3022.appspot.com",
  "messagingSenderId": "472392599751",
  "appId": "1:472392599751:web:da72d6613f7d4aefcb16e2",
  "measurementId": "G-4F6NM2WT5H"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

def updown(choice,path_local,path_on_cloud):
  if choice == "u":
      storage.child(path_on_cloud).put(path_local)
  if choice == "d":
      storage.child(path_on_cloud).download(filename = "test_download.jpg", path = "images/MonkeBot.jpg")
      
def updb(choice):
  if choice == "u":
    storage.child('db/apedatabase.sqlite').put('apedatabase.sqlite')
  if choice == "d":
    storage.child('db/apedatabase.sqlite').download(filename = 'apedatabase.sqlite',path = 'db/apedatabase.sqlite')

updb('u')