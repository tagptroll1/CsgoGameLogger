from discord.ext.commands import Bot


class CsgoBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        super().load_extension("bot.cogs.game_logger")
