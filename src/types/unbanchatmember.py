from __future__ import annotations
from typing import Optional, List, Union

class unbanChatMember:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int',
        only_if_banned: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.only_if_banned = only_if_banned