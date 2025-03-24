from __future__ import annotations
from typing import Optional, List, Union, Any

class InputMediaAudio:
    """InputMediaAudio Telegram API type"""

    def __init__(
        self,
        type: str,
        media: str,
        thumbnail: Optional[Union['InputFile', str]],
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        duration: Optional[int],
        performer: Optional[str],
        title: Optional[str]
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
