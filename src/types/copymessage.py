from __future__ import annotations
from typing import Optional, List, Union

class copyMessage:
    def __init__(
        self,
        chat_id: 'Union[str]',
        from_chat_id: 'Union[str]',
        message_id: 'int',
        message_thread_id: 'Optional[int]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[Union[ReplyKeyboardMarkup]]' = None
    ):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.from_chat_id = from_chat_id
        self.message_id = message_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup