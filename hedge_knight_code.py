import discord
import random
import asyncio
from itertools import cycle
from discord.ext import commands

#This is where global variables go
playerone = None
playertwo = None
counter = 0

#This makes it so typing hk.commandname makes the bot perform a specific command
client = commands.Bot(command_prefix = "hk.")



#---------------LIST OF EVENTS-------------#



#This event will notify the writer in the IDLE that the bot is online and ready for use
@client.event
async def on_ready():
    
    print("Hedge Knight is working.")
    
#End of Event


    
#This event will update the counter every second and reset after five minutes by default
async def countertrack():

    #This pulls in required global variables into this function
    global counter

    #This means the loop wont work until the bot is finished with the on_ready event
    await client.wait_until_ready()

    #While the bot is running loop
    while True:

        #increment counter
        counter += 1

        #After five minutes (three hundred seconds) reset the counter
        if counter == 300:

            counter = 0

        #Before restarting the loop wait one second
        await asyncio.sleep(1) 
    
#End of Event



#This event will print the trumpdog emote is a message has the word "trumpdog" in it
@client.event
async def on_message(message):

    #Logic statement where if trumpdog is in the newest message it spams the trumpdog emote 
    if "trumpdog" in message.content:
        
         await message.channel.send("<:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441>")

    #This line is needed to ensure other commands can be used while it watches for trumpdog
    await client.process_commands(message)

#End of Event


    
#This event will add the user to be player one or player two and wont add them if they are already one of the players or there are two players
@client.command()
async def joingame(ctx, member: discord.Member = None):

    #This pulls in required global variables into this function
    global playerone
    global playertwo

    #Three logic statements where 
    if playerone is None:

        #playerone becomes the person who started the command and the bot sends a message notifying the user they are player one.
        playerone = ctx.message.author
        await ctx.send("You are player one.")

    elif playerone is not None and playertwo is None:

        #Two logic statements where it checks if the user is already in the place of player one
        if ctx.message.author is not playerone:

            #playertwo becomes the user and the bot sends a message notifying the user they are now player two
            playertwo = ctx.message.author
            await ctx.send("You are player two.")

        elif ctx.message.author is playerone:

            #Alerts user they are already player one 
            await ctx.send("You are already in the game.")

    elif playertwo and playerone is not None:

        await ctx.send("There are already two players.")
        
#End of Event


        
#New Event, removes a user from playerone and playertwo if they currently occupy one or the other
@client.command()
async def leavegame(ctx, member: discord.Member = None):

    #This pulls in required global variables into this function
    global playerone
    global playertwo

    #Three logic statements where it's dedicated to finding who the user who used the command is and then removing them from the variable
    if ctx.message.author is playerone:

        playerone = None
        await ctx.send("You are no longer player one.")
        
    elif ctx.message.author is playertwo:
        
        playertwo = None
        await ctx.send("You are no longer player two.")
        
    elif ctx.message.author is playertwo:
       
        await ctx.send("You did not join the game in the first place.")
                
#End of Event



#---------------TESTING COMMANDS-------------#



#This test will send a message into the chat you ent the command in
@client.command()
async def brmo(ctx):
    
    await ctx.send("Thats a bruh moment...")
    
#End of Event



#This test checks the current status of the timecheck variable
@client.command()
async def timer(ctx):

    #This pulls the global variables into the function
    global counter
    
    await ctx.send(counter)
    
#End of Event



#This test checks if player one or player two are taken
@client.command()
async def players(ctx, member: discord.Member = None):

    #This pulls in required global variables into this function
    global playerone
    global playertwo

    #Four logic statements where each one checks if one, both, or none of the spots for players are taken up and prints result
    if playerone and playertwo is not None:
        
        await ctx.send(f"{playerone.name} is player one and {playertwo.name} is player two")
        
    elif playerone is not None and playertwo is None:
        
        await ctx.send(f"{playerone.name} is player one, there is no player two")

    elif playerone is None and playertwo is not None:
                
        await ctx.send(f"There is no player one but player two is {playertwo.name}")
        
    elif playerone is None and playertwo is None:
                
        await ctx.send("There are no players")


#End of Event



#---------------END OF EVENTS---------------#

#Loops through the function waitcounter upon starting the bot
client.loop.create_task(countertrack())
 
#Put in bot token --> bot will go online
client.run("")
