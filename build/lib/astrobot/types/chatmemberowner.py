from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatMemberOwner:
    """ChatMemberOwner Telegram API type"""

    def __init__(
        self,
        status: str,
        user: 'User',
        is_anonymous: bool,
        custom_title: Optional[str]
    ):
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title
