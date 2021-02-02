from datetime import datetime

from discord import Color, Embed
from discord.ext.commands import Bot, BucketType, Cog, command, cooldown

from bot.google_sheets import main


class GameLogger(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command()
    @cooldown(1, 5, BucketType.user)
    async def log(self, ctx, map_name, cheaters: int = 0):
        _map = self.get_map(map_name)

        main(datetime.today().strftime("%m/%d/%Y"), _map, cheaters, ctx.author)

        embed = Embed()
        embed.description = f"Map '{_map}' has been registered with {cheaters} cheaters"
        embed.color = Color.dark_green()

        await ctx.send(embed=embed)

    def get_map(self, map_name: str):
        lower = map_name.lower()

        if lower.startswith("i"):
            return "Inferno"
        elif lower.startswith("t"):
            return "Train"
        elif lower.startswith("m"):
            return "Mirage"
        elif lower.startswith("n"):
            return "Nuke"
        elif lower.startswith("o"):
            return "Overpass"
        elif lower.startswith("d"):
            return "Dust II"
        elif lower.startswith("v"):
            return "Vertigo"

        raise ValueError(f"Map name '{map_name}' is not a valid map")

def setup(bot: Bot):
    bot.add_cog(GameLogger(bot))