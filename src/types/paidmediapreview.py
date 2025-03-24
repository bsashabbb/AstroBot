from __future__ import annotations
from typing import Optional, List, Union

class PaidMediaPreview:
    def __init__(
        self,
        type: 'str',
        width: 'Optional[int]' = None,
        height: 'Optional[int]' = None,
        duration: 'Optional[int]' = None
    ):
        self.type = type
        self.width = width
        self.height = height
        self.duration = duration