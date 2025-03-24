from __future__ import annotations
from typing import Optional, List, Union

class InaccessibleMessage:
    def __init__(
        self,
        chat: 'Chat',
        message_id: 'int',
        date: 'int'
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date