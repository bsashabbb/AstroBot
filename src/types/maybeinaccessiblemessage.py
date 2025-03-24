from __future__ import annotations
from typing import Optional, List, Union

class MaybeInaccessibleMessage:
    def __init__(
        self,
        type: 'str',
        offset: 'int',
        length: 'int',
        url: 'Optional[str]' = None,
        user: 'Optional[User]' = None,
        language: 'Optional[str]' = None,
        custom_emoji_id: 'Optional[str]' = None
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id