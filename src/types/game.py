from __future__ import annotations
from typing import Optional, List, Union

class Game:
    def __init__(
        self,
        title: 'str',
        description: 'str',
        photo: 'List[PhotoSize]',
        text: 'Optional[str]' = None,
        text_entities: 'Optional[List[MessageEntity]]' = None,
        animation: 'Optional[Animation]' = None
    ):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation