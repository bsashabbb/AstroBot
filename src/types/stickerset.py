from __future__ import annotations
from typing import Optional, List, Union

class StickerSet:
    def __init__(
        self,
        name: 'str',
        title: 'str',
        sticker_type: 'str',
        stickers: 'List[Sticker]',
        thumbnail: 'Optional[PhotoSize]' = None
    ):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.stickers = stickers
        self.thumbnail = thumbnail