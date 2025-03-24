from __future__ import annotations
from typing import Optional, List, Union, Any

class RevenueWithdrawalStateSucceeded:
    """RevenueWithdrawalStateSucceeded Telegram API type"""

    def __init__(
        self,
        type: str,
        date: int,
        url: str
    ):
        self.type = type
        self.date = date
        self.url = url
