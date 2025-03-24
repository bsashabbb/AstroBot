from __future__ import annotations
from typing import Optional, List, Union

class InputSticker:
    def __init__(
        self,
        sticker: 'Union[str]',
        format: 'str',
        emoji_list: 'List[str]',
        mask_position: 'Optional[MaskPosition]' = None,
        keywords: 'Optional[List[str]]' = None
    ):
        self.sticker = sticker
        self.format = format
        self.emoji_list = emoji_list
        self.mask_position = mask_position
        self.keywords = keywords