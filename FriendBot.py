import discord
from discord.ext import commands

bot_token = "" # Your bot token
bot_prefix = "!"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

your_user_id = "" # Your user ID
friend_user_id = "" # Your friend's user ID

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.event
async def on_member_update(before, after):
    if after.id == friend_user_id:
        if before.status == discord.Status.offline and after.status == discord.Status.dnd:
            user = await bot.fetch_user(your_user_id)
            dm_channel = await user.create_dm()
            await dm_channel.send(f"{user.name}, your friend is now online in Do Not Disturb mode!")
        elif before.status == discord.Status.dnd and after.status == discord.Status.offline:
            user = await bot.fetch_user(your_user_id)
            dm_channel = await user.create_dm()
            await dm_channel.send(f"{user.name}, your friend has gone offline!")

bot.run(bot_token)
