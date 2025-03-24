from __future__ import annotations
from typing import Optional, List, Union

class ForumTopic:
    def __init__(
        self,
        message_thread_id: 'int',
        name: 'str',
        icon_color: 'int',
        icon_custom_emoji_id: 'Optional[str]' = None
    ):
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id