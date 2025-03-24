from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatBoostSourcePremium:
    """ChatBoostSourcePremium Telegram API type"""

    def __init__(
        self,
        source: str,
        user: 'User'
    ):
        self.source = source
        self.user = user
