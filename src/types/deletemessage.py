from __future__ import annotations
from typing import Optional, List, Union

class deleteMessage:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_id: 'int'
    ):
        self.chat_id = chat_id
        self.message_id = message_id