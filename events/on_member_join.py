from discord.ext import commands
from discord import Member

class MemberJoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'ยินดีต้อนรับ {member.mention} เข้าสู่เซิร์ฟเวอร์!')

    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'{member.mention} ออกจากเซิร์ฟเวอร์แล้ว')


# เพิ่ม Cog นี้เข้าไปใน bot
def setup(bot):
    bot.add_cog(MemberJoinEvent(bot))
