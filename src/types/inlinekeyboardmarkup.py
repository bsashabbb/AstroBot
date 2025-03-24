from __future__ import annotations
from typing import Optional, List, Union

class InlineKeyboardMarkup:
    def __init__(
        self,
        inline_keyboard: 'List[List[InlineKeyboardButton]]'
    ):
        self.inline_keyboard = inline_keyboard