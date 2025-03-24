from __future__ import annotations
from typing import Optional, List, Union, Any

class Gift:
    """Gift Telegram API type"""

    def __init__(
        self,
        id: str,
        sticker: 'Sticker',
        star_count: int,
        upgrade_star_count: Optional[int],
        total_count: Optional[int],
        remaining_count: Optional[int]
    ):
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.upgrade_star_count = upgrade_star_count
        self.total_count = total_count
        self.remaining_count = remaining_count
