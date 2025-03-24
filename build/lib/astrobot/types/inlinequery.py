from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQuery:
    """InlineQuery Telegram API type"""

    def __init__(
        self,
        id: str,
        from_user: 'User',
        query: str,
        offset: str,
        chat_type: Optional[str],
        location: Optional['Location']
    ):
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location
