from __future__ import annotations
from typing import Optional, List, Union, Any

class ShippingOption:
    """ShippingOption Telegram API type"""

    def __init__(
        self,
        id: str,
        title: str,
        prices: List['LabeledPrice']
    ):
        self.id = id
        self.title = title
        self.prices = prices
