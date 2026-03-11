import discord
from discord.ext import commands
from discord import app_commands
from util.music import LocalSong
import os
from mutagen import File as MutagenFile

class LocalMusicPlayer():
    def __init__(self) -> None:
        self.queue: list[LocalSong] = []
        
    def _scan_music_dir(self):
        base_path = os.path.realpath("./music")
        if not os.path.exists(base_path):
            print(f"Directory {base_path} does not exist.")
            return

        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith(('.mp3', '.flac', '.wav', '.ogg')):
                    song_path = os.path.join(root, file)
                    song = LocalSong()
                    song.path = song_path
                    song.album = os.path.basename(root)
                    
                    audio = MutagenFile(song_path)
                    if audio:
                        song.title = str(audio.get('TIT2', audio.get('title', [file])[0]))
                        song.artist = str(audio.get('TPE1', audio.get('artist', ['Unknown'])[0]))
                        song.duration = int(audio.info.length) if hasattr(audio, "info") else 0
                        song.bitrate = int(audio.info.bitrate) if hasattr(audio, "info") and hasattr(audio.info, "bitrate") else 0
                        song.codec = type(audio).__name__
                    if not song.title:
                        song.title = file
                    
                    self.queue.append(song)
        
        if not self.queue:
            print("No music files found in the directory.")
                        

class MusicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self._vc = None
        self._voice_client = None
        self._player = None
        
    async def _connect_to_vc(self, interaction: discord.Interaction):
        self._vc = interaction.user.voice
        if not self._vc:
            await interaction.edit_original_response(content="You are not in a voice channel")
            return False
        self._voice_client = await self._vc.channel.connect()
        return True
        
    @app_commands.command(name="play", description="Play a local music file")
    async def play(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        if not await self._connect_to_vc(interaction):
            return
        
        self._player = LocalMusicPlayer()
        self._player._scan_music_dir()
        song = self._player.queue[0]
        self._voice_client.play(discord.FFmpegPCMAudio(song.path), after=lambda e: self._player.queue.pop(0))
        await interaction.edit_original_response(content=f"🎵 Now playing: **{song.title}**")
        
    async def stop(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        if not self._voice_client:
            await interaction.response.send_message("I am not connected to a voice channel", ephemeral=True)
            return
        self._voice_client.stop()
        await self._voice_client.disconnect()
        self._voice_client = None
        self._player = None
