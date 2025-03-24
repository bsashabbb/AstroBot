from __future__ import annotations
from typing import Optional, List, Union, Any

class MessageOriginChannel:
    """MessageOriginChannel Telegram API type"""

    def __init__(
        self,
        type: str,
        date: int,
        chat: 'Chat',
        message_id: int,
        author_signature: Optional[str]
    ):
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature
