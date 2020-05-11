import discord.ext.commands

class Beemis(commands.Bot):
    async def on_ready(self):
        print("logged in as {0}".format(self.user))
    async def on_message(self, message):
        print("{0.author}: {0.content}".format(message))
