from __future__ import annotations
from typing import Optional, List, Union, Any

class MessageOriginChat:
    """MessageOriginChat Telegram API type"""

    def __init__(
        self,
        type: str,
        date: int,
        sender_chat: 'Chat',
        author_signature: Optional[str]
    ):
        self.type = type
        self.date = date
        self.sender_chat = sender_chat
        self.author_signature = author_signature
