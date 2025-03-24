from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultCachedSticker:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        sticker_file_id: 'str',
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
    ):
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content