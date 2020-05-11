from discord.ext.commands import command

@command()
async def helloworld(ctx):
    await ctx.send("Hello!")
