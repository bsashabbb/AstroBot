from __future__ import annotations
from typing import Optional, List, Union, Any

class PaidMediaVideo:
    """PaidMediaVideo Telegram API type"""

    def __init__(
        self,
        type: str,
        video: 'Video'
    ):
        self.type = type
        self.video = video
