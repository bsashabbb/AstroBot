from __future__ import annotations
from typing import Optional, List, Union, Any

class OrderInfo:
    """OrderInfo Telegram API type"""

    def __init__(
        self,
        name: Optional[str],
        phone_number: Optional[str],
        email: Optional[str],
        shipping_address: Optional['ShippingAddress']
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address
