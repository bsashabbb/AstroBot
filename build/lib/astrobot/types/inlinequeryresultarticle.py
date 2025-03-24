from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultArticle:
    """InlineQueryResultArticle Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        title: str,
        input_message_content: 'InputMessageContent',
        reply_markup: Optional['InlineKeyboardMarkup'],
        url: Optional[str],
        description: Optional[str],
        thumbnail_url: Optional[str],
        thumbnail_width: Optional[int],
        thumbnail_height: Optional[int]
    ):
        self.type = type
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
