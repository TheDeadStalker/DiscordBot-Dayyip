import discord
from discord.ext import commands

class infocommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def bilgi(self,mesaj):
        embed = discord.Embed(title="Receb Dayyip Ersoğan - Evren Bashganım ",
                              description="Dayyip'in hayal alemi ile tanışma fırsatı. ", color=0xe000f0)
        embed.set_author(name="Akgençlik - 2023 Projesi")
        embed.add_field(name="Yapımcı", value="ömer.py#2211", inline=False)
        embed.add_field(name="Versiyon", value="1.0.1", inline=True)
        embed.add_field(name="Instagram'dan takip etmeyi unutmayın. ", value="[@dervisogluberky](https://www.instagram.com/dervisogluberky/)", inline=True)
        embed.add_field(name="Discord sunucumuza da uğramayı unutmayın. ", value="[Tıkla](  https://discord.gg/JsvyFg7dHx)", inline=True)
        await mesaj.send(embed=embed)

def setup(bot):
    bot.add_cog(infocommands(bot))
