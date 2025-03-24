from __future__ import annotations
from typing import Optional, List, Union, Any

class ReactionType:
    """ReactionType Telegram API type"""

    def __init__(
        self,
        type: str,
        emoji: str
    ):
        self.type = type
        self.emoji = emoji
