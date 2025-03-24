from __future__ import annotations
from typing import Optional, List, Union

class setStickerSetThumbnail:
    def __init__(
        self,
        name: 'str',
        user_id: 'int',
        format: 'str',
        thumbnail: 'Optional[Union[str]]' = None
    ):
        self.name = name
        self.user_id = user_id
        self.thumbnail = thumbnail
        self.format = format