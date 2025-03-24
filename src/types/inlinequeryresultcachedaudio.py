from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultCachedAudio:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        audio_file_id: 'str',
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
    ):
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content