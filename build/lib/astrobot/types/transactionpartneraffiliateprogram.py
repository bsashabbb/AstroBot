from __future__ import annotations
from typing import Optional, List, Union, Any

class TransactionPartnerAffiliateProgram:
    """TransactionPartnerAffiliateProgram Telegram API type"""

    def __init__(
        self,
        type: str,
        sponsor_user: Optional['User'],
        commission_per_mille: int
    ):
        self.type = type
        self.sponsor_user = sponsor_user
        self.commission_per_mille = commission_per_mille
