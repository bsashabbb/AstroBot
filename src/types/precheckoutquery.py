from __future__ import annotations
from typing import Optional, List, Union

class PreCheckoutQuery:
    def __init__(
        self,
        id: 'str',
        from_: 'User',
        currency: 'str',
        total_amount: 'int',
        invoice_payload: 'str',
        shipping_option_id: 'Optional[str]' = None,
        order_info: 'Optional[OrderInfo]' = None
    ):
        self.id = id
        self.from_ = from_
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info