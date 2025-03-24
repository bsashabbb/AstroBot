from __future__ import annotations
from typing import Optional, List, Union, Any

class SuccessfulPayment:
    """SuccessfulPayment Telegram API type"""

    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        subscription_expiration_date: Optional[int],
        is_recurring: Optional[bool],
        is_first_recurring: Optional[bool],
        shipping_option_id: Optional[str],
        order_info: Optional['OrderInfo'],
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.subscription_expiration_date = subscription_expiration_date
        self.is_recurring = is_recurring
        self.is_first_recurring = is_first_recurring
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
