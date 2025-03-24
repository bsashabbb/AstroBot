from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatMemberMember:
    """ChatMemberMember Telegram API type"""

    def __init__(
        self,
        status: str,
        user: 'User',
        until_date: Optional[int]
    ):
        self.status = status
        self.user = user
        self.until_date = until_date
