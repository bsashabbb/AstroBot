from __future__ import annotations
from typing import Optional, List, Union

class PaidMediaVideo:
    def __init__(
        self,
        type: 'str',
        video: 'Video'
    ):
        self.type = type
        self.video = video