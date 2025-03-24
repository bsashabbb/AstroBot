from __future__ import annotations
from typing import Optional, List, Union

class Dice:
    def __init__(
        self,
        emoji: 'str',
        value: 'int'
    ):
        self.emoji = emoji
        self.value = value