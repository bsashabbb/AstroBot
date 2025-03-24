from __future__ import annotations
from typing import Optional, List, Union

class ChatBoostSourceGiveaway:
    def __init__(
        self,
        source: 'str',
        giveaway_message_id: 'int',
        user: 'Optional[User]' = None,
        prize_star_count: 'Optional[int]' = None,
        is_unclaimed: 'Optional[bool]' = None
    ):
        self.source = source
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed