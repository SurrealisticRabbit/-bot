import discord
from discord.ext import commands
from commands.base import BaseCommands
from commands.music import MusicCommands

class AlphaBot(commands.Bot):
    def __init__(self) -> None:
        self._intents = discord.Intents.default()
        self._intents.message_content = True
        self._intents.members = True
        self._intents.guilds = True
        self._intents.presences = True
        self._intents.voice_states = True
        super().__init__(command_prefix="!", intents=self._intents)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")
        
    async def setup_hook(self) -> None:
        print("Setting up commands...")
        await self.add_cog(BaseCommands(self))
        print("Setting up Music commands...")
        await self.add_cog(MusicCommands(self))
        print("Syncing commands...")
        await self.tree.sync()
        print("Commands synced!")