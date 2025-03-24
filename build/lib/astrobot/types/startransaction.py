from __future__ import annotations
from typing import Optional, List, Union, Any

class StarTransaction:
    """StarTransaction Telegram API type"""

    def __init__(
        self,
        id: str,
        amount: int,
        nanostar_amount: Optional[int],
        date: int,
        source: Optional['TransactionPartner'],
        receiver: Optional['TransactionPartner']
    ):
        self.id = id
        self.amount = amount
        self.nanostar_amount = nanostar_amount
        self.date = date
        self.source = source
        self.receiver = receiver
