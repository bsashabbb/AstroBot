from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultDocument:
    """InlineQueryResultDocument Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        title: str,
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        document_url: str,
        mime_type: str,
        description: Optional[str],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent'],
        thumbnail_url: Optional[str],
        thumbnail_width: Optional[int],
        thumbnail_height: Optional[int]
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
