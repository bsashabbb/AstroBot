from __future__ import annotations
from typing import Optional, List, Union, Any

class BotCommandScopeChatAdministrators:
    """BotCommandScopeChatAdministrators Telegram API type"""

    def __init__(
        self,
        type: str,
        chat_id: Union[int, str]
    ):
        self.type = type
        self.chat_id = chat_id
