from __future__ import annotations
from typing import Optional, List, Union, Any

class AffiliateInfo:
    """AffiliateInfo Telegram API type"""

    def __init__(
        self,
        affiliate_user: Optional['User'],
        affiliate_chat: Optional['Chat'],
        commission_per_mille: int,
        amount: int,
        nanostar_amount: Optional[int]
    ):
        self.affiliate_user = affiliate_user
        self.affiliate_chat = affiliate_chat
        self.commission_per_mille = commission_per_mille
        self.amount = amount
        self.nanostar_amount = nanostar_amount
