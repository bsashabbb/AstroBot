from __future__ import annotations
from typing import Optional, List, Union, Any

class Gifts:
    """Gifts Telegram API type"""

    def __init__(
        self,
        gifts: List['Gift']
    ):
        self.gifts = gifts
