from models.music_queue import MusicQueue
import discord
from discord.ext import commands
import yt_dlp
import asyncio
from utils.helpers import get_youtube_link, ffmpeg_options, youtube_watch_url, yt_dl_song_options, yt_dl_playlist_options

class MusicPlaying:
    def __init__(self):
        self.ytdl_song = yt_dlp.YoutubeDL(yt_dl_song_options)
        self.ytdl_playlist = yt_dlp.YoutubeDL(yt_dl_playlist_options)
        self.music_queue = MusicQueue()
        self.voice_clients = {}

    async def play_song(self, ctx: commands.Context, song_url):
        voice_client: discord.VoiceClient = self.voice_clients.get(ctx.guild.id)

        if not voice_client or not voice_client.is_connected():
            voice_client = await self.connect_to_voice_channel(ctx)
            
        loop = asyncio.get_event_loop()
        if '&list=' in song_url:
            await self.download_playlist_info(ctx, song_url)
            await self.play_next(ctx)
            return

        song = get_youtube_link(song_url)
        data = await loop.run_in_executor(None, lambda: self.ytdl_song.extract_info(song, download=False))
        if voice_client.is_playing():
            self.music_queue.add_queue(ctx.guild.id, data)
            return

        player = discord.FFmpegOpusAudio(data['url'], **ffmpeg_options)
        voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), loop))

    async def play_next(self, ctx: commands.Context):
        if song := self.music_queue.pop_queue(ctx.guild.id) or self.music_queue.pop_playlist(ctx.guild.id):
            await self.play_song(ctx, youtube_watch_url + song['id'])
        else:
            await ctx.send("ไม่มีเพลงในคิว")

    async def download_playlist_info(self, ctx: commands.Context, playlist_link):
        loop = asyncio.get_running_loop()
        song_info = await loop.run_in_executor(None, lambda: self.ytdl_playlist.extract_info(playlist_link, download=False))
        playlist_data = [
            {'id': e['id'], 'url': e['url'], 'title': e['title'], 'channel': e['uploader']}
            for e in song_info.get('entries', []) if e['id'] not in {song['id'] for song in self.music_queue.playlists.get(ctx.guild.id, [])}
        ]
        self.music_queue.add_playlist(ctx.guild.id, playlist_data)
      
    async def connect_to_voice_channel(self, ctx: commands.Context):
        if ctx.author.voice and ctx.author.voice.channel:
            try:
                voice_client = await ctx.author.voice.channel.connect()
                self.voice_clients[ctx.guild.id] = voice_client
                return voice_client
            except discord.ClientException:
                await ctx.send("บอทไม่สามารถเชื่อมต่อกับห้องเสียงได้")
                return None
        else:
            await ctx.send("คุณต้องอยู่ในห้องเสียงเพื่อใช้คำสั่งนี้")
            return None