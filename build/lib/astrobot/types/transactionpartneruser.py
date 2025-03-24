from __future__ import annotations
from typing import Optional, List, Union, Any

class TransactionPartnerUser:
    """TransactionPartnerUser Telegram API type"""

    def __init__(
        self,
        type: str,
        user: 'User',
        affiliate: Optional['AffiliateInfo'],
        invoice_payload: Optional[str],
        subscription_period: Optional[int],
        paid_media: Optional[List['PaidMedia']],
        paid_media_payload: Optional[str],
        gift: Optional['Gift']
    ):
        self.type = type
        self.user = user
        self.affiliate = affiliate
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift
