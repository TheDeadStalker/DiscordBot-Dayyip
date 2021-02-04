import discord
from discord.ext import commands
import safygiphy

class gif(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def osmanlitorunurte(self, mesaj, member: discord.Member):
        emb = discord.Embed(description="Dayyip evreni " + mesaj.author.name + " ve {0.mention} için fethetmeye hazır".format(member))
        emb.set_image(url="https://media1.tenor.com/images/edfcd54ee6c1e7fc6203fb4b511b4d88/tenor.gif?itemid=13676787")
        await mesaj.send(embed=emb)

def setup(bot):
    bot.add_cog(gif(bot))