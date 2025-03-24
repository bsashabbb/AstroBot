from __future__ import annotations
from typing import Optional, List, Union

class ForumTopicCreated:
    def __init__(
        self,
        name: 'str',
        icon_color: 'int',
        icon_custom_emoji_id: 'Optional[str]' = None
    ):
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id