from __future__ import annotations
from typing import Optional, List, Union, Any

class InputSticker:
    """InputSticker Telegram API type"""

    def __init__(
        self,
        sticker: Union['InputFile', str],
        format: str,
        emoji_list: List[str],
        mask_position: Optional['MaskPosition'],
        keywords: Optional[List[str]]
    ):
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords
