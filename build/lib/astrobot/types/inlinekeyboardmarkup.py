from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineKeyboardMarkup:
    """InlineKeyboardMarkup Telegram API type"""

    def __init__(
        self,
        inline_keyboard: List[List['InlineKeyboardButton']]
    ):
        self.inline_keyboard = inline_keyboard
