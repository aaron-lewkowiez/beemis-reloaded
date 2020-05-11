import discord.ext.commands as commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hiya!")
