from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultVoice:
    """InlineQueryResultVoice Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        voice_url: str,
        title: str,
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        voice_duration: Optional[int],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
