import discord
from discord.ext import commands
from discord import app_commands
from util.music import LocalSong

class LocalMusicPlayer():
    def __init__(self) -> None:
        self.queue: list[LocalSong] = []
        

class MusicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="play_local", description="Play a local music file"
    )
    async def play_local(self, interaction: discord.Interaction, path: str):
        song = LocalSong()
        song.path = path
        song.title = path.split("/")[-1]
        
        await interaction.response.send_message(f"🎵 Now playing: **{song.title}**", ephemeral=True)


