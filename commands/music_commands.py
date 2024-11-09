import discord
from discord.ext import commands
from models.music_queue import MusicQueue
from models.music_playing import MusicPlaying


class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.music_queue = MusicQueue()
        self.music_playing = MusicPlaying()

    @commands.command()
    async def play(self, ctx: commands.Context, url: str):
        await self.music_playing.play_song(ctx, url)

    @commands.command()
    async def pause(self, ctx):
        if self.music_playing.is_playing():
            self.music_playing.pause()
            await ctx.send('เพลงถูกหยุดชั่วคราว')
        else:
            await ctx.send('ไม่มีเพลงที่กำลังเล่นอยู่')

    @commands.command()
    async def stop(self, ctx):
        self.music_playing.stop()
        await ctx.send('เพลงถูกหยุด')

    @commands.command()
    async def resume(self, ctx):
        if self.music_playing.is_paused():
            self.music_playing.resume()
            await ctx.send('เล่นเพลงต่อ')
        else:
            await ctx.send('ไม่มีเพลงที่หยุดชั่วคราว')

    @commands.command()
    async def skip(self, ctx):
        next_song = self.music_queue.get_next_song()
        if next_song:
            self.music_playing.play(next_song)
            await ctx.send(f'ข้ามไปยังเพลงถัดไป: {next_song}')
        else:
            await ctx.send('ไม่มีเพลงในคิว')

# เพิ่ม Cog นี้เข้าไปใน bot
async def setup(bot: commands.Bot):
    await bot.add_cog(MusicCommands(bot))
