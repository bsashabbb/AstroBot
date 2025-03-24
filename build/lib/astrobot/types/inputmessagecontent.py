from __future__ import annotations
from typing import Optional, List, Union, Any

class InputMessageContent:
    """InputMessageContent Telegram API type"""

    def __init__(
        self,
        message_text: str,
        parse_mode: Optional[str],
        entities: Optional[List['MessageEntity']],
        link_preview_options: Optional['LinkPreviewOptions']
    ):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options
