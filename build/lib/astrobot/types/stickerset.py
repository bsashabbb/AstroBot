from __future__ import annotations
from typing import Optional, List, Union, Any

class StickerSet:
    """StickerSet Telegram API type"""

    def __init__(
        self,
        name: str,
        title: str,
        sticker_type: str,
        stickers: List['Sticker'],
        thumbnail: Optional['PhotoSize']
    ):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail
