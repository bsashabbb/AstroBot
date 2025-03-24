from __future__ import annotations
from typing import Optional, List, Union

class InputPollOption:
    def __init__(
        self,
        text: 'str',
        text_parse_mode: 'Optional[str]' = None,
        text_entities: 'Optional[List[MessageEntity]]' = None
    ):
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities