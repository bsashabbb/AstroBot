from __future__ import annotations
from typing import Optional, List, Union

class PaidMediaPhoto:
    def __init__(
        self,
        type: 'str',
        photo: 'List[PhotoSize]'
    ):
        self.type = type
        self.photo = photo