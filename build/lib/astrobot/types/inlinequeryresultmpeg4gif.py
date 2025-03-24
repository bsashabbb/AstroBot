from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultMpeg4Gif:
    """InlineQueryResultMpeg4Gif Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        mpeg4_url: str,
        mpeg4_width: Optional[int],
        mpeg4_height: Optional[int],
        mpeg4_duration: Optional[int],
        thumbnail_url: str,
        thumbnail_mime_type: Optional[str],
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
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
