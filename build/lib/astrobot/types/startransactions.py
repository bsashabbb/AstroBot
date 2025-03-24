from __future__ import annotations
from typing import Optional, List, Union, Any

class StarTransactions:
    """StarTransactions Telegram API type"""

    def __init__(
        self,
        transactions: List['StarTransaction']
    ):
        self.transactions = transactions
