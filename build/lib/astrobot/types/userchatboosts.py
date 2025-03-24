from __future__ import annotations
from typing import Optional, List, Union, Any

class UserChatBoosts:
    """UserChatBoosts Telegram API type"""

    def __init__(
        self,
        boosts: List['ChatBoost']
    ):
        self.boosts = boosts
