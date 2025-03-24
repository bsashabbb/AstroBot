from __future__ import annotations
from typing import Optional, List, Union, Any

class InputMediaPhoto:
    """InputMediaPhoto Telegram API type"""

    def __init__(
        self,
        type: str,
        media: str,
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        show_caption_above_media: Optional[bool],
        has_spoiler: Optional[bool]
    ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler
