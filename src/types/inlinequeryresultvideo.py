from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultVideo:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        video_url: 'str',
        mime_type: 'str',
        thumbnail_url: 'str',
        title: 'str',
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        video_width: 'Optional[int]' = None,
        video_height: 'Optional[int]' = None,
        video_duration: 'Optional[int]' = None,
        description: 'Optional[str]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
    ):
        self.type = type
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content