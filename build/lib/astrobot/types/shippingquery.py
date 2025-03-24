from __future__ import annotations
from typing import Optional, List, Union, Any

class ShippingQuery:
    """ShippingQuery Telegram API type"""

    def __init__(
        self,
        id: str,
        from_user: 'User',
        invoice_payload: str,
        shipping_address: 'ShippingAddress'
    ):
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address
