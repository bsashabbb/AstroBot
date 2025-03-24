from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatMemberLeft:
    """ChatMemberLeft Telegram API type"""

    def __init__(
        self,
        status: str,
        user: 'User'
    ):
        self.status = status
        self.user = user
