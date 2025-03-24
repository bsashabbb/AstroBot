from __future__ import annotations
from typing import Optional, List, Union, Any

class InputInvoiceMessageContent:
    """InputInvoiceMessageContent Telegram API type"""

    def __init__(
        self,
        title: str,
        description: str,
        payload: str,
        provider_token: Optional[str],
        currency: str,
        prices: List['LabeledPrice'],
        max_tip_amount: Optional[int],
        suggested_tip_amounts: Optional[List[int]],
        provider_data: Optional[str],
        photo_url: Optional[str],
        photo_size: Optional[int],
        photo_width: Optional[int],
        photo_height: Optional[int],
        need_name: Optional[bool],
        need_phone_number: Optional[bool],
        need_email: Optional[bool],
        need_shipping_address: Optional[bool],
        send_phone_number_to_provider: Optional[bool],
        send_email_to_provider: Optional[bool],
        is_flexible: Optional[bool]
    ):
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible
