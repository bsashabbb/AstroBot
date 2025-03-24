from __future__ import annotations
from typing import Optional, List, Union

class addStickerToSet:
    def __init__(
        self,
        user_id: 'int',
        name: 'str',
        sticker: 'InputSticker'
    ):
        self.user_id = user_id
        self.name = name
        self.sticker = sticker