from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultCachedMpeg4Gif:
    """InlineQueryResultCachedMpeg4Gif Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str],
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        show_caption_above_media: Optional[bool],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
