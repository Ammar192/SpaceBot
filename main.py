import discord
import json
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("Bot logged in")

@client.event
async def on_message(msg):
    if msg.content.startswith('$image'):
      info = get_image()
      print(info)
      await msg.channel.send(info["title"] + ": " + info["explanation"])
      await msg.channel.send(info["url"])

def get_image():
  res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
  json_data = json.loads(res.text)
  # print(json_data["date"])
  return json_data

client.run("ODAwMTM0OTE5MDM1NTUxNzc1.YANttg.mkoWDZGsgla81OBIF-IEmKZk_dQ")