from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultAudio:
    """InlineQueryResultAudio Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        audio_url: str,
        title: str,
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        performer: Optional[str],
        audio_duration: Optional[int],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
