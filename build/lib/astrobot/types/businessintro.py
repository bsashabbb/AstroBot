from __future__ import annotations
from typing import Optional, List, Union, Any

class BusinessIntro:
    """BusinessIntro Telegram API type"""

    def __init__(
        self,
        title: Optional[str],
        message: Optional[str],
        sticker: Optional['Sticker']
    ):
        self.title = title
        self.message = message
        self.sticker = sticker
