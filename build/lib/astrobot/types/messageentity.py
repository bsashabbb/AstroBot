from __future__ import annotations
from typing import Optional, List, Union, Any

class MessageEntity:
    """MessageEntity Telegram API type"""

    def __init__(
        self,
        type: str,
        offset: int,
        length: int,
        url: Optional[str],
        user: Optional['User'],
        language: Optional[str],
        custom_emoji_id: Optional[str]
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id
