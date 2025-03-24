from __future__ import annotations
from typing import Optional, List, Union

class AffiliateInfo:
    def __init__(
        self,
        commission_per_mille: 'int',
        amount: 'int',
        affiliate_user: 'Optional[User]' = None,
        affiliate_chat: 'Optional[Chat]' = None,
        nanostar_amount: 'Optional[int]' = None
    ):
        self.affiliate_user = affiliate_user
        self.affiliate_chat = affiliate_chat
        self.commission_per_mille = commission_per_mille
        self.amount = amount
        self.nanostar_amount = nanostar_amount