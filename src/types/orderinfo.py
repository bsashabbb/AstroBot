from __future__ import annotations
from typing import Optional, List, Union

class OrderInfo:
    def __init__(
        self,
        name: 'Optional[str]' = None,
        phone_number: 'Optional[str]' = None,
        email: 'Optional[str]' = None,
        shipping_address: 'Optional[ShippingAddress]' = None
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address