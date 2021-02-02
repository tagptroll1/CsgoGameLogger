import os

from bot.bot import CsgoBot
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    csgobot = CsgoBot(command_prefix="$")
    csgobot.run(os.getenv("CSGOBOT_TOKEN"))
