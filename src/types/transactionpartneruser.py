from __future__ import annotations
from typing import Optional, List, Union

class TransactionPartnerUser:
    def __init__(
        self,
        type: 'str',
        user: 'User',
        affiliate: 'Optional[AffiliateInfo]' = None,
        invoice_payload: 'Optional[str]' = None,
        subscription_period: 'Optional[int]' = None,
        paid_media: 'Optional[List[PaidMedia]]' = None,
        paid_media_payload: 'Optional[str]' = None,
        gift: 'Optional[Gift]' = None
    ):
        self.type = type
        self.user = user
        self.affiliate = affiliate
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift