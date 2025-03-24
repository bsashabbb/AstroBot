from __future__ import annotations
from typing import Optional, List, Union

class uploadStickerFile:
    def __init__(
        self,
        user_id: 'int',
        sticker: 'InputFile',
        sticker_format: 'str'
    ):
        self.user_id = user_id
        self.sticker = sticker
        self.sticker_format = sticker_format