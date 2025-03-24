from __future__ import annotations
from typing import Optional, List, Union

class replaceStickerInSet:
    def __init__(
        self,
        user_id: 'int',
        name: 'str',
        old_sticker: 'str',
        sticker: 'InputSticker'
    ):
        self.user_id = user_id
        self.name = name
        self.old_sticker = old_sticker
        self.sticker = sticker