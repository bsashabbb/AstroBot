from __future__ import annotations
from typing import Optional, List, Union

class CallbackQuery:
    def __init__(
        self,
        id: 'str',
        from_: 'User',
        chat_instance: 'str',
        message: 'Optional[MaybeInaccessibleMessage]' = None,
        inline_message_id: 'Optional[str]' = None,
        data: 'Optional[str]' = None,
        game_short_name: 'Optional[str]' = None
    ):
        self.id = id
        self.from_ = from_
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name