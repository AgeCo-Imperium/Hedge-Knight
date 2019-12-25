import discord
from discord.ext import commands

#This makes it so typing hk.commandname makes the bot perform a specific command
client = commands.Bot(command_prefix = "hk.")

@client.event
async def on_ready():
    print("Hedge Knight is working.")

client.run("NjU4MDI0OTMwNTE2MTQwMDMz.XgKzkQ.hj4n76bZb0mmqcPUsmx5-14JA0A")
