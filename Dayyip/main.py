import discord
from discord.ext import commands
import platform

token = "ODAyNTM0NTYwMzk4NTczNTk5.YAwojQ.jBDMBpDZ_R50KqWSGnCjToCY8No"
kanal_adi = ""
class Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix="&", pm_help=None, description=None)
		self.bot_version = "1.0.0"
		self.bot_name = "Dayyip"
		self.author = "AkGençlik"
		self.icon = ""
		self.getDeviceOs = platform.system()
		self.load_extension("commands.info")
		self.load_extension("commands.admin")
		#self.load_extension("commands.music")
		self.load_extension("commands.fun")
		self.load_extension("commands.gif")
		self.load_extension("commands.yardim")
	async def on_ready(self):
		print("DAYYİP EVRENİ FETHETMEYE HAZIRRR")

	async def on_command_error(self, context, exception):
		if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
			await context.send("Aradığınız komutu her yerde aradım ancak bulamadım. Böyle bir komut mu istiyorsun? Peki o halde bana ulaşmalısın. omerkeskin1383@gmail.com adresinden fikirlerinizi mail yolu ile atabilirsiniz.")
	async def on_member_join(self,member: discord.Member):
		kanal = discord.utils.get(member.guild.channels, name="hoşgeldiniz")
		if kanal != None or kanal != 0:
			await kanal.send("Sunucumuza {} adında biri katıldı." .format(member.mention))
		else:
			print("ERR")



bot = Bot()
bot.run(token)
