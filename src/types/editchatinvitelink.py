from __future__ import annotations
from typing import Optional, List, Union

class editChatInviteLink:
    def __init__(
        self,
        chat_id: 'Union[str]',
        invite_link: 'str',
        name: 'Optional[str]' = None,
        expire_date: 'Optional[int]' = None,
        member_limit: 'Optional[int]' = None,
        creates_join_request: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.invite_link = invite_link
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.creates_join_request = creates_join_request