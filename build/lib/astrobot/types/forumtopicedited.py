from __future__ import annotations
from typing import Optional, List, Union, Any

class ForumTopicEdited:
    """ForumTopicEdited Telegram API type"""

    def __init__(
        self,
        name: Optional[str],
        icon_custom_emoji_id: Optional[str]
    ):
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id
