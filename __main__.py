import os

from discord.ext.commands import Bot
import discord.ext.commands
import pkgutil # for dynamic importing
from importlib import import_module
from inspect import isclass

if __name__ == "__main__":
    bot = Bot("!")
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
    bot.run(os.environ['DISCORD_TOKEN'])
