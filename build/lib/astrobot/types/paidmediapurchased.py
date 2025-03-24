from __future__ import annotations
from typing import Optional, List, Union, Any

class PaidMediaPurchased:
    """PaidMediaPurchased Telegram API type"""

    def __init__(
        self,
        from_user: 'User',
        paid_media_payload: str
    ):
        self.from_user = from_user
        self.paid_media_payload = paid_media_payload
