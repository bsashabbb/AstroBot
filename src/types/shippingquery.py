from __future__ import annotations
from typing import Optional, List, Union

class ShippingQuery:
    def __init__(
        self,
        id: 'str',
        from_: 'User',
        invoice_payload: 'str',
        shipping_address: 'ShippingAddress'
    ):
        self.id = id
        self.from_ = from_
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address