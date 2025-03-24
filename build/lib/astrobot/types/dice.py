from __future__ import annotations
from typing import Optional, List, Union, Any

class Dice:
    """Dice Telegram API type"""

    def __init__(
        self,
        emoji: str,
        value: int
    ):
        self.emoji = emoji
        self.value = value
