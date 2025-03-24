from __future__ import annotations
from typing import Optional, List, Union, Any

class Birthdate:
    """Birthdate Telegram API type"""

    def __init__(
        self,
        day: int,
        month: int,
        year: Optional[int]
    ):
        self.day = day
        self.month = month
        self.year = year
