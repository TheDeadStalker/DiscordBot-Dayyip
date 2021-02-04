import discord
from discord.ext import commands

class yardimkomut(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def yardim(self, mesaj, string):
        if(string == "yardim"):
            emb = discord.Embed(description="""
                &yardim Eğlence -> Eğlence Komutları
                &yardım Bilgi -> Bilgi Komutları 
                &yardim rep -> Oto Replace(yanıtlama) Komutları
                """)
            emb.set_author(name="Dayyip - Yardım Komutları")
            await mesaj.send(embed=emb)
        elif(string == "Eğlence"):
            emb = discord.Embed(description="""
                        &osmanlitorunurte  -> Dayyip sizin için evreni fethetmek için hazırlanır
                        """)
            emb.set_author(name="Dayyip - Eğlence Komutları")
            await mesaj.send(embed=emb)

        elif(string == "Bilgi"):
            emb = discord.Embed(description="""
                        &bilgi -> Dayyip Bot hakkında genel bilgiler 
                        """)
            emb.set_author(name="Dayyip - Bilgi Komutları")
            await mesaj.send(embed=emb)
        elif(string == "rep"):
            emb = discord.Embed(description="""
                        &dayyip 
                        &tr
                        &ekonomi
                        &cehape
                        """)
            emb.set_author(name="Dayyip - Oto-Yanıt Komutları")
            await mesaj.send(embed=emb)





def setup(bot):
    bot.add_cog(yardimkomut(bot))