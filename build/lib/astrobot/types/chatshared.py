from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatShared:
    """ChatShared Telegram API type"""

    def __init__(
        self,
        request_id: int,
        chat_id: int,
        title: Optional[str],
        username: Optional[str],
        photo: Optional[List['PhotoSize']]
    ):
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo
