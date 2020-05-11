# for pulling env vars
import os

# dynamic importing tools
import discord
import pkgutil
from importlib import import_module
from inspect import isclass

# beemis himself
from bot import Beemis

if __name__ == "__main__":
    # instantiate the bot
    bot = Beemis("")

    # dynamic import of all commands and cogs. god help us when this must be changed:

    # for all modules in the commands folder
    for (_, name, _) in pkgutil.walk_packages(path=['commands']):
        # get fully qualified module name, and import module
        fqname = 'commands.' + name
        cmodule = import_module(fqname, __package__)
        # find all Command instances in module
        for obj in cmodule.__dict__.values():
            if isinstance(obj, discord.ext.commands.core.Command):
                # import each command
                bot.add_command(obj)
                print("loaded command {}".format(obj))

    # for all modules in the cogs folder
    for (_, name, _) in pkgutil.walk_packages(path=['cogs']):
        # get fully qualified module name, and import module
        fqname = 'cogs.' + name
        cmodule = import_module(fqname, __package__)
        # find all Cog subclases in module
        for name, obj in cmodule.__dict__.items():
            if isclass(obj) and issubclass(obj, discord.ext.commands.Cog):
                # import each cog
                bot.add_cog(obj(bot))
                print("loaded cog {}".format(type(obj).__name__))
    # start the bot
    try:
        bot.run(os.environ['DISCORD_TOKEN'])
    except KeyError: # probably forgot to set the env
        print("Failed to find DISCORD_TOKEN environment variable! Is it set?")
        exit(1)
