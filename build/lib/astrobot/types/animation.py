from __future__ import annotations
from typing import Optional, List, Union, Any

class Animation:
    """Animation Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional['PhotoSize'],
        file_name: Optional[str],
        mime_type: Optional[str],
        file_size: Optional[int]
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
