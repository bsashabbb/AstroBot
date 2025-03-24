from __future__ import annotations
from typing import Optional, List, Union

class BotCommandScopeChat:
    def __init__(
        self,
        type: 'str',
        chat_id: 'Union[str]'
    ):
        self.type = type
        self.chat_id = chat_id