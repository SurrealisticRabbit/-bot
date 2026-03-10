import discord
from discord.ext import commands

class AlphaBot(commands.Bot):
    def __init__(self) -> None:
        self._intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=self._intents)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")