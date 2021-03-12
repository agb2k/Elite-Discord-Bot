import discord
import random
import json
import os

# Connect to discord server
client = discord.Client()


# Function to get a quote
def get_quote():
    n = random.randrange(0, 8)
    with open("quotes.json") as data:
        quotes_json = json.load(data)

    quote = "\"" + quotes_json[n]["Quote"] + "\" - " + quotes_json[n]["Name"]

    return quote


# Asynchronous function to take place when bot is ready
@client.event
async def on_ready():
    print("Logged in as {0.user}!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "ur mum" in message.content.lower():
        await message.channel.send("Shut up!")
    if "avatar" in message.content.lower():
        await message.channel.send("Get a life, Jude!")
    if "nice" in message.content.lower():
        await message.channel.send("Is it nice tho???")
    if message.content.lower().startswith("hi"):
        await message.channel.send("Hi bro")
    if message.content.lower().startswith("that's what she said"):
        await message.channel.send("That is not and will never be what she says, bro")
    if "samima" in message.content.lower():
        await message.channel.send("Lifehack #420: Mention you're Munavar's friend for a discount in Samima. Stonks!!!")
    if message.content.startswith("$quote"):
        quote = get_quote()
        await message.channel.send(quote)

# Keeps password hidden from y'al
token = os.environ.get('Elite_Bot_Token')
client.run(token)
