from __future__ import annotations
from typing import Optional, List, Union

class ChatMemberBanned:
    def __init__(
        self,
        status: 'str',
        user: 'User',
        until_date: 'int'
    ):
        self.status = status
        self.user = user
        self.until_date = until_date