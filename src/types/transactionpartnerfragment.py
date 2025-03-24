from __future__ import annotations
from typing import Optional, List, Union

class TransactionPartnerFragment:
    def __init__(
        self,
        type: 'str',
        withdrawal_state: 'Optional[RevenueWithdrawalState]' = None
    ):
        self.type = type
        self.withdrawal_state = withdrawal_state