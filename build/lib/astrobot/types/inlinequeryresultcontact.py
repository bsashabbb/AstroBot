from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultContact:
    """InlineQueryResultContact Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str],
        vcard: Optional[str],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent'],
        thumbnail_url: Optional[str],
        thumbnail_width: Optional[int],
        thumbnail_height: Optional[int]
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
