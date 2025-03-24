from __future__ import annotations
from typing import Optional, List, Union

class BotCommand:
    def __init__(
        self,
        command: 'str',
        description: 'str'
    ):
        self.command = command
        self.description = description