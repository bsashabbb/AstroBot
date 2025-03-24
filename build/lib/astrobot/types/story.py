from __future__ import annotations
from typing import Optional, List, Union, Any

class Story:
    """Story Telegram API type"""

    def __init__(
        self,
        chat: 'Chat',
        id: int
    ):
        self.chat = chat
        self.id = id
