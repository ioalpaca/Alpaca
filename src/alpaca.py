import logging
from discord.ext import commands
from typing import Any
from utils.logger import get_logger


class Alpaca(commands.Bot):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.logger: logging.Logger = get_logger("alpaca")

    async def on_ready(self) -> None:
        self.logger.info(f"Logged in as {self.user}")
