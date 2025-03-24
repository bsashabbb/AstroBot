from __future__ import annotations
from typing import Optional, List, Union

class MessageOriginChannel:
    def __init__(
        self,
        type: 'str',
        date: 'int',
        chat: 'Chat',
        message_id: 'int',
        author_signature: 'Optional[str]' = None
    ):
        self.type = type
        self.date = date
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature