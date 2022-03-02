import discord
import credentials as cr
import requests
import json
import random

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

comment_list = [
    "Hmmm...",
    "For sure.",
    "I don't know about that",
    "I concur.",
    "Ok...",
    "lol",
    "You would say that!"
]

client = discord.Client()

@client.event
async def on_ready():
    print(client.user, "has connected to Discord!")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
    if "belamy" in str(message.content).lower():
        msg = "That's my name. don't wear it out!"
        await message.channel.send(msg)
    
    n = random.choice(1,100)
    if n == 10:
        comment = random.choice(comment_list)
        await message.channel.send(comment)      
    
client.run(cr.bot_token)