from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultCachedVideo:
    """InlineQueryResultCachedVideo Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        video_file_id: str,
        title: str,
        description: Optional[str],
        caption: Optional[str],
        parse_mode: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        show_caption_above_media: Optional[bool],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent']
    ):
        self.type = type
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
