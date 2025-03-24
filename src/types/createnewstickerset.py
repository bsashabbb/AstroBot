from __future__ import annotations
from typing import Optional, List, Union

class createNewStickerSet:
    def __init__(
        self,
        user_id: 'int',
        name: 'str',
        title: 'str',
        stickers: 'List[InputSticker]',
        sticker_type: 'Optional[str]' = None,
        needs_repainting: 'Optional[bool]' = None
    ):
        self.user_id = user_id
        self.name = name
        self.title = title
        self.stickers = stickers
        self.sticker_type = sticker_type
        self.needs_repainting = needs_repainting