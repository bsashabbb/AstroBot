from __future__ import annotations
from typing import Optional, List, Union

class getGameHighScores:
    def __init__(
        self,
        user_id: 'int',
        chat_id: 'Optional[int]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None
    ):
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id