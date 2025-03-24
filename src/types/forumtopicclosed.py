from __future__ import annotations
from typing import Optional, List, Union

class ForumTopicClosed:
    def __init__(
        self,
        name: 'Optional[str]' = None,
        icon_custom_emoji_id: 'Optional[str]' = None
    ):
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id