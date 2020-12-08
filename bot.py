import discord
from discord.ext import commands
import random
import os

teksty = [" to śmieć"," jest jebaną pałą"," chuj ci na starego"," miesza bigos łokciem"," pal gume"," do berła"," wyjmij chuja z mordy"," rucham ci matke z całej epy", " pal gume naleśniku jebany"," matka ci sie puszcza"," sklej pizde flecie"," nie bądź taki do przodu bo Cię sznurówk wyprzzedzają"," jesteś rozwinięty jak papier toaletowy"," teraz mi przykro :("," widziałem Cię w sklepie rowerowym na półce z pedałami flecie"]
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")
sendMessage = await message.channel.send
@client.event
async def on_message(message):
    if message.content.find("rudy.losuj") != -1:
        players = message.content
        players = str(players)[11:].split(' ')
        if(len(players)==10):
            random.shuffle(players)
            response = "**Team1**\n"+players[0]+"\n"+players[1]+"\n"+players[2]+"\n"+players[3]+"\n"+players[4]+"\n"+"\n"+"**Team2**\n"+players[5]+"\n"+players[6]+"\n"+players[7]+"\n"+players[8]+"\n"+players[9]+""
            sendMessage(response)
        else:
            sendMessage("Ma być 10 zawodników pajacu")

    elif message.content.find("rudy to ") != -1:
        author = (str(message.author))[:-5]
        if(author == "Marcin1"):
            sendMessage("Dobrze, postaram się zmienić D:")
        else:
            random.shuffle(teksty)
            sendMessage(author+teksty[0])
    elif message.content.find("rudy to") != -1:
        author = (str(message.author))[:-5]
        sendMessage(author+" nie bądź taki hej do przodu bo Ci tyłu zabraknie cwaniaczku")

    elif message.content.find("bajo jajo") != -1:
        sendMessage("Ty pojebie kurwa się zamknij tam kurwa a nie bajoo jajo ty pierdolony chamie")
        
client.run(token)


