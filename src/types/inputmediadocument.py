from __future__ import annotations
from typing import Optional, List, Union

class InputMediaDocument:
    def __init__(
        self,
        type: 'str',
        media: 'str',
        thumbnail: 'Optional[Union[str]]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        disable_content_type_detection: 'Optional[bool]' = None
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection