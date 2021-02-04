import discord
from discord.ext import commands
import time

class adminkomut(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(hidden=True)
    async def yenile(self, mesaj, value:str):
        dizin = "commands."
        a = 1
        try:
            if(a):
                self.bot.unload_extension(dizin + value)
                self.bot.load_extension(dizin + value)
                await mesaj.send(value + " dosyası yenilendi!")
            else:
                await mesaj.send("Dayyip bunu kullanmanı istemiyor. Karşı mısın? Yallah, Silivriye!")
        except ImportError as e:
            print(e)
    @commands.command(aliases=["clear"])
    async def temizle(self, mesaj, sayi:int):
        a = 1
        if(a):
            if(sayi > 0 and sayi <= 100):
                kanal = mesaj.channel
                message = await kanal.history(limit=sayi).flatten()
                mesaj2 = await mesaj.send("{} adet mesaj var.".format(sayi))
                time.sleep(1)
                await mesaj2.edit(content = "{} adet mesaj siliniyor..." .format(sayi))
                time.sleep(0.5)
                await kanal.delete_messages(message)
                await mesaj2.edit(content=":white_check_mark: {} adet mesaj silindi" .format(sayi))
                time.sleep(0.5)
                message = await kanal.history(limit=1).flatten()
                await kanal.delete_messages(message)

            else:
                await mesaj.send("En fazla 100 en az 1 mesaj silebilirim")
        else:
            await mesaj.send("Dayyip bunu kullanmanı istemiyor. Karşı mısın? Yallah, Silivriye!")

    @commands.command()
    async def kick(self,mesaj, member: discord.Member, *args,):
        await member.kick(reason=None)

    @commands.command()
    async def ban(self, mesaj, member: discord.Member, *args,):
        await member.ban(reason=None)
    @commands.command()
    async def mute(self):
        pass





def setup(bot):
    bot.add_cog(adminkomut(bot))