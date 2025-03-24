from __future__ import annotations
from typing import Optional, List, Union, Any

class Invoice:
    """Invoice Telegram API type"""

    def __init__(
        self,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount
