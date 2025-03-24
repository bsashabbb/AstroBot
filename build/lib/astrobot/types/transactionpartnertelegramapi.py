from __future__ import annotations
from typing import Optional, List, Union, Any

class TransactionPartnerTelegramApi:
    """TransactionPartnerTelegramApi Telegram API type"""

    def __init__(
        self,
        type: str,
        request_count: int
    ):
        self.type = type
        self.request_count = request_count
