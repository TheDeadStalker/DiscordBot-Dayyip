import discord
from discord.ext import commands


class funkomut(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def dayyip(self, mesaj):
        await mesaj.send("Evren Başkanı.")

    @commands.command()
    async def tr(self, mesaj):
        await mesaj.send("2023 Türkiye Süper Güç.")

    @commands.command()
    async def ekonomi(self, mesaj):
        await mesaj.send("Evren liderimiz sayesinde devler ligine taşındık. Tank var uçak var ama dış güçler nedeniyle ekonomimiz zayıflatılmaya çalışılıyor.")

    @commands.command()
    async def cehape(self, mesaj):
        await mesaj.send("Yalandaroğlu'nun partisi.")



def setup(bot):
    bot.add_cog(funkomut(bot))