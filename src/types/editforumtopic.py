from __future__ import annotations
from typing import Optional, List, Union

class editForumTopic:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_thread_id: 'int',
        name: 'Optional[str]' = None,
        icon_custom_emoji_id: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id