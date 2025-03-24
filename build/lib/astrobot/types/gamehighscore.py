from __future__ import annotations
from typing import Optional, List, Union, Any

class GameHighScore:
    """GameHighScore Telegram API type"""

    def __init__(
        self,
        position: int,
        user: 'User',
        score: int
    ):
        self.position = position
        self.user = user
        self.score = score
