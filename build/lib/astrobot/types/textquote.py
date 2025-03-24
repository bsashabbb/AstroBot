from __future__ import annotations
from typing import Optional, List, Union, Any

class TextQuote:
    """TextQuote Telegram API type"""

    def __init__(
        self,
        text: str,
        entities: Optional[List['MessageEntity']],
        position: int,
        is_manual: Optional[bool]
    ):
        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual
