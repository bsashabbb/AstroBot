from __future__ import annotations
from typing import Optional, List, Union

class sendInvoice:
    def __init__(
        self,
        chat_id: 'Union[str]',
        title: 'str',
        description: 'str',
        payload: 'str',
        currency: 'str',
        prices: 'List[LabeledPrice]',
        message_thread_id: 'Optional[int]' = None,
        provider_token: 'Optional[str]' = None,
        max_tip_amount: 'Optional[int]' = None,
        suggested_tip_amounts: 'Optional[List[int]]' = None,
        start_parameter: 'Optional[str]' = None,
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
        is_flexible: 'Optional[bool]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        message_effect_id: 'Optional[str]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.start_parameter = start_parameter
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
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup