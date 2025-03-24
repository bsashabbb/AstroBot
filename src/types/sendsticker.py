from __future__ import annotations
from typing import Optional, List, Union

class sendSticker:
    def __init__(
        self,
        chat_id: 'Union[str]',
        sticker: 'Union[str]',
        business_connection_id: 'Optional[str]' = None,
        message_thread_id: 'Optional[int]' = None,
        emoji: 'Optional[str]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        message_effect_id: 'Optional[str]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[Union[ReplyKeyboardMarkup]]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.sticker = sticker
        self.emoji = emoji
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup