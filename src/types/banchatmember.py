from __future__ import annotations
from typing import Optional, List, Union

class banChatMember:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int',
        until_date: 'Optional[int]' = None,
        revoke_messages: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.until_date = until_date
        self.revoke_messages = revoke_messages