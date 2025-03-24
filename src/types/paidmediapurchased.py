from __future__ import annotations
from typing import Optional, List, Union

class PaidMediaPurchased:
    def __init__(
        self,
        from_: 'User',
        paid_media_payload: 'str'
    ):
        self.from_ = from_
        self.paid_media_payload = paid_media_payload