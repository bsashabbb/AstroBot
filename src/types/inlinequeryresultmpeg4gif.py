from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultMpeg4Gif:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        mpeg4_url: 'str',
        thumbnail_url: 'str',
        mpeg4_width: 'Optional[int]' = None,
        mpeg4_height: 'Optional[int]' = None,
        mpeg4_duration: 'Optional[int]' = None,
        thumbnail_mime_type: 'Optional[str]' = None,
        title: 'Optional[str]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
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