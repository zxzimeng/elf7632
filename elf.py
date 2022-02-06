import discord
from discord import user
from dotenv import load_dotenv
from datetime import date
import calendar
import ast
import re

load_dotenv()
TOKEN = 'OTE1NzU1MDE5NDczNjY2MDQ4.YagNUg.qxaVtKg2Px3vd7obq2Fw147wqyE'
GUILD = 'Secret Santa'

client = discord.Client()


@client.event
async def on_ready():
  global zaria, carlos, elaine, darlene, accepted_channels, question_channel
  zaria = await client.fetch_user(880981393738436648)
  carlos = await client.fetch_user(873212295684173904)
  elaine = await client.fetch_user(769732076811059230)
  darlene = await client.fetch_user(695785055573770281)
  question_channel = client.get_channel(915757856924508181)
  accepted_channels = [915761501598531665, 915761610717548635, 915761658251603989, 915761702044303411]
  for guild in client.guilds:
    if guild.name == GUILD:
      break

  print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n')
  print("Elf's Ready!")


@client.event
async def on_message(message):
  global zaria, carlos, elaine, darlene, accepted_channels, question_channel

  if message.author == client.user:
    return 
  
  userMsg: str = str(message.content)
  messageChannel = str(message.channel)
  messageAuthor = str(message.author)
  authorDiscrimator = message.author.discriminator
  serverID = message.guild.id
  channelID = message.channel.id

  if channelID in accepted_channels:
    await message.channel.purge(limit=1)
    await question_channel.send(userMsg + '\n@everyone')

  print(f"""
  Message: {userMsg}
  Channel: {messageChannel}
  Channel ID: {channelID}
  Author: {messageAuthor}
  Author Discrimator: {authorDiscrimator}
  Server ID: {serverID}
  """)

  


client.run(TOKEN)
