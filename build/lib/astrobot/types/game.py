from __future__ import annotations
from typing import Optional, List, Union, Any

class Game:
    """Game Telegram API type"""

    def __init__(
        self,
        title: str,
        description: str,
        photo: List['PhotoSize'],
        text: Optional[str],
        text_entities: Optional[List['MessageEntity']],
        animation: Optional['Animation']
    ):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation
