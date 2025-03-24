from __future__ import annotations
from typing import Optional, List, Union

class editMessageMedia:
    def __init__(
        self,
        media: 'InputMedia',
        business_connection_id: 'Optional[str]' = None,
        chat_id: 'Optional[Union[str]]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.media = media
        self.reply_markup = reply_markup