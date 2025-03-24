from __future__ import annotations
from typing import Optional, List, Union, Any

class TransactionPartnerFragment:
    """TransactionPartnerFragment Telegram API type"""

    def __init__(
        self,
        type: str,
        withdrawal_state: Optional['RevenueWithdrawalState']
    ):
        self.type = type
        self.withdrawal_state = withdrawal_state
