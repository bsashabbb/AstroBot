from __future__ import annotations
from typing import Optional, List, Union

class RevenueWithdrawalStateSucceeded:
    def __init__(
        self,
        type: 'str',
        date: 'int',
        url: 'str'
    ):
        self.type = type
        self.date = date
        self.url = url