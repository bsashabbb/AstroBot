from __future__ import annotations
from typing import Optional, List, Union

class setStickerMaskPosition:
    def __init__(
        self,
        sticker: 'str',
        mask_position: 'Optional[MaskPosition]' = None
    ):
        self.sticker = sticker
        self.mask_position = mask_position