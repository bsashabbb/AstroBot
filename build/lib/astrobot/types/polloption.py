from __future__ import annotations
from typing import Optional, List, Union, Any

class PollOption:
    """PollOption Telegram API type"""

    def __init__(
        self,
        text: str,
        text_entities: Optional[List['MessageEntity']],
        voter_count: int
    ):
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count
