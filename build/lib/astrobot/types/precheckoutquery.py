from __future__ import annotations
from typing import Optional, List, Union, Any

class PreCheckoutQuery:
    """PreCheckoutQuery Telegram API type"""

    def __init__(
        self,
        id: str,
        from_user: 'User',
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str],
        order_info: Optional['OrderInfo']
    ):
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
