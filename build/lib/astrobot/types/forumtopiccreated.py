from __future__ import annotations
from typing import Optional, List, Union, Any

class ForumTopicCreated:
    """ForumTopicCreated Telegram API type"""

    def __init__(
        self,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str]
    ):
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
