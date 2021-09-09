from .cog import Reloader


def setup(bot):
    bot.add_cog(Reloader(bot))


__version__ = "0.0.2"
