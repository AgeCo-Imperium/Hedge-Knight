import discord
import random
from discord.ext import commands

#This is where global variables go
playerone = None
playertwo = None


#This makes it so typing hk.commandname makes the bot perform a specific command
client = commands.Bot(command_prefix = "hk.")



#New Event, prints to IDLE on running to alert that its working
@client.event
async def on_ready():
    
    print("Hedge Knight is working.")
    
#End of Event



#New Event, prints the trumpdog emote if someone says trumpdog in the chat
@client.event
async def on_message(message):

    #If statement, if trumpdog is in the lastest message then...
    if "trumpdog" in message.content:
        
        #In the channel where the message was sent, send the enclosed content
         await message.channel.send("<:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441>")

    #This line is needed to ensure other commands can be used, otherwise it always waits for trumpdog only   
    await client.process_commands(message)

#End of Event



#New Event, prints "that's a bruh moment" when you type hk.brmo (MOSTLY FOR TESTING)
@client.command()
async def brmo(ctx):
    
    await ctx.send("Thats a bruh moment...")
    
#End of Event



#New Event, used to assign playerone and playetwo and tie them with user ID's for games, if there is already a player one/two they can't play if they type this command.
@client.command()
async def joingame(ctx, member: discord.Member = None):

    #This pulls in the global playerone and playertwo variables into the function
    global playerone
    global playertwo

    #If statement, if playerone is not taken by anyone then...
    if playerone is None:

        #playerone becomes the person who started the command and the bot sends a message notifying the user they are player one.
        playerone = ctx.message.author
        await ctx.send("You are player one.")

    #(I) Else if statement, if there is a player one and player two is not taken then...
    elif playerone is not None and playertwo is None:

        #Nested if statement, if the person who started the command is not the same ID as player one then...
        if ctx.message.author is not playerone:

            #playertwo becomes the person who started the command and the bot sends a message notifying the user they are second place
            playertwo = ctx.message.author
            await ctx.send("You are player two.")

        #Else if statement, if the person who became player one uses the command again then they don't get the next spot, they are notified by message
        elif ctx.message.author is playerone:

            await ctx.send("You are already in the game.")

    #(II) Else if statement, if playerone and playertwo are both taken and not empty the notify the user they can't join
    elif playertwo and playerone is not None:

        await ctx.send("There are already two players.")
        
#End of Event


        
#New Event, removes a user from playerone and playertwo if they currently occupy one or the other
@client.command()
async def leavegame(ctx, member: discord.Member = None):

    #This pulls in the global playerone and playertwo variables into the function
    global playerone
    global playertwo

    #Three logic statements dedicated to finding who the user who used the command is and then removing them from the variable
    if ctx.message.author is playerone:

        playerone = None
        await ctx.send("You are no longer player one.")
        
    elif ctx.message.author is playertwo:
        
        playertwo = None
        await ctx.send("You are no longer player two.")
        
    elif ctx.message.author is playertwo:
       
        await ctx.send("You did not join the game in the first place.")
                
#End of Event



#New Event, gives both playerone and playertwo ID's from the global variables
@client.command()
async def players(ctx, member: discord.Member = None):

    #This pulls in the global variables into this function, if they are changed somewhere else then these variable will still change
    global playerone
    global playertwo

    #This is essentially four logic statements that test if playerone and playertwo re taken either at the same time or individually.
    if playerone and playertwo is not None:
        
        await ctx.send(f"{playerone.name} is player one and {playertwo.name} is player two")
        
    elif playerone is not None and playertwo is None:
        
        await ctx.send(f"{playerone.name} is player one, there is no player two")

    elif playerone is None and playertwo is not None:
                
        await ctx.send(f"There is no player one but player two is {playertwo.name}")
        
    elif playerone is None and playertwo is None:
                
        await ctx.send("There are no players")


#End of Event


 
#Put in bot token --> bot will go online
client.run("")
