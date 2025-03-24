from __future__ import annotations
from typing import Optional, List, Union

class PollOption:
    def __init__(
        self,
        text: 'str',
        voter_count: 'int',
        text_entities: 'Optional[List[MessageEntity]]' = None
    ):
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count