import os
import discord
import random
import gpt_2_simple as gpt2
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

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
            new_prob = int(message.content.split(" ")[1])
            if new_prob < 0:
                await message.channel.send("Probability must be greater than 0.")
            else:
                probability = new_prob
                if probability = 0:
                    await mesage.channel.send("I'll stop talking completely until you change the probability again.")
                else:
                    await message.channel.send(f"I'll now generate text approximately 1 in every {probability} messages.")
        except:
            await message.channel.send("Could not parse a number from your message.")

    else:
        if probability != 0:
            if random.randint(1, probability) == 1:
                length = random.randint(25, 100)
                reply = gpt2.generate(sess, length=length, return_as_list=True)[0]
                await message.channel.send(reply)

client.run(discord_token)
