from __future__ import annotations
from typing import Optional, List, Union

class BotCommandScopeChatMember:
    def __init__(
        self,
        type: 'str',
        chat_id: 'Union[str]',
        user_id: 'int'
    ):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id