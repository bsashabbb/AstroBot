from __future__ import annotations
from typing import Optional, List, Union

class PaidMediaInfo:
    def __init__(
        self,
        star_count: 'int',
        paid_media: 'List[PaidMedia]'
    ):
        self.star_count = star_count
        self.paid_media = paid_media