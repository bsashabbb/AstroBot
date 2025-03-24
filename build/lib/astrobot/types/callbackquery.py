from __future__ import annotations
from typing import Optional, List, Union, Any

class CallbackQuery:
    """CallbackQuery Telegram API type"""

    def __init__(
        self,
        id: str,
        from_user: 'User',
        message: Optional['MaybeInaccessibleMessage'],
        inline_message_id: Optional[str],
        chat_instance: str,
        data: Optional[str],
        game_short_name: Optional[str]
    ):
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name
