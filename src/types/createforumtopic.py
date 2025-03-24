from __future__ import annotations
from typing import Optional, List, Union

class createForumTopic:
    def __init__(
        self,
        chat_id: 'Union[str]',
        name: 'str',
        icon_color: 'Optional[int]' = None,
        icon_custom_emoji_id: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id