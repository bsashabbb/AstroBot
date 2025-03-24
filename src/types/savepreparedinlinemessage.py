from __future__ import annotations
from typing import Optional, List, Union

class savePreparedInlineMessage:
    def __init__(
        self,
        user_id: 'int',
        result: 'InlineQueryResult',
        allow_user_chats: 'Optional[bool]' = None,
        allow_bot_chats: 'Optional[bool]' = None,
        allow_group_chats: 'Optional[bool]' = None,
        allow_channel_chats: 'Optional[bool]' = None
    ):
        self.user_id = user_id
        self.result = result
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats