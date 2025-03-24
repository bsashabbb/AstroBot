from __future__ import annotations
from typing import Optional, List, Union, Any

class Chat:
    """Chat Telegram API type"""

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str],
        username: Optional[str],
        first_name: Optional[str],
        last_name: Optional[str],
        is_forum: Optional[bool]
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
