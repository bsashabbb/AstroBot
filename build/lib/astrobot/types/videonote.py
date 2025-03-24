from __future__ import annotations
from typing import Optional, List, Union, Any

class VideoNote:
    """VideoNote Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbnail: Optional['PhotoSize'],
        file_size: Optional[int]
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size
