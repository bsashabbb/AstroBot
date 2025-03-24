from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultPhoto:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        photo_url: 'str',
        thumbnail_url: 'str',
        photo_width: 'Optional[int]' = None,
        photo_height: 'Optional[int]' = None,
        title: 'Optional[str]' = None,
        description: 'Optional[str]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
    ):
        self.type = type
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content