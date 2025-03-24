from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultCachedDocument:
    """InlineQueryResultCachedDocument Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str],
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
