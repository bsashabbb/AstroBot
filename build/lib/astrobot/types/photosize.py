from __future__ import annotations
from typing import Optional, List, Union, Any

class PhotoSize:
    """PhotoSize Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: Optional[int]
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
