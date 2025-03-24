from __future__ import annotations
from typing import Optional, List, Union

class MessageOriginHiddenUser:
    def __init__(
        self,
        type: 'str',
        date: 'int',
        sender_user_name: 'str'
    ):
        self.type = type
        self.date = date
        self.sender_user_name = sender_user_name