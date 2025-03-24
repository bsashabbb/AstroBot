from __future__ import annotations
from typing import Optional, List, Union

class BusinessIntro:
    def __init__(
        self,
        title: 'Optional[str]' = None,
        message: 'Optional[str]' = None,
        sticker: 'Optional[Sticker]' = None
    ):
        self.title = title
        self.message = message
        self.sticker = sticker