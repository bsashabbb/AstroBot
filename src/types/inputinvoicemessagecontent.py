from __future__ import annotations
from typing import Optional, List, Union

class InputInvoiceMessageContent:
    def __init__(
        self,
        title: 'str',
        description: 'str',
        payload: 'str',
        currency: 'str',
        prices: 'List[LabeledPrice]',
        provider_token: 'Optional[str]' = None,
        max_tip_amount: 'Optional[int]' = None,
        suggested_tip_amounts: 'Optional[List[int]]' = None,
        provider_data: 'Optional[str]' = None,
        photo_url: 'Optional[str]' = None,
        photo_size: 'Optional[int]' = None,
        photo_width: 'Optional[int]' = None,
        photo_height: 'Optional[int]' = None,
        need_name: 'Optional[bool]' = None,
        need_phone_number: 'Optional[bool]' = None,
        need_email: 'Optional[bool]' = None,
        need_shipping_address: 'Optional[bool]' = None,
        send_phone_number_to_provider: 'Optional[bool]' = None,
        send_email_to_provider: 'Optional[bool]' = None,
        is_flexible: 'Optional[bool]' = None
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