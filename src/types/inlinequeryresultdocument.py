from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultDocument:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        title: 'str',
        document_url: 'str',
        mime_type: 'str',
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        description: 'Optional[str]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None,
        thumbnail_url: 'Optional[str]' = None,
        thumbnail_width: 'Optional[int]' = None,
        thumbnail_height: 'Optional[int]' = None
    ):
        self.type = type
        self.id = id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height