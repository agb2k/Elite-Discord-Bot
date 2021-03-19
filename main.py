import discord
import random
import json
import os

# Connect to discord server
client = discord.Client()


# Function to get a quote
def get_quote():
    n = random.randrange(0, 13)
    with open("quotes.json") as data:
        quotes_json = json.load(data)

    quote = "\"" + quotes_json[n]["Quote"] + "\" - " + quotes_json[n]["Name"]

    return quote


# Asynchronous function to take place when bot is ready
@client.event
async def on_ready():
    print("Logged in as {0.user}!".format(client))


# Commands on message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "ur mum" in message.content.lower():
        await message.channel.send("Shut up!")
    if "avatar" in message.content.lower():
        await message.channel.send("Get a life, loser!")
    if "korra" in message.content.lower():
        await message.channel.send("Get a life, loser!")
    if message.content.lower().startswith("nice"):
        await message.channel.send("Is it nice tho???")
    if message.content.lower().startswith("hi") and message.content.split("hi")[1] == "":
        await message.channel.send("Hi bro")
    if message.content.lower().startswith("that's what she said") or message.content.lower().startswith("thats what "
                                                                                                        "she said"):
        await message.channel.send("That is not and will never be what she says, bro")
    if "samima" in message.content.lower():
        await message.channel.send("Lifehack #420: Mention you're Munavar's friend for a discount in Samima. Stonks!")
    if "abhi" in message.content.lower():
        await message.channel.send("I see you're talking to/about the coolest, smartest, hottest human to ever exist.")
    if "pravenash" in message.content.lower():
        await message.channel.send("Rackets, bro???")
    if "yash" in message.content.lower():
        await message.channel.send("Yash is busy drinking cold coffee in Canada at the moment. Please try again later")
    if "jude" in message.content.lower():
        await message.channel.send("Jude's busy watching Avatar right now")
    if "jeff" in message.content.lower():
        await message.channel.send("Kevin, bro???\n...\n...\n...\nYes, he is his bro")
    if "lol" in message.content.lower():
        await message.channel.send("Is it really that funny?")
    if "lmao" in message.content.lower():
        await message.channel.send("Is it REALLY that funny?????")
    if "wow" in message.content.lower():
        await message.channel.send("I don't really feel like THIS is a wow moment but you do you bro")
    if "bruh" in message.content.lower():
        await message.channel.send("bruhhhhh")
    if "shut up" in message.content.lower():
        await message.channel.send("no u")
    if "gay" in message.content.lower():
        await message.channel.send("It's 2021 bro")
    if "bye" in message.content.lower():
        await message.channel.send("Don't leave me! :(")
    if "lame" in message.content.lower():
        await message.channel.send("ur lame")
    if "suck" in message.content.lower():
        await message.channel.send("You suck!")
    if "no u" in message.content.lower():
        await message.channel.send("NO U")
    if "noice" in message.content.lower():
        await message.channel.send("cool cool cool")
    if message.content.startswith("!quote"):
        quote = get_quote()
        await message.channel.send(quote)

# Keeps password hidden from y'all
token = os.environ.get('Elite_Bot_Token')
client.run(token)
