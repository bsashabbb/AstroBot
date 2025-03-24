from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultContact:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        phone_number: 'str',
        first_name: 'str',
        last_name: 'Optional[str]' = None,
        vcard: 'Optional[str]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None,
        thumbnail_url: 'Optional[str]' = None,
        thumbnail_width: 'Optional[int]' = None,
        thumbnail_height: 'Optional[int]' = None
    ):
        self.type = type
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height