from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultCachedVoice:
    """InlineQueryResultCachedVoice Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        voice_file_id: str,
        title: str,
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
