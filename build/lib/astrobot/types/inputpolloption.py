from __future__ import annotations
from typing import Optional, List, Union, Any

class InputPollOption:
    """InputPollOption Telegram API type"""

    def __init__(
        self,
        text: str,
        text_parse_mode: Optional[str],
        text_entities: Optional[List['MessageEntity']]
    ):
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities
