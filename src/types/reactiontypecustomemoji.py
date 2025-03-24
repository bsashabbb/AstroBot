from __future__ import annotations
from typing import Optional, List, Union

class ReactionTypeCustomEmoji:
    def __init__(
        self,
        type: 'str',
        custom_emoji_id: 'str'
    ):
        self.type = type
        self.custom_emoji_id = custom_emoji_id