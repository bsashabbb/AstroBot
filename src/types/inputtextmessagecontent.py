from __future__ import annotations
from typing import Optional, List, Union

class InputTextMessageContent:
    def __init__(
        self,
        message_text: 'str',
        parse_mode: 'Optional[str]' = None,
        entities: 'Optional[List[MessageEntity]]' = None,
        link_preview_options: 'Optional[LinkPreviewOptions]' = None
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options