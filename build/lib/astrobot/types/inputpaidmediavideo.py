from __future__ import annotations
from typing import Optional, List, Union, Any

class InputPaidMediaVideo:
    """InputPaidMediaVideo Telegram API type"""

    def __init__(
        self,
        type: str,
        media: str,
        thumbnail: Optional[Union['InputFile', str]],
        width: Optional[int],
        height: Optional[int],
        duration: Optional[int],
        supports_streaming: Optional[bool]
    ):
        self.type = type
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
