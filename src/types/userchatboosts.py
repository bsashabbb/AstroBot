from __future__ import annotations
from typing import Optional, List, Union

class UserChatBoosts:
    def __init__(
        self,
        boosts: 'List[ChatBoost]'
    ):
        self.boosts = boosts