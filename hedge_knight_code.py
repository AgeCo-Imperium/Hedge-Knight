import discord
from discord.ext import commands

#This makes it so typing hk.commandname makes the bot perform a specific command
client = commands.Bot(command_prefix = "hk.")


#New Event, prints to IDLE on running to alert that its working
@client.event
async def on_ready():
    
    print("Hedge Knight is working.")
    
#End of Event



#New Event, prints that's a bruh moment when you type hk.bruhthem
@client.command()
async def bruhthem(ctx):
    
    await ctx.send("That's a bruh moment...")
    
#End of Event



#New Event, when someone types trumpdog the bot will print the emote (THIS DOES NOT WORK YET)
@client.event
async def on_message(message):

    #This line makes sure the bot does not respond to its own message
    if client.user.id != message.author.id:
        #If trumpdog is somewhere in the message await for the bot to send a given message.
        if "trumpdog" in message.content:
            await channel.send("<:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441>")

    await client.process_commands(message)   

#End of Event



#Put in bot token --> bot will go online
client.run("")
