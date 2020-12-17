print("Initializing")
import discord
import monkeymanager
import ver1
import random
from updown import *
#Initialize and declare some global variables

client = discord.Client()

token = ""

commands = ['help','bless','go','flip','register',"stats","transfer","daily",'play','top']

bothelp = open('bin/logs/monkehelp.txt','r+').read()
statusdict = {'online': discord.Status.online,
                              'dnd' : discord.Status.dnd,
                              'idle' : discord.Status.idle,
                              'invisible' : discord.Status.invisible}


#mention function
def mention(id):
    authorname = "<@!" + str(id) + ">"
    return authorname
 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The World Return To Monke"))
    updb('d')
    print("Succesfully recieved databsae from firebase")

@client.event
async def on_connect():
    await client.change_presence(status = discord.Status.online)
    print("Monke Lord with id",client.user," initialized with latency ",client.latency,"\nListening for new messages.\n")
    
@client.event

async def on_message(message):

#monke checks if people want him to read the message or not

    if message.content.startswith('!monke'):
        
        #-----Message Log (For Debugging)----------
        print("--------New Message Alert--------","\nAuthor - ",message.author,"\nMessage - ",message.content,"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
        message.content.lower()
        if message.author == client.user:
            return
        messageid = message.content.split()
        authorname = mention(message.author.id)
        dctag = message.author
        
        if messageid[1] in commands:
                
            
            
    #Bless Function --> Requires user to call monke and use the argument bless 
            if len(messageid)<2 or messageid[1] == "help":
                
        #<Help> --> Ask Monkey for the existing commands. Gives the user all possible commands from the documentation
                embedhelp1 = discord.Embed(title = "Monke Lord", description = "****Created by thy holy hamster - Inferio#5558\n\n*Version - 1.1*\n\nuse prefix **!monke** followed by one of the commands", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                embedhelp1.add_field(name = "**Casual Commands :**",value  = "*Just some random commands*",inline=False)
                embedhelp1.add_field(name = "help", value = "Lists version status all the commands that can be used with the bot.", inline =True)
                embedhelp1.add_field(name = "bless", value = "Monke lord blesses you. Probably the best thing that'll happen to you today. ", inline =True)
                embedhelp1.add_field(name = "go <___>", value = "Makes the bot change his status to your choice. Options include - ```online, idle, dnd, invisible``` ",inline = "False")
                embedhelp1.add_field(name = "**Economy Commands :**", value = "*Moneh related commands*",inline = False )
                embedhelp1.add_field(name = "register", value = "Creates an account for you in the Monke Bank.", inline =True)
                embedhelp1.add_field(name = "stats", value = "Displays your stats. As simple as that.", inline =True)
                embedhelp1.add_field(name = "daily", value = "Adds as small amount of money into your account but you can use it only once a day!",inline = True)
                embedhelp1.add_field(name = "transfer", value = "Used to transfer moneh into someone else's account. \nSyntax to be used - ```!monke transfer @user amount```",inline = False)
                embedhelp1.add_field(name = "-------------------------------Secret Notice-------------------------------", value = "||There's a hidden feature in this version. The first person to find it and report it to <@!338615698937085963> will get 1000 monke moneh so be on the lookout||",inline = False)
                embedhelp1.set_footer(text = "©Inferio 2020",icon_url= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fe7at4b7ctun41.jpg&f=1&nofb=1")
                embedhelp1.set_image(url ="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.0LYcpWEci69KqEETC2Fm_gHaEK%26pid%3DApi&f=1" )
                await message.channel.send(embed = embedhelp1)
                
                
            else:
                
                
    #Main Functions       

                #Bless --> mentions the user and blesses em.
        
                if messageid[1] == "bless":
                    fmessage = authorname + ", you have been blessed by the Holy Monke."
                    
                    imembed = discord.Embed(description = fmessage) #creates embed
                    file = discord.File("Images/monkebless.jpeg", filename="image.png")
                    imembed.set_image(url="attachment://image.png")
                    await message.channel.send(file=file, embed=imembed)
                    print("\n")

                #Change Status --> Changes the active status of bot depend on given argument

                if messageid[1] == "go":
                    print("Recieved request to change Status")
                    try:
                        await client.change_presence(status = statusdict[messageid[2]])
                        await message.channel.send("Roger! I'll set my status as " + messageid[2] + " from here on." )
                    except:
                        await message.channel.send(r'Please use one of the following \'\'\'online,dnd,idle,invisible\'\'\'')
                    
        #Coinflip  ------------------------------------------------
                if messageid[1] == "flip":
                    print("Flipping monkey")
                    flipresult = random.choice(["heads","tails"])
                    await message.channel.send("Monke flipped a coin and got "+flipresult)
            
                if messageid[1] == "top":
                    updb('d')
                    top = ver1.top()
                    print(top)
                    out = "Top Users :"
                    nolist = ['🥇','🥈','🥉','🎁','🍌']
                    _ = 0
                    await message.channel.send("🎉 Top Users Across The Server 🎉")
                    for user in top:
                        id = user[0][3:21]
                        print(id)
                        temuser = await client.fetch_user(int(id))
                        print(message.author)
                        arl = temuser.avatar_url
                        statsembed = discord.Embed()    
                        statsembed.set_author(name = nolist[_])
                        statsembed.add_field(name = "Username :",value = str(user[0]))
                        statsembed.set_footer(text = "Monke Money : "+str(user[1]), icon_url = "https://opengameart.org/sites/default/files/01coin.gif")
                        statsembed.set_thumbnail(url = arl)
                        print("Embed Ready to send.")
                        await message.channel.send(embed = statsembed)
                        out =  out + user[0]
                        _+=1
                    
                
            
                                
    #---------Monke Moneh Starts Here---------------------------------------------------------------------------------------------------------

    #) 1) - Register

                if messageid[1] == "register":
                    updb('d')
                    print("\nAttempting to register a new user -> ",message.author)
                    try:
                        monkeymanager.createaccount(str(authorname),str(dctag))
                        monkeymanager.updatedb()
                        await message.channel.send("Thanks for registering in the Monke Council, "+authorname+". You can access your account at anytime and make transactions. And yeah, Don't forget to ***INVEST***!!!!!")
                        print("\n\nNew Account registered with UserID - ",authorname," belonging to ",message.author)
                        updb('u')
                    except :
                        await message.channel.send("Sorry, you cannot register as an account named "+authorname+" already exists. Please contact the moderators if this is a mistake. ")
                        print("\n\nAccount Registration Failed.")
                    
    #) 2) - Stats
                if messageid[1] in ["stats","transfer","daily"]:
                    updb('d')
                    if monkeymanager.verify(authorname) == "Passed":        
                        if messageid[1] == "stats":
                            if messageid[2] == "":                  
                                print("Retrieving stats of ",dctag,' from the database')
                                stats = monkeymanager.stats(authorname)
                                print("Stats recieved - ",stats)
                                if stats == None:
                                    print("Failed to retrieve stats. No account with current username exists.")
                                    await message.channel.send("You can't view your stats unless you have an account dum dum. Now go make an account using !monke register and ***INVEST!!!!***")
                                else:
                                    statsembed = discord.Embed()    
                                    statsembed.set_author(name = "User Information", icon_url = "https://i.pinimg.com/originals/83/0e/21/830e214cee0748514579bbddf1d431f8.gif")
                                    statsembed.add_field("Username : " ,value = str(dctag).split('#')[0],inline = False)
                                    statsembed.add_field(name = "**Last Use of Daily Command -** ",value = stats[0][3],inline = False)
                                    statsembed.set_footer(text = "Monke Money : "+str(stats[0][1]), icon_url = "https://opengameart.org/sites/default/files/01coin.gif")
                                    statsembed.set_thumbnail(url = message.author.avatar_url)
                                    print("Embed Ready to send.")
                                    await message.channel.send(embed = statsembed)
                            else:
                                id = monkeymanager.stats(messageid[2])
                                if id == None:
                                    print("Failed to retrieve stats. No account with current username exists.")
                                    await message.channel.send("Failed To retrieve stats. No account with current username exists.")
                                else:
                                    rmoneh = id[0][1]
                                    rid = id[0][0].split('!')[1].split('>')[0]                                
                                    temuser = await client.fetch_user(int(rid))
                                    arl = temuser.avatar_url
                                    statsembed = discord.Embed()    
                                    statsembed.set_author(name = "User Information", icon_url = "https://i.pinimg.com/originals/83/0e/21/830e214cee0748514579bbddf1d431f8.gif")
                                    statsembed.add_field(name = "Username" ,value = id[0][2],inline = False)
                                    statsembed.add_field(name = "Last Use of Daily Command",value = id[0][3],inline = False)
                                    statsembed.set_footer(text = "Monke Money : "+str(id[0][1]), icon_url = "https://opengameart.org/sites/default/files/01coin.gif")
                                    statsembed.set_thumbnail(url = arl)
                                    print("Embed Ready to send.")
                                    await message.channel.send(embed = statsembed)
                                    
                #) 3) - Transfer
                        if messageid[1] == "transfer":
                            #try:
                            await message.channel.send("Transaction started!")
                            try:
                                debiter = authorname
                                crediter = messageid[2]
                                if '!' in crediter:
                                    print("messageid[2] already includes !")
                                else:
                                    print(crediter)
                                    screditer = crediter.split('@')
                                    crediter = screditer[0]+"@!"+screditer[1]
                                print("Debiter :",debiter,"\nCrediter :",crediter)
                                creditertag = monkeymanager.getdctag(crediter)
                                amt = messageid[3]
                            
                                status = monkeymanager.transfer(debiter,crediter,amt)
                                if status == "Success":
                                    monkeymanager.updatedb()
                                    print("Transaction Succesful")
                                    transembed = discord.Embed(title = "Transaction Successful", description = "From : "+str(message.author)+"\nTo: "+str(creditertag), url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  
                                    transembed.set_footer(text = "Moneh Transferred : "+amt, icon_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.iheart.com%2Fv3%2Fre%2Fnew_assets%2F5966c663fc45646e4b88fe9e&f=1&nofb=1")
                                    transembed.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fz4nxull42wt31.png&f=1&nofb=1")
                                    await message.channel.send(embed = transembed)
                                    updb('u')
                                else:
                                    await message.channel.send("Transaction Failed. Please confirm if you have enough balance in your account.")
                                    transembed = discord.Embed(title = "Transaction Failed", description = "You don't have enough monke moneh :", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  
                                    transembed.set_footer(text = "Moneh Transferred : 0", icon_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.iheart.com%2Fv3%2Fre%2Fnew_assets%2F5966c663fc45646e4b88fe9e&f=1&nofb=1")
                                    transembed.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FeR2N-T-SNsg%2Fmaxresdefault.jpg&f=1&nofb=1")
                                    await message.channel.send(embed = transembed)
                            except:
                                await message.channel.send("Transaction Failed. Please use the correct syntax and confirm if the recipient has a Monke Council Account.")
                                await message.channel.send("```!monke transfer @user amount```")        
                            
            #) 4) - Daily 
                        if messageid[1] == "daily":
                            result = ver1.daily(authorname)
                            
                            if result == None:
                                print("Already done for today.")
                                await message.channel.send("Sorry sire, you've used this command already today. But don't fret, wait till tommorow and you can use it again!")
                            else:
                                await message.channel.send("OMG SIR YOU WON **"+str(result[0])+"COINS **!!! Your current account balance is "+str(result[1]))
                                monkeymanager.updatedb()
                                updb('u')
                    else:
                        await message.channel.send("Sorry but you're not registered with the Monke Council. Please create an account using !monke register to use this command.")
        else:
            await message.channel.send("Sorry but there's no command ") 

            
#run-client
client.run(token)

