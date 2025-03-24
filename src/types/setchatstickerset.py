from __future__ import annotations
from typing import Optional, List, Union

class setChatStickerSet:
    def __init__(
        self,
        chat_id: 'Union[str]',
        sticker_set_name: 'str'
    ):
        self.chat_id = chat_id
        self.sticker_set_name = sticker_set_name