from __future__ import annotations
from typing import Optional, List, Union

class Gift:
    def __init__(
        self,
        id: 'str',
        sticker: 'Sticker',
        star_count: 'int',
        upgrade_star_count: 'Optional[int]' = None,
        total_count: 'Optional[int]' = None,
        remaining_count: 'Optional[int]' = None
    ):
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.upgrade_star_count = upgrade_star_count
        self.total_count = total_count
        self.remaining_count = remaining_count