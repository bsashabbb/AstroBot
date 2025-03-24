from __future__ import annotations
from typing import Optional, List, Union, Any

class PaidMediaPreview:
    """PaidMediaPreview Telegram API type"""

    def __init__(
        self,
        type: str,
        width: Optional[int],
        height: Optional[int],
        duration: Optional[int]
    ):
        self.type = type
        self.width = width
        self.height = height
        self.duration = duration
