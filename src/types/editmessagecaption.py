from __future__ import annotations
from typing import Optional, List, Union

class editMessageCaption:
    def __init__(
        self,
        business_connection_id: 'Optional[str]' = None,
        chat_id: 'Optional[Union[str]]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup