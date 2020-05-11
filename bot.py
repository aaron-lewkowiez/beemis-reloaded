import discord.ext.commands as commands

class Beemis(commands.Bot):
    async def on_ready(self):
        print("logged in as {0}".format(self.user))
