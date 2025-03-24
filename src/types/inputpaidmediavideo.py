from __future__ import annotations
from typing import Optional, List, Union

class InputPaidMediaVideo:
    def __init__(
        self,
        type: 'str',
        media: 'str',
        thumbnail: 'Optional[Union[str]]' = None,
        width: 'Optional[int]' = None,
        height: 'Optional[int]' = None,
        duration: 'Optional[int]' = None,
        supports_streaming: 'Optional[bool]' = None
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming