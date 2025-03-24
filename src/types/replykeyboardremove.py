from __future__ import annotations
from typing import Optional, List, Union

class ReplyKeyboardRemove:
    def __init__(
        self,
        remove_keyboard: 'bool',
        selective: 'Optional[bool]' = None
    ):
        self.remove_keyboard = remove_keyboard
        self.selective = selective