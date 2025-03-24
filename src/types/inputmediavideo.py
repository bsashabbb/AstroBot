from __future__ import annotations
from typing import Optional, List, Union

class InputMediaVideo:
    def __init__(
        self,
        type: 'str',
        media: 'str',
        thumbnail: 'Optional[Union[str]]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        width: 'Optional[int]' = None,
        height: 'Optional[int]' = None,
        duration: 'Optional[int]' = None,
        supports_streaming: 'Optional[bool]' = None,
        has_spoiler: 'Optional[bool]' = None
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler