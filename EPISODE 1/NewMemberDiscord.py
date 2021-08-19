import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import requests
import io

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
	print("Bot connected")


@bot.event
async def on_member_join(member):
	channel = bot.get_channel(877776051688833024)
	img = Image.open("canvas.jpg").resize((400, 200), Image.ANTIALIAS)
	url = str(member.avatar_url)

	response = requests.get(url, stream=True)
	response = Image.open(io.BytesIO(response.content))
	response = response.convert("RGBA")
	response = response.resize((100, 100), Image.ANTIALIAS)

	img.paste(response, (15, 15, 115, 115))

	idraw = ImageDraw.Draw(img)
	font = ImageFont.truetype("marvin.ttf", size=20)

	idraw.text((130, 30), f"{member}", font=font)

	img.save("banner.jpg")
	await channel.send(file=discord.File(fp="banner.jpg"))

bot.run("token")