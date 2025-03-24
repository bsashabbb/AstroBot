from __future__ import annotations
from typing import Optional, List, Union, Any

class ReactionCount:
    """ReactionCount Telegram API type"""

    def __init__(
        self,
        type: 'ReactionType',
        total_count: int
    ):
        self.type = type
        self.total_count = total_count
