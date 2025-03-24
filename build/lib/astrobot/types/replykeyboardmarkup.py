from __future__ import annotations
from typing import Optional, List, Union, Any

class ReplyKeyboardMarkup:
    """ReplyKeyboardMarkup Telegram API type"""

    def __init__(
        self,
        keyboard: List[List['KeyboardButton']],
        is_persistent: Optional[bool],
        resize_keyboard: Optional[bool],
        one_time_keyboard: Optional[bool],
        input_field_placeholder: Optional[str],
        selective: Optional[bool]
    ):
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
