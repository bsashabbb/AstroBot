from __future__ import annotations
from typing import Optional, List, Union

class setGameScore:
    def __init__(
        self,
        user_id: 'int',
        score: 'int',
        force: 'Optional[bool]' = None,
        disable_edit_message: 'Optional[bool]' = None,
        chat_id: 'Optional[int]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None
    ):
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id