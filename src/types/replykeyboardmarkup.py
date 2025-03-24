from __future__ import annotations
from typing import Optional, List, Union

class ReplyKeyboardMarkup:
    def __init__(
        self,
        keyboard: 'List[List[KeyboardButton]]',
        is_persistent: 'Optional[bool]' = None,
        resize_keyboard: 'Optional[bool]' = None,
        one_time_keyboard: 'Optional[bool]' = None,
        input_field_placeholder: 'Optional[str]' = None,
        selective: 'Optional[bool]' = None
    ):
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective