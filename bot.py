import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set in the environment variables.")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    await bot.load_extension('commands.music_commands')
    # await bot.load_extension('commands.utility_commands')
    # await bot.load_extension('commands.moderation_commands')
    # await bot.load_extension('events.on_member_join')

# เริ่มต้นบอท
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Main function to run the bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

# Run the bot
asyncio.run(main())
