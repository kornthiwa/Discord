from discord.ext import commands

class UtilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

# เพิ่ม Cog นี้เข้าไปใน bot
def setup(bot):
    bot.add_cog(UtilityCommands(bot))
