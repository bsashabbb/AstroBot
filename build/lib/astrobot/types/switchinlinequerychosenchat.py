from __future__ import annotations
from typing import Optional, List, Union, Any

class SwitchInlineQueryChosenChat:
    """SwitchInlineQueryChosenChat Telegram API type"""

    def __init__(
        self,
        query: Optional[str],
        allow_user_chats: Optional[bool],
        allow_bot_chats: Optional[bool],
        allow_group_chats: Optional[bool],
        allow_channel_chats: Optional[bool]
    ):
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats
