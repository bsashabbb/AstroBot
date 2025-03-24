from __future__ import annotations
from typing import Optional, List, Union, Any

class BusinessConnection:
    """BusinessConnection Telegram API type"""

    def __init__(
        self,
        id: str,
        user: 'User',
        user_chat_id: int,
        date: int,
        can_reply: bool,
        is_enabled: bool
    ):
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled
