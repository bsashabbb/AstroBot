from __future__ import annotations
from typing import Optional, List, Union

class setUserEmojiStatus:
    def __init__(
        self,
        user_id: 'int',
        emoji_status_custom_emoji_id: 'Optional[str]' = None,
        emoji_status_expiration_date: 'Optional[int]' = None
    ):
        self.user_id = user_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date