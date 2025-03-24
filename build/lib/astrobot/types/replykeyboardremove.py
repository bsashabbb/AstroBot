from __future__ import annotations
from typing import Optional, List, Union, Any

class ReplyKeyboardRemove:
    """ReplyKeyboardRemove Telegram API type"""

    def __init__(
        self,
        remove_keyboard: bool,
        selective: Optional[bool]
    ):
        self.remove_keyboard = remove_keyboard
        self.selective = selective
