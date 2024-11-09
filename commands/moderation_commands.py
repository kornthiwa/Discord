from discord.ext import commands

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} ถูกเตะออกจากเซิร์ฟเวอร์')

# เพิ่ม Cog นี้เข้าไปใน bot
def setup(bot):
    bot.add_cog(ModerationCommands(bot))
