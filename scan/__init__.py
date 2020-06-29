
from .scan import Scan


def setup(bot):
    bot.add_cog(Scan(bot))
