from __future__ import annotations
from typing import Optional, List, Union

class StarTransaction:
    def __init__(
        self,
        id: 'str',
        amount: 'int',
        date: 'int',
        nanostar_amount: 'Optional[int]' = None,
        source: 'Optional[TransactionPartner]' = None,
        receiver: 'Optional[TransactionPartner]' = None
    ):
        self.id = id
        self.amount = amount
        self.nanostar_amount = nanostar_amount
        self.date = date
        self.source = source
        self.receiver = receiver