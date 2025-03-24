from __future__ import annotations
from typing import Optional, List, Union

class StarTransactions:
    def __init__(
        self,
        transactions: 'List[StarTransaction]'
    ):
        self.transactions = transactions