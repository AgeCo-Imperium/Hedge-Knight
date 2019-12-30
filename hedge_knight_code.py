import discord
import random
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
async def bruh(ctx):
    
    await ctx.send("That's a bruh moment...")
    
#End of Event


    
#New Event, prints oh wow if someone says wow
@client.event
async def on_message(message):

    if "trumpdog" in message.content:
        await message.channel.send("<:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441> <:TrumpDog:639548018231869441>")
                               
#End of Event



#Put in bot token --> bot will go online
client.run("")
