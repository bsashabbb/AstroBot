from __future__ import annotations
from typing import Optional, List, Union

class TransactionPartnerAffiliateProgram:
    def __init__(
        self,
        type: 'str',
        commission_per_mille: 'int',
        sponsor_user: 'Optional[User]' = None
    ):
        self.type = type
        self.sponsor_user = sponsor_user
        self.commission_per_mille = commission_per_mille