import os
import discord
from dotenv import load_dotenv
from alpaca import Alpaca

load_dotenv()
TOKEN: str | None = os.getenv("DISCORD_TOKEN")

if __name__ == "__main__":
    bot = Alpaca(command_prefix="!", intents=discord.Intents.default())
    bot.run(TOKEN)
