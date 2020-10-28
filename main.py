import os
import discord
import random
import gpt_2_simple as gpt2
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

probability = 50

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    print(message)
    global probability
    if message.author == client.user:
        return
    if message.content.startswith("/probability "):
        try:
            newProb = int(message.content.split(" ")[1])
            if newProb < 0:
                await message.channel.send("Probability must be greater than 0.")
            else:
                probability = newProb
                await message.channel.send("Will now generate text approximately 1 every " + str(probability) + " messages.")
        except:
            await message.channel.send("Could not parse a number from your message.")

    else:
        if probability != 0:
            if random.randint(1, probability) == 1:
                reply = gpt2.generate(sess, length=100, return_as_list=True)[0]
                await message.channel.send(reply)

client.run(TOKEN)
