from __future__ import annotations
from typing import Optional, List, Union, Any

class InputMediaVideo:
    """InputMediaVideo Telegram API type"""

    def __init__(
        self,
        type: str,
        media: str,
        thumbnail: Optional[Union['InputFile', str]],
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        show_caption_above_media: Optional[bool],
        width: Optional[int],
        height: Optional[int],
        duration: Optional[int],
        supports_streaming: Optional[bool],
        has_spoiler: Optional[bool]
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
