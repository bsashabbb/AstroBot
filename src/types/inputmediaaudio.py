from __future__ import annotations
from typing import Optional, List, Union

class InputMediaAudio:
    def __init__(
        self,
        type: 'str',
        media: 'str',
        thumbnail: 'Optional[Union[str]]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        duration: 'Optional[int]' = None,
        performer: 'Optional[str]' = None,
        title: 'Optional[str]' = None
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title