from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatBoostSourceGiveaway:
    """ChatBoostSourceGiveaway Telegram API type"""

    def __init__(
        self,
        source: str,
        giveaway_message_id: int,
        user: Optional['User'],
        prize_star_count: Optional[int],
        is_unclaimed: Optional[bool]
    ):
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed
