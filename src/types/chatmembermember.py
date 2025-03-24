from __future__ import annotations
from typing import Optional, List, Union

class ChatMemberMember:
    def __init__(
        self,
        status: 'str',
        user: 'User',
        until_date: 'Optional[int]' = None
    ):
        self.status = status
        self.user = user
        self.until_date = until_date