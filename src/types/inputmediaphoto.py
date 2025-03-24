from __future__ import annotations
from typing import Optional, List, Union

class InputMediaPhoto:
    def __init__(
        self,
        type: 'str',
        media: 'str',
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        has_spoiler: 'Optional[bool]' = None
    ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler