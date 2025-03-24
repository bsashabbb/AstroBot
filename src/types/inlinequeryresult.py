from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResult:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        title: 'str',
        input_message_content: 'InputMessageContent',
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        url: 'Optional[str]' = None,
        description: 'Optional[str]' = None,
        thumbnail_url: 'Optional[str]' = None,
        thumbnail_width: 'Optional[int]' = None,
        thumbnail_height: 'Optional[int]' = None
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