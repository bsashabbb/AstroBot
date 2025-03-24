from __future__ import annotations
from typing import Optional, List, Union

class createChatInviteLink:
    def __init__(
        self,
        chat_id: 'Union[str]',
        name: 'Optional[str]' = None,
        expire_date: 'Optional[int]' = None,
        member_limit: 'Optional[int]' = None,
        creates_join_request: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.creates_join_request = creates_join_request