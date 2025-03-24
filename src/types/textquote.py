from __future__ import annotations
from typing import Optional, List, Union

class TextQuote:
    def __init__(
        self,
        text: 'str',
        position: 'int',
        entities: 'Optional[List[MessageEntity]]' = None,
        is_manual: 'Optional[bool]' = None
    ):
        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual