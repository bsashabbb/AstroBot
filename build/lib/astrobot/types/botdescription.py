from __future__ import annotations
from typing import Optional, List, Union, Any

class BotDescription:
    """BotDescription Telegram API type"""

    def __init__(
        self,
        description: str
    ):
        self.description = description
