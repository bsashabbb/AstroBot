from __future__ import annotations
from typing import Optional, List, Union

class editMessageText:
    def __init__(
        self,
        text: 'str',
        business_connection_id: 'Optional[str]' = None,
        chat_id: 'Optional[Union[str]]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        entities: 'Optional[List[MessageEntity]]' = None,
        link_preview_options: 'Optional[LinkPreviewOptions]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.reply_markup = reply_markup