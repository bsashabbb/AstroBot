from __future__ import annotations
from typing import Optional, List, Union

class MessageOrigin:
    def __init__(
        self,
        type: 'str',
        date: 'int',
        sender_user: 'User'
    ):
        self.type = type
        self.date = date
        self.sender_user = sender_user